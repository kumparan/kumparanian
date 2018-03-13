# Data Engineer help texts
de_help_text = """For Data Engineer role.

Run the following command to generate your own dataset:

$ kumparanian de generate-dataset your_full_name_in_snake_case

This command will generate multiple CSV files inside data/
directory. Note that this command will generate different dataset
with different name input, so make sure your input name is correct.
The total size of the data is roughly 4GB but unfortunately you only
have machine with 1GB or memory. To simulate this, you can
use ulimit -v 1000000.

Before you zip the folder and submit your work, you can verify
your submission using the following command:

$ kumparanian de verify de_your_full_name/

It make sure that required files is exists and in the correct
format. Please read your assesment email/document for the guideline.
"""

generate_short_help = "Generate the data"
generate_usage = """Generate the data

Example:
$ kumparanian de generate-dataset your_full_name_in_snake_case

More info:
$ kumparanian de --help
"""

verify_short_help = "Verify the submission"
verify_usage = """Verify the submission

Example:
$ kumparanian de verify de_<your_full_name_in_snake_case>/

More info:
$ kumparanian de --help
"""

evaluate_short_help = "Evaluate the submission"
evaluate_usage = """Evaluate the submission

Run the solution.py first:
$ python solution.py --code_id candidate_name --num_file=40

Evaluate the submission:
$ kumparanian de evaluate submission_dir/ solution_dir/

"""
