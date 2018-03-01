# Kumparanian
Kumparanian is a set of workflows that optimize Kumparan's data engineering 
and data scientist hiring process. It's cut down 1-2 working day(s) submission 
review process in just less than one hour. 

If you are our candidate, you need to install `kumparanian` first by using
the following command:

    pip install kumparanian 

Show the help command:

    % kumparanian ds --help
    Usage: kumparanian ds [OPTIONS] COMMAND [ARGS]...

      For Data Scientist role.

      Before you submit your trained model, you can verify your trained model
      using the following command:

      $ kumparanian ds verify YOURMODEL.pickle

      Use the following command to evaluate your trained model against your test
      dataset:

      $ kumparanian ds evaluate YOURMODEL.pickle test_file.csv

    Options:
      --help  Show this message and exit.

    Commands:
      evaluate  Evaluate the model
      verify    Verify the model

      If you found any issues, feel free report it at:
      https://github.com/kumparan/kumparanian/issues

Then read our assessment and you should be good.

The following section is not required for candidate, only for project's
documentation purpose.


## Kumparan's Model Interface
The first component of Kumparanian is a 
[Kumparan's Model Interface](./interface/model.py).
We've designed such interface for Machine Learning model that allow us to 
design a problem so that it will have a deterministic result.

The model interface contains 3 required methods: `train`, `predict` and 
`save`. The candidate will solve the assessment test by implement the `train` 
and `predict` methods. We provide `save` method to helps the candidate to save 
the trained model.

Read more about the [Kumparan's Model Interface](./interface/README.md).


## Kumparanian CLI
The second component of Kumparanian is a `kumparanian(1)`. This CLI will helps
the candidate to verify and test their model and helps our team to evaluate
the candidate's trained model.

`kumparanian(1)` can be installed via the following command:

    pip install kumparanian

To get started, run the following command:

    kumparanian --help



If you found any issue, please open new issue here 
[kumparanian/issues](https://github.com/kumparan/kumparanian/issues).


