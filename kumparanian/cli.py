import click

import kumparanian.ds as ds

# Help text
epilog = ("If you found any issues, feel free report it at: "
          "https://github.com/kumparan/kumparanian/issues")
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


@click.group(epilog=epilog)
def cli():
    pass


@cli.group(name="ds", help=ds_help_text, epilog=epilog)
def ds_group():
    pass


@ds_group.command(short_help=verify_short_help, help=verify_usage)
@click.argument("model", type=click.Path(exists=True))
def verify(model):
    try:
        ds.model.verify(model)
    except Exception as err:
        message = "[INVALID] {}".format(err)
        click.secho(message, fg="red")
        exit(1)
    click.secho("[VALID] Model is valid.", fg="green")
    exit(0)


@ds_group.command(help="Evaluate the model")
@click.option("--model",
              required=True,
              type=click.Path(exists=True),
              help="Path to model pickle file")
@click.option("--test",
              required=True,
              type=click.Path(exists=True),
              help="Path test set CSV file")
def evaluate():
    click.echo("test")


def main():
    cli()
