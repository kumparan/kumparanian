# Kumparan's Model Interface

[model.py](./model.py) is an interface file to implement 
your model.

You must implement `train` method and `predict` method.

`train` is a method to train your model. You can read
training data, preprocess and perform the training inside
this method.

`predict` is a method to run the prediction using your
trained model. This method depends on the task that you
are solving, please read the instruction that sent by
the Kumparan team for what is the input and the output
of the method.

In this interface, we implement `save` method to helps you
save your trained model. You may not edit this method 
directly.

You can add more initialization parameter and define
new methods to the `Model` class.


### Usage

    python model.py

It will run the training and save your trained model to
file `model.pickle`.
