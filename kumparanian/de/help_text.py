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
format.
"""

generate_short_help = "Generate the data"
generate_usage = """Generate the data

Example:
$ kumparanian de generate-dataset your_full_name_in_snake_case

More info:
$ kumparanian de --help
"""
