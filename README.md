# data-science
data science repo for spotify song selector



# routes

"/" : "server running"

"/about" : returns json basic route info

"/database/get_all_songs" : returns json of all song data in song_list5
                            [{"songid":"5X4Qm0rVLcZeeO4tSDmBg3",
                            "artist":"Jack Bruce",
                            "track":"Running Thro' Our Hands",
                            "danceability":0.456,
                            "energy":0.255,
                            "key":9.0,
                            "loudness":-15.805,
                            "mode":1.0,
                            "speechiness":0.048,
                            "acousticness":0.946,
                            "instrumentalness":0.17,
                            "liveness":0.951,
                            "valence":0.0532,
                            "tempo":116.424,
                            "duration_ms":253067.0,
                            "time_signature":4.0}]

"/database/generate_track_csv" : generate song data into tracks.csv

"/model/predict" : call model for prediction of next song

"/spotipy/get_track" : "get spotipy track data"
                        -- params = {"track": track name/song title  ex. "Never Gonna Give You Up"}

"/spotipy/get_audio_features" : "audio features for list or single song_id"
                                --params = {"song_id":"1vWWohf17o0bf8mcXXwuM1"}
                                        or {"song_id":["1vWWohf17o0bf8mcXXwuM1", "05JGVUwt7XJk5FPqH0Wsch"]}
