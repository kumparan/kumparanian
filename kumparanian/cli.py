import multiprocessing

import click

import kumparanian.ds as ds

# Help texts
epilog = (
    "If you found any issues, feel free report it at: "
    "https://github.com/kumparan/kumparanian/issues"
)


@click.group(epilog=epilog)
def cli():
    pass


@cli.group(name="ds", help=ds.help_text, epilog=epilog)
def ds_group():
    pass


@ds_group.command(short_help=ds.verify_short_help, help=ds.verify_usage)
@click.argument("model", type=click.Path(exists=True))
@click.argument("file", type=click.Path(exists=True))
def verify(model, file):
    try:
        ds.model.verify(model, file)
    except Exception as err:
        message = "[INVALID] {}".format(err)
        click.secho(message, fg="red")
        exit(1)
    click.secho("[VALID] Model is valid.", fg="green")
    exit(0)


@ds_group.command(short_help=ds.evaluate_short_help, help=ds.evaluate_usage)
@click.argument("model", type=click.Path(exists=True))
@click.argument("file", type=click.Path(exists=True))
@click.argument("testfile", type=click.Path(exists=True))
def evaluate(model, file, testfile):
    # Make sure the model is valid
    try:
        ds.model.verify(model, file)
    except Exception:
        message = "Model is invalid, please verify the model"
        click.secho(message, fg="red")
        exit(1)

    # Evaluate the model; only shows accuracy
    acc = ds.model.evaluate(model, file, testfile, data_type="topic_model")
    click.echo("Accuracy: {}".format(acc))


def main():
    cli()


if __name__ == "__main__":
    # handle "Error: No such option: --multiprocessing-fork"
    # read more https://github.com/pyinstaller/pyinstaller/issues/2023
    multiprocessing.freeze_support()
    cli()
