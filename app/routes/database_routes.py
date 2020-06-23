

from flask import Blueprint
import pandas as pd


database_routes = Blueprint("database_routes", __name__)






@database_routes.route("/database/get_all_songs", methods=["GET"])
def get_all_songs():
    df = pd.read_csv("app/song_list5.csv", sep=",")

    print(df.shape)

    input("Enter to get data: ")

    return df.to_json(orient='records')


@database_routes.route("/database/generate_track_csv")
def generate_track_csv():
    return "in development.."

    ### # TODO:
    # Need to rewrite to read from song list
        # call spotify/get_track
            # track_name file open song list
            # params = {"track_name" : track_name}
            # headers = {"content-type" : "application/json"}
            # response = requests.get(http + "/spotipy/get_track", params=params, headers=headers)
            # song_id = response['tracks']['items']['id']
        # call spotify/get_audio_features
            # headers = {"content-type" : "application/json"}
            # response = requests.get(http + "/spotipy/get_audio_features", params={"song_id":song_id}, headers=headers)
            # append tracks.csv

    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


    f = open("../tracks.csv", "a")
    headers = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness',\
                'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']

    header_line = "track_id" + "*" + "artist" + "*" + "track" + "*" + "genre" + "*" + "popularity" + "*" + "explicit" + "*" + "release_date"
    for x in headers:
        header_line += "*" + x
    header_line += "\n"

    f.write(header_line)

    genre_goal = 50000
    for genre in sp.recommendation_genre_seeds()['genres']:
        track_total = 0

        while track_total < genre_goal:
            results = sp.search(q=genre, limit=50)
            track_total+=50
            print(track_total)

            for result in results['tracks']['items']:

                try:
                    uri = result['uri']
                    artist = result['artists'][0]['name']
                    track = result['name']
                    track_id = result['id']
                    popularity = result['popularity']
                    explicit = result['explicit']
                    release_date = result['album']['release_date']

                    pprint({"Artist": artist, "Track":track})
                    song_features = sp.audio_features(uri)

                    # write to csv

                    line = str(track_id) + "*" + artist + "*" + track + "*" + genre + "*" + str(popularity) + "*" + str(explicit) + "*" + str(release_date)
                    for x in headers:
                        line += "*" + str(song_features[0][x])
                    line+="\n"

                    f.write(line)

                except Exception as e:
                    print(e)
                    continue


    f.close()
