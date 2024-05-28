import subprocess
import unittest


class TestCLI(unittest.TestCase):
    def test_kumparanian(self):
        with open("tests/kumparanian.output") as file:
            expected_output = file.read()
        command = "kumparanian"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_help(self):
        with open("tests/kumparanian_help.output") as file:
            expected_output = file.read()
        command = "kumparanian --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds(self):
        with open("tests/kumparanian_ds.output") as file:
            expected_output = file.read()
        command = "kumparanian ds"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_help(self):
        with open("tests/kumparanian_ds_help.output") as file:
            expected_output = file.read()
        command = "kumparanian ds --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify(self):
        with open("tests/kumparanian_ds_verify.output") as file:
            expected_output = file.read()
        command = "kumparanian ds verify; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_help(self):
        with open("tests/kumparanian_ds_verify_help.output") as file:
            expected_output = file.read()
        command = "kumparanian ds verify --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_valid_sklearn_model(self):
        with open("tests/kumparanian_ds_verify_valid_model.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/sklearn_valid_model.pickle "
            "tests/vectorizer_label_encoder.pickle"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_valid_tf_model(self):
        with open("tests/kumparanian_ds_verify_valid_model.output") as file:
            expected_output = file.read()
        command = "kumparanian ds verify tests/tf_valid_model.keras tests/tokenizer_label_encoder.pickle"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_pickle_file(self):
        with open("tests/kumparanian_ds_verify_invalid_pickle_file.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/invalid_pickle.pickle "
            "tests/tokenizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_tokenizer(self):
        with open("tests/kumparanian_ds_verify_invalid_tokenizer.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/tf_valid_model.keras "
            "tests/invalid_tokenizer.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_vectorizer(self):
        with open("tests/kumparanian_ds_verify_invalid_vectorizer.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/sklearn_valid_model.pickle "
            "tests/invalid_vectorizer.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_label_encoder(self):
        with open("tests/kumparanian_ds_verify_invalid_label_encoder.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/tf_valid_model.keras "
            "tests/invalid_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_model_predict(self):
        with open("tests/kumparanian_ds_verify_invalid_model_predict.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds verify tests/invalid_model.pickle "
            "tests/vectorizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate(self):
        with open("tests/kumparanian_ds_evaluate.output") as file:
            expected_output = file.read()
        command = "kumparanian ds evaluate; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_help(self):
        with open("tests/kumparanian_ds_evaluate_help.output") as file:
            expected_output = file.read()
        command = "kumparanian ds evaluate --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model(self):
        with open("tests/kumparanian_ds_evaluate_model.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds evaluate tests/sklearn_valid_model.pickle "
            "tests/vectorizer_label_encoder.pickle; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model_test(self):
        with open("tests/kumparanian_ds_evaluate_model_test.output") as file:
            expected_output = file.read()
        command = (
            "kumparanian ds evaluate tests/tf_valid_model.keras tests/tokenizer_label_encoder.pickle "
            "tests/test_set.csv; exit 0"
        )
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de(self):
        with open("tests/kumparanian_de.output") as f:
            expected_output = f.read()
        command = "kumparanian de"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_help(self):
        with open("tests/kumparanian_de_help.output") as f:
            expected_output = f.read()
        command = "kumparanian de --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_generate_dataset_help(self):
        with open("tests/kumparanian_de_generate_dataset_help.output") as f:
            expected_output = f.read()
        command = "kumparanian de generate-dataset --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_verify(self):
        with open("tests/kumparanian_de_verify.output") as f:
            expected_output = f.read()
        command = "kumparanian de verify; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_verify_help(self):
        with open("tests/kumparanian_de_verify_help.output") as f:
            expected_output = f.read()
        command = "kumparanian de verify --help"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_verify_valid(self):
        with open("tests/kumparanian_de_verify_valid.output") as f:
            expected_output = f.read()
        command = "kumparanian de verify tests/de/de_test_valid/; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_verify_invalid(self):
        with open("tests/kumparanian_de_verify_invalid.output") as f:
            expected_output = f.read()
        command = "kumparanian de verify tests/de/de_test_invalid/; exit 0"
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
