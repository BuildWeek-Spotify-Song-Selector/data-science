
import spotipy
import time
import json
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from pickle import load
import tensorflow as tf
from tensorflow import keras
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, redirect, request, session, make_response,session,redirect


app = Flask(__name__)

SPOT_CLIENT_ID = "417789dcea984a95a3d5f4b325787e46"
SPOT_CLIENT_SECRET = "c9a76a25685b4899ae1964898df71dab"

# this is the default route to load the application
@app.route('/')
def index(): 
      return 'This is my backend'

# This route accepts a track id parammter in the path
# and calls spotify to rettive track information and metadata
# This information will be passed to the saved ML model
@app.route('/track/<track_id>', methods = ["GET","POST"])
def song_info(track_id):
    #track_id = request.args['track_id']
    print('-------------trackid--------------------')
    client_id = SPOT_CLIENT_ID
    client_secret = SPOT_CLIENT_SECRET
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# spotify object to access API
    sp = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)
    #meta = sp.track(track_id)
    features = sp.audio_features(tracks=[track_id])
    
    
    #'name' : meta['name'],
    #'album' : meta['album']['name'],
    #'artist' : meta['album']['artists'][0]['name'],
    #'release_date' : meta['album']['release_date'],
    track = {
    #'popularity' : features[0]['popularity'],
    'duration_ms': features[0]['duration_ms'],
    'key': features[0]['key'],
    'mode': features[0]['mode'],
    'valence': features[0]['valence'],
    'acousticness' : features[0]['acousticness'],
    'danceability' : features[0]['danceability'],
    'energy' : features[0]['energy'],
    'instrumentalness' : features[0]['instrumentalness'],
    'liveness' : features[0]['liveness'],
    'loudness' : features[0]['loudness'],
    'speechiness':features[0]['speechiness'],
    'tempo' : features[0]['tempo'],
    'time_signature': features[0]['time_signature']
    }
    return call_model(track)
    #track = ['mode','key','duration_ms','valence', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature']
    #print (track)
    #return track

  #this method calls the saved ML model based 
  #and receives a pandas dataframe with the predictions
def call_model(track): 
    scaler = load(open('scaler.pkl', 'rb'))
    df = pd.DataFrame(track,index=[0])
    print(df)
    #df['DataFrame Column'] = df['DataFrame Column'].astype(float)
    out_arr = np.atleast_2d(df.values)
    x_train = scaler.transform(out_arr)
    #x_train = scaler.transform(df.values)
    print(x_train)

    # temp = tempfile.TemporaryFile()
    # with open('encoder.h5'. mode='rb') as f:
    #    h5 = decrypt_func(f.read())
    #    temp.write(h5)
    # with h5py.File(temp, 'r') as h5file:
    #    model = load_model(h5file)





    
    encoder = load_model('encoder.h5')
    #encoder = keras.models.load_model('encoder.h5')
    #encoder = tf.keras.models.load_model('encoder.h5')
    print("loaded model")

    #preds = encoder.predict(x_train)
    preds = encoder.predict(x_train)
    print(preds)
    
    #call saved model snd get predictions
    output = df.to_json(preds)[1:-1].replace('},{', '} {')
    #output = df.to_json(preds)
    return output



#Setting the env in windows  
#$env:FLASK_APP = "routes.py"
#flask db upgrade
#track_id used to check the routes-  
#7AiMnJSODcJoKDejQ3mnoJ
#26VFTg2z8YR0cCuwLzESi2