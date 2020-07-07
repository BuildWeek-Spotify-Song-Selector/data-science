# import pandas
#
# df = pandas.read_csv("song_list5.csv", sep=",")
#
#
# print(df.head())


import requests
from pprint import pprint
import json

http = "http://localhost:5000"


def get_track(track):

    params = {"track" : track}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/spotipy/get_track", params=params, headers=headers)

    pprint(json.loads(response.text))


def get_audio_features(song_id):
    params = {"song_id" : song_id}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/spotipy/get_audio_features", params=params, headers=headers)

    pprint(json.loads(response.text))


def get_model_prediction(song_id):
    params = {"song_id" : song_id,
              "user_playlist" : [],
              "num_songs":3}

    # song_id = request.args.get('song_id')
    # user_playlist = request.args.get("user_playlist")
    # num_songs = request.args.get("num_songs")

    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/model/pred", params=params, headers=headers)

    # pprint(json.loads(response.text))
    pprint(response.text)



if __name__ == "__main__":
    # get_track("3cfOd4CMv2snFaKAnMdnvK")
    # get_track("2MLHyLy5z5l5YRp7momlgw")
    # get_audio_features("3cfOd4CMv2snFaKAnMdnvK")
    # data = ["2MLHyLy5z5l5YRp7momlgw"] * 50
    #
    # for x in data:
    #     get_model_prediction(x)
    get_model_prediction("3cfOd4CMv2snFaKAnMdnvK")
    # 'prediction': [4.786012649536133, 7.772339344024658]
