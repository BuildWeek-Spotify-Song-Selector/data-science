
from flask import Blueprint, request
from app.services import spotipy_service

model_routes = Blueprint("model_routes", __name__)



@model_routes.route('/track/<track_id>')
def song_info(track_id):
    # track_id = request.args['track_id']
    print('-------------trackid--------------------')

    # spotify object to access API
    sp = spotipy_service.spotipy_api()
    meta = sp.track(track_id)
    features = sp.audio_features(tracks=[track_id])


    track = {
    'name' : meta['name'],
    'album' : meta['album']['name'],
    'artist' : meta['album']['artists'][0]['name'],
    'release_date' : meta['album']['release_date'],
    'length' : meta['duration_ms'],
    'popularity' : meta['popularity'],
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

    # track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

  # this method calls the saved ML model based
  # and receives a pandas dataframe with the predictions
def call_model():
    # call saved model snd get predictions
    output = df.to_json(track='tracks')[1:-1].replace('},{', '} {')
    return output
