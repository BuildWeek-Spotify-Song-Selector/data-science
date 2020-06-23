import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from pickle import load
import keras



class Prediction_Model:

    def __init__(self):
        self.songs = pd.read_csv("song_lists/song_list5.csv")
        self.features = self.songs[["danceability",
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
                                    "time_signature"]].to_numpy()



    def load(self):
        scaler = load(open('model_files/scaler.pkl', 'rb'))
        x_train = scaler.transform(self.features)
        encoder = load_model('model_files/encoder.h5')
        # preds = encoder.predict(x_train)
