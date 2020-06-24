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


def get_model_prediction(track_id):
    params = {"track_id" : track_id}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/model/pred", params=params, headers=headers)

    pprint(response.text)



if __name__ == "__main__":
    #get_track("Walking On the Sun")
    #get_audio_features("2MLHyLy5z5l5YRp7momlgw")
    #get_model_prediction("2MLHyLy5z5l5YRp7momlgw")
    get_model_prediction("2MLHyLyp7momlgw")
    # print(1+2)
