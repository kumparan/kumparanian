import subprocess
import unittest


class TestCLI(unittest.TestCase):
    def test_kumparanian(self):
        with open("tests/kumparanian.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_help(self):
        with open("tests/kumparanian_help.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds(self):
        with open("tests/kumparanian_ds.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_help(self):
        with open("tests/kumparanian_ds_help.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify(self):
        with open("tests/kumparanian_ds_verify.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds verify; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_help(self):
        with open("tests/kumparanian_ds_verify_help.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds verify --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_valid_sklearn_model(self):
        with open("tests/kumparanian_ds_verify_valid_model.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/sklearn_valid_model.pickle "
            "tests/vectorizer_label_encoder.pickle"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_valid_tf_model(self):
        with open("tests/kumparanian_ds_verify_valid_model.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds verify tests/tf_valid_model.keras tests/tokenizer_label_encoder.pickle"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_pickle_file(self):
        with open("tests/kumparanian_ds_verify_invalid_pickle_file.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/invalid_pickle.pickle "
            "tests/tokenizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_tokenizer(self):
        with open("tests/kumparanian_ds_verify_invalid_tokenizer.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/tf_valid_model.keras "
            "tests/invalid_tokenizer.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_vectorizer(self):
        with open("tests/kumparanian_ds_verify_invalid_vectorizer.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/sklearn_valid_model.pickle "
            "tests/invalid_vectorizer.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_label_encoder(self):
        with open("tests/kumparanian_ds_verify_invalid_label_encoder.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/tf_valid_model.keras "
            "tests/invalid_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_model_predict(self):
        with open("tests/kumparanian_ds_verify_invalid_model_predict.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds verify tests/invalid_model.pickle "
            "tests/vectorizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate(self):
        with open("tests/kumparanian_ds_evaluate.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds evaluate; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_help(self):
        with open("tests/kumparanian_ds_evaluate_help.output") as file:
            expected_output = file.read()
        command = "python -m kumparanian ds evaluate --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model(self):
        with open("tests/kumparanian_ds_evaluate_model.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds evaluate tests/sklearn_valid_model.pickle "
            "tests/vectorizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model_test(self):
        with open("tests/kumparanian_ds_evaluate_model_test.output") as file:
            expected_output = file.read()
        command = (
            "python -m kumparanian ds evaluate tests/tf_valid_model.keras tests/tokenizer_label_encoder.pickle "
            "tests/test_set.csv; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
