import pandas

df = pandas.read_csv("tracks.csv", sep="*")

print(df.shape)

print(len(df['track_id'].unique()))

# df.drop_duplicates(subset="track_id", inplace=True)
#
# print(df.shape)
