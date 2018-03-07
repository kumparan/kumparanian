import unittest
import subprocess


class TestCLI(unittest.TestCase):
    def test_kumparanian(self):

        with open("tests/kumparanian.output") as f:
            expected_output = f.read()
        command = "kumparanian"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_help(self):
        with open("tests/kumparanian_help.output") as f:
            expected_output = f.read()
        command = "kumparanian"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds(self):
        with open("tests/kumparanian_ds.output") as f:
            expected_output = f.read()
        command = "kumparanian ds"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_help(self):
        with open("tests/kumparanian_ds_help.output") as f:
            expected_output = f.read()
        command = "kumparanian ds --help"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify(self):
        with open("tests/kumparanian_ds_verify.output") as f:
            expected_output = f.read()
        command = "kumparanian ds verify; exit 0"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_help(self):
        with open("tests/kumparanian_ds_verify_help.output") as f:
            expected_output = f.read()
        command = "kumparanian ds verify --help"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_valid_model(self):
        with open("tests/kumparanian_ds_verify_valid_model.output") as f:
            expected_output = f.read()
        command = "kumparanian ds verify tests/valid_model.pickle"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_verify_invalid_model(self):
        with open("tests/kumparanian_ds_verify_invalid_model.output") as f:
            expected_output = f.read()
        command = "kumparanian ds verify tests/invalid_model.pickle; exit 0"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate(self):
        with open("tests/kumparanian_ds_evaluate.output") as f:
            expected_output = f.read()
        command = "kumparanian ds evaluate; exit 0"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_help(self):
        with open("tests/kumparanian_ds_evaluate_help.output") as f:
            expected_output = f.read()
        command = "kumparanian ds evaluate --help"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model(self):
        with open("tests/kumparanian_ds_evaluate_model.output") as f:
            expected_output = f.read()
        command = "kumparanian ds evaluate tests/valid_model.pickle; exit 0"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_ds_evaluate_model_test(self):
        with open("tests/kumparanian_ds_evaluate_model_test.output") as f:
            expected_output = f.read()
        command = ("kumparanian ds evaluate tests/valid_model.pickle "
                   "tests/test_set.csv; exit 0")
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de(self):
        with open("tests/kumparanian_de.output") as f:
            expected_output = f.read()
        command = "kumparanian de"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_help(self):
        with open("tests/kumparanian_de_help.output") as f:
            expected_output = f.read()
        command = "kumparanian de --help"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))

    def test_kumparanian_de_generate_dataset_help(self):
        with open("tests/kumparanian_de_generate_dataset_help.output") as f:
            expected_output = f.read()
        command = "kumparanian de generate-dataset --help"
        output = subprocess.check_output(command,
                                         stderr=subprocess.STDOUT,
                                         shell=True)
        self.assertEqual(expected_output, output.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
