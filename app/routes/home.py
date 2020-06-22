

from flask import Blueprint
import json

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def home():
    return "Server running.."


@home_routes.route("/about")
def about():

    functions = {"/" : "server running",
                 "/about" : "route info",
                 "/database/get_all_songs" : "get json of song data",
                 "/database/generate_track_csv" : "generate song data",
                 "/model/predict" : "call model for prediction",
                 "/spotipy/get_track" : "get spotipy track data",
                 "/spotipy/get_audio_features" : "audio features for list or single track_id"
                 }

    return json.dumps(functions)
