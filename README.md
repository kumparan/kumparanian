# Kumparanian [![Build Status](https://travis-ci.org/kumparan/kumparanian.svg?branch=master)](https://travis-ci.org/kumparan/kumparanian) [![PyPI version](https://badge.fury.io/py/kumparanian.svg)](https://badge.fury.io/py/kumparanian)
Kumparanian is a set of workflows that optimize Kumparan's data engineering 
and data scientist hiring process. It cuts down 1-2 working day(s) submission 
review process to just less than an hour.

If you are our candidate, you need to install `kumparanian` using following command (we highly recommend to install inside virtual env, like venv):

    python -m venv <your_env_name>

    source <your_env_name>/bin/activate

    pip install kumparanian 

consult its help command:

    % kumparanian ds --help
    Usage: kumparanian ds [OPTIONS] COMMAND [ARGS]...

      For Data Scientist role.

      Before you submit your trained model, you can verify your trained model
      using the following command:

      $ kumparanian ds verify YOURMODEL.pickle YOURFILE.pickle
    
      YOURMODEL.pickle should contain your trained model, and YOURFILE.pickle
      should contain the necessary preprocessing components such as the vectorizer, 
      label encoder, and model type.

      Use the following command to evaluate your trained model against your test
      dataset:

      $ kumparanian ds evaluate YOURMODEL.pickle YOURFILE.pickle test_file.csv

    Options:
      --help  Show this message and exit.

    Commands:
      evaluate  Evaluate the model
      verify    Verify the model

      If you found any issues, feel free report it at:
      https://github.com/kumparan/kumparanian/issues

then read our assessment and you should be good.

Subsequent sections are not required for candidate as it intended only for project's
documentation purpose.


## Kumparan's Model Interface
The first component of Kumparanian is a 
[Kumparan's Model Interface](./interface/model.py).
We've designed an interface for Machine Learning model that allows us to 
design a problem to have deterministic result.

The model interface contains 3 required methods: `train`, `predict` and 
`save`. The candidate will solve the assessment test by implement the `train` 
and `predict` methods. We provide `save` method to helps the candidate to save 
the trained model.

Read more about the [Kumparan's Model Interface](./interface/README.md).


## Kumparanian CLI
The second component of Kumparanian is a `kumparanian`. This CLI will help
the candidate to verify and test their model while also help our team to evaluate
the candidate's trained model.

`kumparanian` can be installed via the following command:

    pip install kumparanian

To get started, run the following command:

    kumparanian --help



If you found any issue, please open new issue here 
[kumparanian/issues](https://github.com/kumparan/kumparanian/issues).


