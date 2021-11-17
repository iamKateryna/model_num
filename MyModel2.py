import tensorflow as tf
PATH = 'TF_MODEL_2'

class MyModel2(object):
    def __init__(self):
        self.model = tf.keras.models.load_model(PATH)

    def predict(self, X):
        classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        Y = self.model.predict(X)
        Y = Y[0]*100
        probs = {classes[i]: Y[i] for i in range(len(classes))}
        return probs