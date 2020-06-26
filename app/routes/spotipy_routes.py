
from flask import Blueprint, request
from app.services import spotipy_service
from app.log.log_error import log_error
import json

spotipy_routes = Blueprint("spotipy_routes", __name__)



@spotipy_routes.route("/spotipy/get_track_data", methods=["GET"])
def get_track_data():

    try:
        song_id = request.args.get("track_id")

        track = sp.track(track_id)
        features = sp.audio_features(tracks=[track_id])

        print("features: {features}")

        track = {
        'song_id' : track[0]['track_id'],
        'artist' : track[0]['artist'],
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
        'time_signature': features[0]['time_signature']
        }

    except Exception as e:
        log_error(e)
        return "Error with request.."


    return json.dumps(track)



@spotipy_routes.route("/spotipy/get_track", methods=["GET"])
def get_track():

    track = request.args.get("track")

    if not track:
        return "track not provided"

    try:
        sp = spotipy_service.spotipy_api()
        result = sp.search(q=track)
        print(type(result))
        return json.dumps(result)

    except Exception as e:
        log_error(e)
        return "Error with search\n" + str(e)



@spotipy_routes.route("/spotipy/get_audio_features", methods=["GET"])
def get_audio_features():

    song_id = request.args.get("song_id")

    if not song_id:
        return "song_id(s) not provided"

    try:
        sp = spotipy_service.spotipy_api()

        if type(song_id) == list:
            result = sp.audio_features(tracks=song_id)
        else:
            result = sp.audio_features(tracks=[song_id])

        return json.dumps(result)

    except Exception as e:
        log_error(e)
        return "Error with search\n" + str(e)
