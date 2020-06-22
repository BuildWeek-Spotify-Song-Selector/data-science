
from flask import Blueprint, request

model_routes = Blueprint("model_routes", __name__)



@model_routes.route("/model/predict", methods=["POST"])
def predict():

    track_id = request.args.get("track_id")

    if not track_id:
        return "track_id not provided"

    ### TODO:
    # call model and get predicted song track id to return

    # predicted_track_id = model.predict(track_id)

    # return json.dumps({"track_id" : predicted_track_id})

    return "in development.."
