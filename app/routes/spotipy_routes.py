
from flask import Blueprint, request
from app.services import spotipy_service

spotipy_routes = Blueprint("spotipy_routes", __name__)


@spotipy_routes.route("/spotipy/get_track", methods=["GET"])
def get_track():

    track = request.args.get("track")

    if not track:
        return "track not provided"

    try:
        sp = spotipy_service.spotipy_api()
        result = sp.search(q=track)
        return json.dumps(result)

    except e as Exception:
        print(e)
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

    except e as Exception:
        print(e)
        return "Error with search\n" + str(e)
