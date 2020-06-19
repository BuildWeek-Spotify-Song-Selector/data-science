
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
from pprint import pprint


load_dotenv()

#
# util.prompt_for_user_token("bi423x859c25z4xnvy06kquj4",
#                            "user-library-read",
#                            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
#                            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
#                            redirect_uri='http://localhost')


os.environ["SPOTIPY_CLIENT_ID"] = os.getenv("SPOTIFY_CLIENT_ID")
os.environ["SPOTIPY_CLIENT_SECRET"] = os.getenv("SPOTIFY_CLIENT_SECRET")


def generate_track_csv():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


    f = open("tracks.csv", "a")
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



if __name__ == "__main__":

    # generate_track_csv()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    # pprint(sp.recommendation_genre_seeds())

    urn = 'spotify:track:2MLHyLy5z5l5YRp7momlgw'
    track = sp.track(urn)
    # pprint(track)


    seed_artists = ['3jOstUTkEu2JkjvRdBA5Gu']
    seed_genres = ['rock']
    for i in range(1):
        result = sp.recommendations(seed_artists=, seed_genres=['rock'], seed_tracks=['2MLHyLy5z5l5YRp7momlgw'])
        pprint(result)
        for t in result['tracks']:
            pprint(t['artists'][0]['name'])
            pprint(t['id'])


    # dict_keys(['meta', 'track', 'bars', 'beats', 'sections', 'segments', 'tatums'])
    # urn = 'spotify:track:2MLHyLy5z5l5YRp7momlgw'
    # track = sp.audio_analysis(urn)
    # pprint(track)
    # pprint(track['meta'])

    # song_features = sp.audio_features(urn)
    # pprint(song_features)
    #
    #
    # # get genres
    # pprint(sp.recommendation_genre_seeds())
