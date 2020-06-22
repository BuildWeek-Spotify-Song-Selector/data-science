# import pandas
#
# df = pandas.read_csv("song_list5.csv", sep=",")
#
#
# print(df.head())


import requests

http = "http://localhost:5000"


def get_track(track_name):

    params = {"track_name" : track_name}
    headers = {"content-type" : "application/json"}
    response = requests.get(http + "/spotipy/get_track", params=params, headers=headers)

    print(response.text)



if __name__ == "__main__":
    get_track("Walking On the Sun")
