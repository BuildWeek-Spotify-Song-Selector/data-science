

import pymongo
import pandas as pd
import json
from app.services.model import Prediction_Model, model

class Song_Database:

    def __init__(self):
        self.connection = "mongodb+srv://joe_maulin:pQK3om3P5I3XxjyJ@cluster0-zjx5c.mongodb.net/<dbname>?retryWrites=true&w=majority"
        self.create_database()

    def create_database(self):
        self.client = pymongo.MongoClient(self.connection)
        self.database = self.client.song_database
        collections = self.database.list_collection_names()

        if "songs" not in collections:
            self.collection = self.database.songs
            self.collection.insert_one({"_id":"init" ,"songid":"placeholder"})

        else:
            self.collection = self.database.songs

    def get_track(self, songid):

        track = self.collection.find_one({"songid" : songid})
        if track:
            return track

    def get_tracks(self, songids):

        tracks = []

        for id in songids:
            track = self.get_track(id)
            tracks.append(track)

        return tracks


    def add_track(self, track):

        self.collection.insert_one(track)


    def update_track(self, track):

        self.collection.replace_one({"songid": track['songid']}, track, upsert=True)


    def get_predictions(self):

        tracks = self.collection.find({"prediction": {"$exists" : True}})
        return tracks


    def add_prediction(self, track, prediction):

        self.collection.update_one({"songid": track['songid']}, {"$set": {"prediction":prediction}})


    def import_song_data(self):

        df = pd.read_csv("app/services/song_lists/song_list5.csv", sep=",")
        records = json.loads(df.to_json(orient="records"))
        self.collection.insert_many(records)

        self.set_initial_predictions()

    def set_initial_predictions(self):

        tracks = self.collection.find({"prediction": {"$exists" : False}})

        i = 0
        for x in tracks:
            try:
                print(i, "predicted..")
                prediction = model.predict(x)

                self.add_prediction(x, [float(prediction[0][0]),float(prediction[0][1])])

            except:
                continue
            i+=1



if __name__ == "__main__":
    import pandas as pd
    import json

    # db = Song_Database()
    # search_tracks = json.dumps(list(db.get_predictions()))
    #
    # df = pd.read_json(search_tracks)
    #
    # print(df.head())

    song_database = Song_Database()
    # #
    # # song_database.set_initial_predictions()
    #
    #
    # for x in song_database.get_predictions():
    #     print(x)


    track = song_database.get_track("2MLHyLy5z5l5YRp7momlgw")
    print(f"track: {track}")
    # track['prediction'] = [2,32]
    #
    # song_database.add_prediction(track, [.4,.1])
    # # song_database.update_track(track)
    #
    # track = song_database.get_track("6t9dKp7Nf1t4HpYXOdeVNl")
    # print(track)


    # features = ['songid','artist','track','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms','time_signature']
    # data = ['5X4Qm0rVLcZeeO4tSDmBg3','Jack Bruce',"Running Thro' Our Hands",0.456,0.255,9.0,-15.805,1.0,0.048,0.946,0.17,0.951,0.0532,116.424,253067.0,4.0]
    #
    # track = {}
    # for i in range(len(features)):
    #     track[features[i]] = data[i]
    #
    # print(f"track:{track}")
    #
    # song_database.add_track(track)

    # query = song_database.collection.find({"songid":"5X4Qm0rVLcZeeO4tSDmBg3"})
    # for x in query:
    #     print(x)

    # print(song_database.database.list_collection_names())
    # print(song_database.client.list_database_names())
    # print(song_database.client.list_collection_names())

    # song_database.import_song_data()
