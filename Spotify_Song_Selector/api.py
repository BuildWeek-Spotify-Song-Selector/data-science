
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
    for genre in sp.recommendation_genre_seeds()['genres']:
        results = sp.search(q=genre, limit=50)

        for result in results['tracks']['items']:
            try:
                uri = result['uri']
                artist = result['artists'][0]['name']
                track = result['name']

                pprint({"Artist": artist, "Track":track})
                song_features = sp.audio_features(uri)

                # write to csv

                line = artist + "," + track + "," + genre + ","
                for x in song_features[0].values():
                    line += str(x) + ","
                line+="\n"

                # print(line)
                f.write(line)

            except:
                continue

    f.close()
        # pprint(song_features)
        # print("\n")

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
