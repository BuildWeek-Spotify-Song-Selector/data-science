import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from pickle import load
import keras


class Prediction_Model:

    def __init__(self):
        self.features = ["danceability",
                        "energy",
                        "key",
                        "loudness",
                        "mode",
                        "speechiness",
                        "acousticness",
                        "instrumentalness",
                        "liveness",
                        "valence",
                        "tempo",
                        "duration_ms",
                        "time_signature"]

        self.load()



    def load(self):
        self.scaler = load(open('app/services/model_data/scaler.pkl', 'rb'))
        self.encoder = load_model('app/services/model_data/encoder.h5')
        print("model loaded..")


    def predict(self, song_data):
        x_data = self.organize_song_data(song_data)
        print(x_data)
        print(f"Scaler: {self.scaler}")
        x_train = self.scaler.transform(x_data)
        preds = self.encoder.predict(x_train)

        return preds


    def organize_song_data(self, song_data):
        x_data = []

        for feature in self.features:
            x_data.append(song_data[feature])

        # return np.atleast_2d(x_data)
        return [x_data]


model = Prediction_Model()


if __name__ == "__main__":
    data = np.atleast_2d([ 4.56000e-01,  2.55000e-01,  9.00000e+00, -1.58050e+01, 1.00000e+00,  4.80000e-02,  9.46000e-01,  1.70000e-01, 9.51000e-01,  5.32000e-02,  1.16424e+02,  2.53067e+05,4.00000e+00])
    print(data.shape)
    scaler = load(open('model_data/scaler.pkl', 'rb'))
    scaler.transform(data)
