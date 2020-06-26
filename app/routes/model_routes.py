
from flask import Blueprint, request, jsonify
from app.services import spotipy_service
from app.services.model import Prediction_Model, model
from app.services.database import Song_Database
from app.log.log_error import log_error
import json
import pandas as pd
import numpy as np


model_routes = Blueprint("model_routes", __name__)




@model_routes.route('/model/pred', methods=["GET"])
def song_info():

    try:
        song_id = request.args.get('song_id')
        user_playlist = request.args.get("user_playlist")
        num_songs = int(request.args.get("num_songs"))
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
        'track' : meta['name'],
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
            tracks = find_nearest_neighbors(track, prediction, user_playlist, num_songs)

        else:
            if 'prediction' in lookup_track.keys():
                prediction = lookup_track['prediction']
            else:
                prediction = call_model(track)
                db.add_prediction(lookup_track, prediction[0])

            tracks = find_nearest_neighbors(lookup_track, prediction, user_playlist, num_songs)
            tracks = [x for x in tracks]


        return str(tracks)

    except Exception as e:
        log_error(e)
        return "Error with request.."

  # this method calls the saved ML model based
  # and receives a pandas dataframe with the predictions
def call_model(track):
    # call saved model snd get predictions
    track_prediction = model.predict(track)

    return track_prediction



def find_nearest_neighbors(track, prediction, user_playlist, num_songs):
    db = Song_Database()

    print("playlist")
    if user_playlist:
        user_song_ids = [x["songid"] for x in user_playlist] + track["songid"]
    else:
        user_song_ids = track["songid"]

    print("tracks")
    search_tracks = db.get_predictions()
    return_tracks = {}

    print("searching")
    for x in search_tracks:
        try:
            if x['songid'] in user_song_ids:
                continue
            song_vector = np.asarray(x['prediction']).astype(int)
            idx = sum(np.abs(song_vector - prediction))

            if len(return_tracks.keys())<=num_songs:
                return_tracks[idx] = x

            else:
                minimum = min(return_tracks.keys())

                if minimum>idx:
                    del return_tracks[minimum]
                    return_tracks[idx] = x

        except Exception as e:
            print(f"Error: {e}")


    return return_tracks.values()






if __name__ == "__main__":
    pass
