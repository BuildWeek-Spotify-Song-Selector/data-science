import pandas as pd
import numpy as np
from pickle import load
from keras.models import load_model



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
        # print(f"Scaler: {self.scaler}")

        x_train = self.scaler.transform(x_data)
        preds = self.encoder.predict(x_train)

        return preds[0].tolist()


    def organize_song_data(self, song_data):
        x_data = []

        for feature in self.features:
            x_data.append(song_data[feature])

        # return np.atleast_2d(x_data)
        return [x_data]


global model

model = Prediction_Model()


if __name__ == "__main__":
    data = {'danceability': 0.731, 'energy': 0.867, 'key': 11, 'loudness': -5.881, 'mode': 1, 'speechiness': 0.032, 'acousticness': 0.0395, 'instrumentalness': 0, 'liveness': 0.0861, 'valence': 0.776, 'tempo': 104.019, 'duration_ms': 200373, 'time_signature': 4, 'song_id': '3cfOd4CMv2snFaKAnMdnvK', 'track': 'All Star', 'artist': 'Smash Mouth'}
    preds = model.predict(data)

    print(preds)
