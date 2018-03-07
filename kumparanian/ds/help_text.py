# Data Scientist Help Texts
ds_help_text = """For Data Scientist role.

Before you submit your trained model, you can verify your trained model using
the following command:

$ kumparanian ds verify YOURMODEL.pickle

Use the following command to evaluate your trained model against your test
dataset:

$ kumparanian ds evaluate YOURMODEL.pickle test_file.csv
"""

verify_short_help = "Verify the model"
verify_usage = """Verify the model

Example:
$ kumparanian ds verify YOURMODEL.pickle
"""

evaluate_short_help = "Evaluate the model"
evaluate_usage = """Evaluate the model

Example:

$ kumparanian ds evaluate YOURMODEL.pickle test_file.csv
"""
