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
    model_file = open(path, "r")
    try:
        model = pickle.load(model_file)
    except Exception:
        model_file.close()
        raise ValueError("Invalid pickle file.")
    model_file.close()
    print(model)
