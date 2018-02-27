import pickle


def verify_model(path):
    """Verify trained model.

    Model is valid if:
    1. It is a pickle file
    2. It implements a predict method that accepts a string
       argument (article_content)
    3. It implements a predict method that returns a string
       (article_topic)
    """
    model_file = open(path, "rb")
    try:
        model = pickle.load(model_file)
        model_file.close()
    except Exception:
        model_file.close()
        raise ValueError("Invalid pickle file.")

    # Check the predict method
    example_content = "test article content"
    try:
        article_topic = model.predict(example_content)
    except AttributeError as err:
        error_msg = ("Model should contains predict method:"
                     "model.predict(artcile_content)")
        raise AttributeError(error_msg)
    except TypeError as err:
        error_msg = ("Model should accept string as argument:"
                     "model.predict(artcile_content)")
        raise TypeError(error_msg)

    # Make sure the article_topic is string
    error_msg = ("Predict method should return a string:"
                 "artcile_topic = model.predict(article_content)")
    assert isinstance(article_topic, str), error_msg

    return True
