import unittest

from kumparanian import ds


# Test data
class ValidModel:
    def predict(self, article_content):
        article_topic = "test"
        return article_topic


class InvalidModelNoPredict:
    pass


class InvalidModelPredictArg:
    def predict(self):
        article_topic = "test"
        return article_topic


class InvalidModelPredictReturn:
    def predict(self, article_content):
        article_topic = "test"
        return [article_topic]


class TestVerifyModel(unittest.TestCase):
    def test_invalid_pickle(self):
        # TODO:
        # - load dummy invalid pickle file
        # Write a random file
        file_name = "test_invalid_pickle.txt"
        with open(file_name, "w") as f:
            f.write("invalid pickle file")
        with self.assertRaisesRegex(ValueError, "Invalid pickle file"):
            ds.verify_model(file_name)


if __name__ == '__main__':
    unittest.main()
