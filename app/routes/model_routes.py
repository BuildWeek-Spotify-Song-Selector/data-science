
from flask import Blueprint, request
from app.services import spotipy_service
from app.services.model import Prediction_Model, model
from app.services.database import Song_Database
from app.log.log_error import log_error
import json


model_routes = Blueprint("model_routes", __name__)




@model_routes.route('/model/pred', methods=["GET"])
def song_info():

    try:
        song_id = request.args.get('song_id')
        print('-------------trackid--------------------')

        # spotify object to access API
        sp = spotipy_service.spotipy_api()
        meta = sp.track(song_id)
        features = sp.audio_features(tracks=[song_id])

        print("features: {features}")

        track = {
        'danceability' : features[0]['danceability'],
        'energy' : features[0]['energy'],
        'key' : features[0]['key'],
        'loudness' : features[0]['loudness'],
        'mode' : features[0]['mode'],
        'speechiness':features[0]['speechiness'],
        'acousticness' : features[0]['acousticness'],
        'instrumentalness' : features[0]['instrumentalness'],
        'liveness' : features[0]['liveness'],
        'valence' : features[0]['valence'],
        'tempo' : features[0]['tempo'],
        'duration_ms' : features[0]['duration_ms'],
        'time_signature': features[0]['time_signature'],
        'song_id' : song_id,
        'track' : meta['name'],,
        'artist' : meta['artists'][0]['name']
        }

        # get song database
        db = Song_Database()

        # look up if song apperars in database
        lookup_track = db.get_track(song_id)

        # add song if not in database
        if not lookup_track:
            prediction = call_model(track)
            track['prediction'] = prediction[0]
            db.add_track(track)

        else:
            if 'prediction' in lookup_track.keys():
                prediction = lookup_track['prediction']
            else:
                prediction = call_model(track)
                db.add_prediction(lookup_track, prediction[0])

        # run closest vectors function
        tracks = find_closest_neighbors(song_id, prediction)

        return json.dumps(tracks)

    except Exception as e:
        log_error(e)
        return "Error with request.."

  # this method calls the saved ML model based
  # and receives a pandas dataframe with the predictions
def call_model(track):
    # call saved model snd get predictions
    track_prediction = model.predict(track)

    return track_prediction
