import click

from .ds import verify_model


@click.group()
def cli():
    pass


ds_help_text = """For data Scientist role.

Before you submit your trained model, you can verify your trained model using
the following command:

$ kumparanian ds verify --model YOURMODEL.pickle

Use the following command to evaluate your trained model against your test
dataset:

$ kumparanian ds evaluate --model YOURMODEL.pickle --test-set file.csv

If you found any issues, feel free report it at:
https://github.com/kumparan/kumparanian/issues

"""


@cli.group(name="ds", help=ds_help_text)
def ds_group():
    pass


@ds_group.command(help="Verify the model")
@click.option("--model",
              required=True,
              type=click.Path(exists=True),
              help="Path to model pickle file")
def verify(model):
    try:
        verify_model(model)
    except Exception as err:
        message = "Error: {}".format(err)
        click.secho(message, fg="red")
    click.secho("Model is valid.", fg="green")
    

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
