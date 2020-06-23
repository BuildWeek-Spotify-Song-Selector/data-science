# import pandas
#
# df = pandas.read_csv("song_list5.csv", sep=",")
#
#
# print(df.head())


import requests

http = "http://localhost:5000"


def get_track(track):

    params = {"track" : track}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/spotipy/get_track", params=params, headers=headers)

    print(response.text)


def get_audio_features(song_id):
    params = {"song_id" : song_id}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/spotipy/get_audio_features", params=params, headers=headers)

    print(response.text)



if __name__ == "__main__":
    #get_track("Walking On the Sun")
    get_audio_features("2MLHyLy5z5l5YRp7momlgw")
