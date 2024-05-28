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
save your trained model, fitted preprocessor, and label encoder.
You may not edit this directly.

You can add more initialization parameter and define
new methods to the Model class.

Usage:
Install `kumparanian` first:

    pip install kumparanian

Run

    python model.py

It will run the training and save your trained model to
file `model.pickle` for scikit-learn and 'model.keras'
for TensorFlow. It will also save your fitted preprocessor
and label_encoder to file 'preprocessor_label_encoder.pickle'.
"""

from kumparanian import ds

# Import your libraries here
# Example:
# import torch


class Model:

    def __init__(self):
        """
        You can add more parameter here to initialize your model
        """
        # Instantiate preprocessor and label encoder
        self.preprocessor = "YourPreprocessorClass()"
        # Delete the string and replace YourPreprocessorClass with your
        # actual preprocessor class (tokenizer/vectorizer)
        self.label_encoder = "YourLabelEncoderClass()"
        # Delete the string and replace YourLabelEncoderClass with your
        # actual label encoder class, delete the string

        pass

    def train(self):
        """
        NOTE: Implement your training procedure in this method.
        """

        # Example:
        # data = read_dataset("file.csv")
        # preprocessed_data = self.preprocessor.fit_transform(data)
        # encoded_labels = self.label_encoder.fit_transform(labels)
        # self.model.fit(preprocessed_data, encoded_labels)
        # Replace the above lines with your actual training procedure

        raise NotImplementedError  # Delete this line

    def predict(self, input):
        """
        NOTE: Implement your predict procedure in this method.
        """

        # Example:
        # processed_input = self.preprocessor.transform(input)
        # output = self.model.predict(processed_input)
        # decoded_label = self.label_encoder.inverse_transform(output)
        # return decoded_label
        # Replace the above lines with your actual prediction procedure

        raise NotImplementedError  # Delete this line

    def save(self, model):
        """
        If it's scikit-learn model, save trained model to model.pickle file
        and if it's tensorflow model, save trained model to model.keras file
        """
        ds.model.save(
            model,
            self.preprocessor,
            self.label_encoder,
            "model.pickle",
            "preprocessor_label_encoder.pickle",
        )


if __name__ == "__main__":
    # NOTE: Edit this if you add more initialization parameter
    model = Model()

    # Train your model
    model.train()

    # Save your trained model to model.pickle
    model.save(model)
