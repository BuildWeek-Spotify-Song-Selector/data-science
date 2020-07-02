import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pandas.io.json import json_normalize
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, session, make_response,session,redirect
load_dotenv()

app = Flask(__name__)



client_id = os.getenv("SPOT_CLIENT_ID")
client_secret = os.getenv("SPOT_CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

@app.route('/')
def index():
    return 'Welcome Page!'


@app.route('/track/<track_id>', methods = ["GET","POST"])
def song_info(track_id):
    # spotify object to access API
    sp = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)
    #track_id = "7AiMnJSODcJoKDejQ3mnoJ"

    recom = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=[track_id])
    
    #print(recom.keys())
    #print(json_normalize(recom))
    json_normalize(recom['tracks'],record_path=['artists'],sep="_")
    artist_and_track = json_normalize(
                            data=recom['tracks'],
                            record_path='artists',
                            meta=['id'],
                            record_prefix='sp_artist_',
                            meta_prefix='sp_track_',
                            sep="_"
                            )
    artist_and_track = artist_and_track[['sp_track_id']]
    print(artist_and_track[['sp_track_id']])
    track = artist_and_track['sp_track_id'].to_dict()
    # features = sp.audio_features(tracks=[track])
    # track = {
    # #'popularity' : features[0]['popularity'],
    # 'duration_ms': features[0]['duration_ms'],
    # 'key': features[0]['key'],
    # 'mode': features[0]['mode'],
    # 'valence': features[0]['valence'],
    # 'acousticness' : features[0]['acousticness'],
    # 'danceability' : features[0]['danceability'],
    # 'energy' : features[0]['energy'],
    # 'instrumentalness' : features[0]['instrumentalness'],
    # 'liveness' : features[0]['liveness'],
    # 'loudness' : features[0]['loudness'],
    # 'speechiness':features[0]['speechiness'],
    # 'tempo' : features[0]['tempo'],
    # 'time_signature': features[0]['time_signature']
    # }
    
    # #track = ['mode','key','duration_ms','valence', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature']
    # #print (track)
    return track
     

#Setting the env in windows  
#$env:FLASK_APP="recommend.py"
#spot_app\recommend.py
#track_id used to check the routes-  
#7AiMnJSODcJoKDejQ3mnoJ
#26VFTg2z8YR0cCuwLzESi2