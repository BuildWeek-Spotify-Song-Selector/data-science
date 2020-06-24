
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
import os
# from dotenv import load_dotenv
from pprint import pprint


# load_dotenv()

#
# util.prompt_for_user_token("bi423x859c25z4xnvy06kquj4",
#                            "user-library-read",
#                            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
#                            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
#                            redirect_uri='http://localhost')


client_id = '9a4e32732c6045289b1d85705c247a0f'
client_secret = '0ec437eade2b42ef878ea7009de904ef'


def spotipy_api():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    return sp




if __name__ == "__main__":

    # generate_track_csv()
    # sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    sp = spotipy_api()
    # pprint(sp.recommendation_genre_seeds())

    # result = sp.search(q="Walking On The Sun")
    # print(result)

    urn = 'spotify:track:2MLHyLy5z5l5YRp7momlgw'
    track = sp.track(urn)
    pprint(track)


    # seed_artists = ['3jOstUTkEu2JkjvRdBA5Gu']
    # seed_genres = ['rock']
    # for i in range(1):
    #     result = sp.recommendations(seed_artists=seed_artists, seed_genres=['rock'], seed_tracks=['2MLHyLy5z5l5YRp7momlgw'])
    #     pprint(result)
    #     for t in result['tracks']:
    #         pprint(t['artists'][0]['name'])
    #         pprint(t['id'])


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
