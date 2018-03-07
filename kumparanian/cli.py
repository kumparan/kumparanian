import click

import kumparanian.ds as ds
import kumparanian.de as de

# Help texts
epilog = ("If you found any issues, feel free report it at: "
          "https://github.com/kumparan/kumparanian/issues")


@click.group(epilog=epilog)
def cli():
    pass


@cli.group(name="ds", help=ds.help_text, epilog=epilog)
def ds_group():
    pass


@ds_group.command(short_help=ds.verify_short_help,
                  help=ds.verify_usage)
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


@ds_group.command(short_help=ds.evaluate_short_help,
                  help=ds.evaluate_usage)
@click.argument("model", type=click.Path(exists=True))
@click.argument("testfile", type=click.Path(exists=True))
def evaluate(model, testfile):
    # Make sure the model is valid
    try:
        ds.model.verify(model)
    except Exception:
        message = "Model is invalid, please verify the model"
        click.secho(message, fg="red")
        exit(1)

    # Evaluate the model; only shows accuracy
    acc = ds.model.evaluate(model, testfile, data_type="topic_model")
    click.echo("Accuracy: {}".format(acc))


@cli.group(name="de", help=de.help_text, epilog=epilog)
def de_group():
    pass


@de_group.command(name="generate-dataset",
                  short_help=de.generate_short_help,
                  help=de.generate_usage)
@click.argument("candidate_name", type=str)
@click.option("--output-dir",
              default="data",
              help="Output directory",
              type=click.Path(exists=False,
                              file_okay=False,
                              writable=True))
@click.option("--num-files", default=40, type=int, help="Number of files")
@click.option("--num-workers", default=4, type=int, help="Number of workers")
def generate_dataset(candidate_name, output_dir, num_files, num_workers):
    de.dataset.generate_data(candidate_name=candidate_name,
                             output_dir=output_dir,
                             num_files=num_files,
                             num_workers=num_workers)
    click.secho("[kumparanian] Output: " + output_dir + "/", fg="green")


def main():
    cli()
