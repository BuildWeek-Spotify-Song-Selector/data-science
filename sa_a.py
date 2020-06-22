import os
import time
import spotipy
# To access authorised Spotify data
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

SPOT_CLIENT_ID = "417789dcea984a95a3d5f4b325787e46"
SPOT_CLIENT_SECRET = "c9a76a25685b4899ae1964898df71dab"

client_id = SPOT_CLIENT_ID
client_secret = SPOT_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# spotify object to access API
sp = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager)

#warm fuzzy playlist
#print(sp.user_playlist_tracks("spotify", "37i9dQZF1DX5IDTimEWoTd"))
playlist_creator = "spotify"
playlist_id = "37i9dQZF1DX5IDTimEWoTd"

def analyze_playlist(creator, playlist_id):
    
    # Create empty dataframe
    playlist_features_list = ["artist", "album", "track_name", "track_id",
                              "danceability", "energy", "key", "loudness", "mode",
                              "speechiness", "instrumentalness", "liveness", "valence", "tempo",
                              "duration_ms","time_signature"]
    
    playlist_df = pd.DataFrame(columns=playlist_features_list)
    

    
    # Loop through every track in the playlist, extract features and append the features to the playlist df
    
    playlist = sp.user_playlist_tracks(creator, playlist_id)["items"]
    for track in playlist:
        # Create empty dict
        playlist_features = {}
        # Get metadata
        playlist_features["artist"] = track["track"]["album"]["artists"][0]["name"]
        playlist_features["album"] = track["track"]["album"]["name"]
        playlist_features["track_name"] = track["track"]["name"]
        playlist_features["track_id"] = track["track"]["id"]
        
        # Get audio features
        audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # Concat the dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)
        
    return playlist_df   

playlist_df = analyze_playlist(playlist_creator, playlist_id)
#print(playlist_df.head())

#Analyze Multiple Playlists
playlist_dict = {
    "warm_fuzzy_feeling" : ("spotify", "37i9dQZF1DX5IDTimEWoTd"), 
    "love_songs_heart" : ("indiemono", "5KbTzqKBqxQRD8OBtJTZrS"),
    "romance_songs": ("Susan Doles", "7sAUK3XK8NHH1s5vGcTBkF"),
    "happy_songs": ("redmusiccompany", "0deORnapZgrxFY4nsKr9JA"),
    "sad_songs":("elizacat4","56adfjzaO4gkQwEIZACbX5"),
    "angry_songs": ("straga34", "2iD8Dw0rsIMpgG8Dq69RgE"),
    "love_songs":("Indiemono","5KbTzqKBqxQRD8OBtJTZrS"),
    "sad_ult_songs": ("bigdunc808", "7e1prKLGheo7IgW7GXFvrP"),
    #"sad_tenta_songs": ("Zak", "0RAPggs3kKlAI7CjoyG3hr"),
    #"angry_girl_songs":("mbellagray99", "0ZuPYh5vNNRPINIWmD5CaK"),
    

}

def analyze_playlist_dict(playlist_dict):
    
    # Loop through every playlist in the dict and analyze it
    for i, (key, val) in enumerate(playlist_dict.items()):
        playlist_df = analyze_playlist(*val)
        # Add a playlist column so that we can see which playlist a track belongs too
        playlist_df["playlist"] = key
        # Create or concat df
        if i == 0:
            playlist_dict_df = playlist_df
        else:
            playlist_dict_df = pd.concat([playlist_dict_df, playlist_df], ignore_index = True)
            
    return playlist_dict_df

multiple_playlist_df = analyze_playlist_dict(playlist_dict)


print(multiple_playlist_df["playlist"].value_counts())
multiple_playlist_df.to_csv("mood.csv", index = False)