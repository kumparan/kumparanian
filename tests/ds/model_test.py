import unittest

import dill

import kumparanian.ds as ds


# Test data
class ValidModel:
    def predict(self, article_content):
        article_topic = "test"
        return article_topic


class InvalidModelNoPredict:
    test = "value"


class InvalidModelPredictArg:
    def predict(self):
        article_topic = "test"
        return article_topic


class InvalidModelPredictReturn:
    def predict(self, article_content):
        article_topic = "test"
        return [article_topic]


class TestModel(unittest.TestCase):
    def test_save_model(self):
        model = {}
        filename = "test_saved_model.pickle"
        ds.model.save(model, filename)

        with open(filename, "rb") as f:
            loaded_model = dill.load(f)
            self.assertEqual(model, loaded_model)

    def test_invalid_pickle(self):
        # Write a random file
        file_name = "test_invalid_pickle.txt"
        with open(file_name, "w") as f:
            f.write("invalid pickle file")
        with self.assertRaisesRegex(ValueError, "Invalid pickle file"):
            ds.model.verify(file_name)

    def test_invalid_model_no_predict(self):
        # Create a pickle file
        file_name = "test_invalid_model_no_predict.pickle"
        with open(file_name, "wb") as f:
            invalid_model = InvalidModelNoPredict()
            dill.dump(invalid_model, f)

        error_msg = "Model should contains predict method"
        with self.assertRaisesRegex(AttributeError, error_msg):
            ds.model.verify(file_name)

    def test_invalid_model_predict_arg(self):
        # Create a pickle file
        file_name = "test_invalid_model_predict_arg.pickle"
        with open(file_name, "wb") as f:
            invalid_model = InvalidModelPredictArg()
            dill.dump(invalid_model, f)

        error_msg = "Model should accept string as argument"
        with self.assertRaisesRegex(TypeError, error_msg):
            ds.model.verify(file_name)

    def test_invalid_model_predict_ret(self):
        # Create a pickle file
        file_name = "test_invalid_model_predict_ret.pickle"
        with open(file_name, "wb") as f:
            invalid_model = InvalidModelPredictReturn()
            dill.dump(invalid_model, f)

        error_msg = "Predict method should return a string"
        with self.assertRaisesRegex(AssertionError, error_msg):
            ds.model.verify(file_name)

    def test_valid_model(self):
        # Create a pickle file
        file_name = "test_valid_model.pickle"
        with open(file_name, "wb") as f:
            valid_model = ValidModel()
            dill.dump(valid_model, f)

        self.assertTrue(ds.model.verify(file_name))


if __name__ == "__main__":
    unittest.main()
