"""
Kumparan's Model Interface

This is an interface file to implement your model.

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
save your trained model. You may not edit this directly.


Usage:

    python model.py

It will run the training and save your trained model to
file `model.pickle`.
"""

import pickle

# Import your libraries here
# Example:
# import torch


class Model:

    def __init__(self):
        """
        You can add more parameter here to initialize your model
        """
        pass

    def train(self):
        """
        NOTE: Implement your training procedure in this method.
        """

        # Delete this line
        raise NotImplementedError

    def predict(self, input):
        """
        NOTE: Implement your predict procedure in this method.
        """

        # Delete this line
        raise NotImplementedError

    def save(self):
        """
        Save trained model to model.pickle file.
        """
        with open("model.pickle", "wb") as f:
            pickle.dump(self, f)


if __name__ == '__main__':
    # NOTE: Edit this if you add more initialization parameter
    model = Model()

    # Train your model
    model.train()

    # Save your trained model to model.pickle
    model.save()
