import csv
import os
import warnings

import pickle
import numpy as np

# Set the logging level for TensorFlow to hide warnings and informational
# messages. This is done to reduce noise in the console output.
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


def load_model_and_components(model_path, file_path):
    """
    Load trained model, vectorizer/tokenizer, and label encoder from file.

    Args:
        model_path (str): Path to the model file.
        file_path (str): Path to the file containing the vectorizer/tokenizer and label encoder.

    Returns:
        tuple: Contains the model, vectorizer/tokenizer, and label encoder
    """
    with open(file_path, "rb") as file:
        saved_data = pickle.load(file)

    label_encoder = saved_data["label_encoder"]
    model_extension = os.path.splitext(model_path)[1]

    if model_extension in [".pickle", ".pkl"]:
        with open(model_path, "rb") as model_file:
            model = pickle.load(model_file)
        vectorizer = saved_data["vectorizer"]
        return model, vectorizer, label_encoder, model_extension
    elif model_extension in [".keras"]:
        model = load_model(model_path, compile=False)
        tokenizer = saved_data["tokenizer"]
        return model, tokenizer, label_encoder, model_extension


def verify(model_path, file_path):
    """
    Verify trained model.

    Valid Scikit-learn Model Criteria:
    1. It is stored in the pickle file format.
    2. It gives string results after undergoing vectorization, prediction, and label encoding.

    Valid TensorFlow Model Criteria:
    1. It is stored in the keras file format.
    2. It gives string results after undergoing tokenization, prediction, and label encoding.

    Valid Vectorizer Criteria:
    1. It is a sklearn.feature_extraction.text.TfidfVectorizer instance.
    2. It is already fitted with the training data.

    Tokenizer is valid if:
    1. It is a tf.keras.preprocessing.text.Tokenizer instance.
    2. It is already fitted with the training data.

    Label Encoder is valid if:
    1. It is a sklearn.preprocessing.LabelEncoder instance.
    2. It is already fitted with the labels.

    Args:
        model_path (str): Path to the model file.
        file_path (str): Path to the file containing the vectorizer/tokenizer and label encoder.

    Returns:
        bool: True if the model is valid, otherwise raises an exception.
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            warnings.simplefilter("ignore", category=DeprecationWarning)
            model, preprocessor, label_encoder, model_extension = load_model_and_components(
                model_path, file_path
            )
    except Exception:
        raise ValueError(
            "Provided files should contain a model, a vectorizer/tokenizer, "
            "and a label encoder"
        )

    if not isinstance(label_encoder, LabelEncoder):
        raise TypeError(
            "Label encoder should be an instance of sklearn.preprocessing.LabelEncoder"
        )

    example_content = [
        "KBRN, Pekanbaru (MCH): Kloter Tujuh Embarkasi Batam yang mengangkut Jemaah Calon Haji (JCH)"
    ]

    if model_extension in [".pickle", ".pkl"]:
        if not isinstance(preprocessor, TfidfVectorizer):
            raise TypeError(
                "Vectorizer should be an instance of sklearn.feature_extraction.text.TfidfVectorizer"
            )
        vectorized_text = preprocessor.transform(example_content)

        if not hasattr(model, "predict"):
            raise AttributeError("Model should contain predict method")
        article_topic = model.predict(vectorized_text)

        if not isinstance(article_topic, np.ndarray):
            raise TypeError("Model's predict method should return a numpy.ndarray")
        predicted_labels = label_encoder.inverse_transform(article_topic)
        result = predicted_labels[0]

        if not isinstance(result, str):
            raise TypeError("The result should be a string")

    elif model_extension in [".keras"]:
        if not isinstance(preprocessor, Tokenizer):
            raise TypeError(
                "Tokenizer should be an instance of tf.keras.preprocessing.text.Tokenizer"
            )

        X_preprocessed = preprocessor.texts_to_sequences(example_content)
        max_sequence_length = model.input_shape[1]
        X_padded = pad_sequences(X_preprocessed, maxlen=max_sequence_length)

        if not hasattr(model, "predict"):
            raise AttributeError("Model should contain predict method")
        article_topic = model.predict(X_padded, verbose=0)

        if not isinstance(article_topic, np.ndarray):
            raise TypeError("Model's predict method should return a numpy.ndarray")
        predicted_class_index = article_topic.argmax(axis=1)[0]
        result = label_encoder.inverse_transform([predicted_class_index])[0]

        if not isinstance(result, str):
            raise TypeError("The result should be a string")

    return True


def save(
    model_object,
    preprocessor_object,
    label_encoder_object,
    model_path,
    file_path,
):
    """
    Save a model object and its components to separate files.

    Args:
        model_object (object): The model object to be saved (e.g., a scikit-learn or TensorFlow model).
        preprocessor_object (object): The preprocessor object (e.g., a tokenizer or vectorizer).
        label_encoder_object (object): The label encoder object.
        model_path (str): The path where the model object will be saved.
        file_path (str): The path where additional objects (tokenizer, label encoder) will be saved.
    """

    model_extension = os.path.splitext(model_path)[1]

    if model_extension in [".pickle", ".pkl"]:
        # Save the scikit-learn model using dill
        with open(model_path, "wb") as model_file:
            pickle.dump(model_object, model_file)

        # Save the vectorizer and label encoder in a separate file
        with open(file_path, "wb") as file:
            pickle.dump(
                {
                    "vectorizer": preprocessor_object,
                    "label_encoder": label_encoder_object,
                },
                file,
            )

    elif model_extension in [".keras"]:
        # Save the TensorFlow model using Keras' save model function
        model_object.save(model_path)

        # Save the tokenizer and label encoder in a separate file
        with open(file_path, "wb") as file:
            pickle.dump(
                {
                    "tokenizer": preprocessor_object,
                    "label_encoder": label_encoder_object,
                },
                file,
            )


def evaluate(model_path, file_path, test_set_path, data_type=None):
    """
    Evaluate the model accuracy; it assumes that the model is valid
    otherwise it will throw an exception.

    Args:
        model_path (str): Path to the model file.
        file_path (str): Path to the file containing the vectorizer/tokenizer and label encoder.
        test_set_path (str): Path to the CSV file containing the test set.
        data_type (str): Type of the model to evaluate.

    Returns:
        float: The accuracy of the model on the test set.
    """
    # Load the model first, pickle file should be verified first before evaluate
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        warnings.simplefilter("ignore", category=DeprecationWarning)
        model, preprocessor, label_encoder, model_extension = load_model_and_components(model_path, file_path)

    if data_type == "topic_model":
        with open(test_set_path, "r") as test_file:
            rows = csv.DictReader(test_file)
            sample_count = 0
            correct_predict = 0
            for row in rows:
                article_content = row["article_content"]
                expected_article_topic = row["article_topic"]

                if model_extension in [".pickle", ".pkl"]:
                    vectorized_text = preprocessor.transform([article_content])
                    article_topic_numeric = model.predict(vectorized_text)
                    predicted_article_topic = label_encoder.inverse_transform(
                        article_topic_numeric
                    )[0]
                elif model_extension in [".keras"]:
                    X_preprocessed = preprocessor.texts_to_sequences([article_content])
                    max_sequence_length = model.input_shape[1]
                    X_padded = pad_sequences(X_preprocessed, maxlen=max_sequence_length)
                    y_pred_labels = model.predict(X_padded, verbose=0)
                    predicted_class_index = y_pred_labels.argmax(axis=1)[0]
                    predicted_article_topic = label_encoder.inverse_transform(
                        [predicted_class_index]
                    )[0]

                sample_count += 1
                if predicted_article_topic == expected_article_topic:
                    correct_predict += 1

        accuracy = float(correct_predict) / sample_count
        return accuracy
