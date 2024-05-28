import os
import unittest

# Set the logging level for TensorFlow to hide warnings and informational
# messages. This is done to reduce noise in the console output.
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Dense, Embedding, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

import kumparanian.ds.model as model


class ValidSKLearnModel:
    """Dummy Valid Scikit-Learn Model."""

    def predict(self, x_input):
        return np.array([0])


class InvalidModelNoPredict:
    """Dummy Invalid Model: No Prediction Method."""

    pass


class InvalidModelPredictArg:
    """Dummy Invalid Model: Prediction Method with Invalid Argument."""

    def predict(self, x_input):
        if not isinstance(x_input, np.ndarray):
            raise ValueError("Invalid argument type")
        return np.array([0])


class InvalidModelPredictReturn:
    """Dummy Invalid Model: Prediction Method with Invalid Return."""

    def predict(self, x_input):
        return ["invalid_prediction"]


def create_valid_tf_model():
    """Dummy Valid Tensorflow Model."""

    tf_model = Sequential()
    tf_model.add(
        Embedding(input_dim=1000, output_dim=64, input_length=10, name="embedding")
    )
    tf_model.add(Flatten())
    tf_model.add(Dense(1, activation="sigmoid", name="dense"))
    tf_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return tf_model


# Test Cases
class TestModel(unittest.TestCase):
    """Test cases for the model."""

    def setUp(self):
        """Set up common objects for testing."""
        self.valid_vectorizer = TfidfVectorizer()
        self.valid_vectorizer.fit(["sample text"])
        self.valid_label_encoder = LabelEncoder()
        self.valid_label_encoder.fit(["test"])
        self.valid_tokenizer = Tokenizer()
        self.valid_tokenizer.fit_on_texts(["sample text"])
        self.sklearn_model_path = "test_sklearn_model.pickle"
        self.file_path = "test_file.pickle"
        self.tf_model_path = "test_tf_model.keras"

    def test_save_sklearn_model(self):
        """Test saving and loading a Scikit-Learn model."""
        model_obj = ValidSKLearnModel()
        preprocessor = self.valid_vectorizer
        label_encoder = self.valid_label_encoder

        model.save(
            model_obj,
            preprocessor,
            label_encoder,
            self.sklearn_model_path,
            self.file_path,
        )
        loaded_model, loaded_label_encoder, loaded_vectorizer, loaded_model_extension = (
            model.Model.load(self.sklearn_model_path, self.file_path)
        )

        sample_input = self.valid_vectorizer.transform(["sample text"])
        self.assertTrue(
            np.array_equal(
                model_obj.predict(sample_input), loaded_model.predict(sample_input)
            )
        )

    def test_save_tf_model(self):
        """Test saving and loading a TensorFlow model."""
        model_obj = create_valid_tf_model()
        preprocessor = self.valid_tokenizer
        label_encoder = self.valid_label_encoder

        model.save(
            model_obj,
            preprocessor,
            label_encoder,
            self.tf_model_path,
            self.file_path,
        )
        loaded_model, loaded_label_encoder, loaded_tokenizer, loaded_model_extension = (
            model.Model.load(self.tf_model_path, self.file_path)
        )

        sample_input = self.valid_tokenizer.texts_to_sequences(["sample text"])
        sample_input = pad_sequences(sample_input, maxlen=10)
        self.assertTrue(
            np.array_equal(
                model_obj.predict(sample_input, verbose=0),
                loaded_model.predict(sample_input, verbose=0),
            )
        )

    def test_invalid_pickle(self):
        """Test case for handling invalid pickle files."""
        file_name = "test_invalid_pickle.pickle"
        with open(file_name, "w") as f:
            f.write("invalid pickle file")
        with self.assertRaises(ValueError):
            model.verify(self.sklearn_model_path, file_name)
        os.remove(file_name)

    def test_invalid_model_no_predict(self):
        """Test case for handling models with no predict method."""
        model_obj = InvalidModelNoPredict()
        preprocessor = self.valid_vectorizer
        label_encoder = self.valid_label_encoder

        with open(self.file_path, "wb") as f:
            pickle.dump(
                {
                    "vectorizer": preprocessor,
                    "label_encoder": label_encoder,
                },
                f,
            )
        with open(self.sklearn_model_path, "wb") as f:
            pickle.dump(model_obj, f)

        with self.assertRaises(AttributeError):
            model.verify(self.sklearn_model_path, self.file_path)

    def test_invalid_model_predict_arg(self):
        """Test case for handling models with predict method having invalid arguments."""
        model_obj = InvalidModelPredictArg()
        preprocessor = self.valid_vectorizer
        label_encoder = self.valid_label_encoder

        with open(self.file_path, "wb") as f:
            pickle.dump(
                {
                    "vectorizer": preprocessor,
                    "label_encoder": label_encoder,
                },
                f,
            )
        with open(self.sklearn_model_path, "wb") as f:
            pickle.dump(model_obj, f)

        with self.assertRaises(ValueError):
            model.verify(self.sklearn_model_path, self.file_path)

    def test_invalid_model_predict_return(self):
        """Test case for handling models with predict method returning invalid types."""
        model_obj = InvalidModelPredictReturn()
        preprocessor = self.valid_vectorizer
        label_encoder = self.valid_label_encoder

        with open(self.file_path, "wb") as f:
            pickle.dump(
                {
                    "vectorizer": preprocessor,
                    "label_encoder": label_encoder,
                },
                f,
            )
        with open(self.sklearn_model_path, "wb") as f:
            pickle.dump(model_obj, f)

        with self.assertRaises(TypeError):
            model.verify(self.sklearn_model_path, self.file_path)

    def test_invalid_tokenizer(self):
        """Test case for handling invalid tokenizers."""
        model_obj = create_valid_tf_model()
        invalid_tokenizer = "Invalid Tokenizer"
        label_encoder = self.valid_label_encoder

        model.save(
            model_obj,
            invalid_tokenizer,
            label_encoder,
            self.tf_model_path,
            self.file_path,
        )
        with self.assertRaises(TypeError):
            model.verify(self.tf_model_path, self.file_path)

    def test_invalid_vectorizer(self):
        """Test case for handling invalid vectorizers."""
        invalid_model_obj = InvalidModelNoPredict()
        preprocessor = "Invalid Vectorizer"
        label_encoder = self.valid_label_encoder

        with open(self.file_path, "wb") as f:
            pickle.dump(
                {
                    "vectorizer": preprocessor,
                    "label_encoder": label_encoder,
                },
                f,
            )
        with open(self.sklearn_model_path, "wb") as f:
            pickle.dump(invalid_model_obj, f)

        with self.assertRaises(TypeError):
            model.verify(self.sklearn_model_path, self.file_path)

    def test_invalid_label_encoder(self):
        """Test case for handling invalid label encoders."""
        invalid_model_obj = InvalidModelNoPredict()
        preprocessor = self.valid_vectorizer
        label_encoder = "Invalid Label Encoder"

        with open(self.file_path, "wb") as f:
            pickle.dump(
                {
                    "vectorizer": preprocessor,
                    "label_encoder": label_encoder,
                },
                f,
            )
        with open(self.sklearn_model_path, "wb") as f:
            pickle.dump(invalid_model_obj, f)

        with self.assertRaises(TypeError):
            model.verify(self.sklearn_model_path, self.file_path)

    def test_valid_sklearn_model(self):
        """Test case for handling valid Scikit-Learn models."""
        model_obj = ValidSKLearnModel()
        preprocessor = self.valid_vectorizer
        label_encoder = self.valid_label_encoder

        model.save(
            model_obj,
            preprocessor,
            label_encoder,
            self.sklearn_model_path,
            self.file_path,
        )
        self.assertTrue(model.verify(self.sklearn_model_path, self.file_path))

    def test_valid_tf_model(self):
        """Test case for handling valid TensorFlow models."""
        model_obj = create_valid_tf_model()
        preprocessor = self.valid_tokenizer
        label_encoder = self.valid_label_encoder

        model.save(
            model_obj,
            preprocessor,
            label_encoder,
            self.tf_model_path,
            self.file_path,
        )
        self.assertTrue(model.verify(self.tf_model_path, self.file_path))


if __name__ == "__main__":
    unittest.main()
