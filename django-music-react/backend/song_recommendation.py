import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import spotipy
from spotipy import SpotifyClientCredentials
import youtube_dl

##values found from kaggle spotify 175k row dataset used to normalize values
tempo_max = 243.07
duration_ms_max = 5338302
key_max = 11
loudness_max = 3.855
loudness_min = -60

##Spotify API Credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="b8f8407e9b10446b82f00dfc1c71c60b",
                                                            client_secret="973ca784cdd34701af4c2e0ca3b82b76"))

ydl = youtube_dl.YoutubeDL({})

def get_spotify_id(title, artist):
    ##Obtain spotify_ID from title and artist of a song
    track_id = sp.search(q='artist:' +artist + ' track:' + title, type='track')
    return track_id['tracks']['items'][0]['id']

def get_song_vector(spotify_ID):
    ##Getting Song features for one song 
    data = sp.audio_features(tracks = [spotify_ID])

    ##Converting features into dataframe
    data_spotify_dict_df = pd.DataFrame(data)

    ##Picking only columns needed
    data_spotify_dict_df = data_spotify_dict_df[['acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence']]

    ##Normalizing column values as needed between (0-1)
    data_spotify_dict_df["tempo"] = data_spotify_dict_df["tempo"]/tempo_max
    data_spotify_dict_df["duration_ms"] = data_spotify_dict_df["duration_ms"]/duration_ms_max
    data_spotify_dict_df["key"] = data_spotify_dict_df["key"]/key_max
    data_spotify_dict_df["loudness"] = (data_spotify_dict_df["loudness"]-loudness_max)/loudness_min

    return data_spotify_dict_df
	
	
def generateInitialReccomendationDataset(Spotify_ID):
    ##Access 100 top songs that spotify reccomends for particular track and augment them with audio features
    reccomended_track_info=sp.recommendations(seed_tracks=[Spotify_ID],limit=100)['tracks']
    reccomended_track_info_df = pd.DataFrame(reccomended_track_info)
    features = []
    for id in reccomended_track_info_df['id']:
        features.append(get_song_vector(id).iloc[0])
    feature_df = pd.DataFrame(features)
    feature_df['name'] = list(reccomended_track_info_df['name'])
    feature_df['album'] = [x['name'] for x in reccomended_track_info_df['album']]
    feature_df['artists'] = [x[0]['name'] for x in reccomended_track_info_df['artists']]
    feature_df['id'] = list(reccomended_track_info_df['id'])
    feature_df['external_url'] = [x['spotify'] for x in reccomended_track_info_df['external_urls']]
    feature_df['preview_url'] = list(reccomended_track_info_df['preview_url'])
    feature_df['popularity'] = list(reccomended_track_info_df['popularity'])
    feature_df = feature_df[['name','album','artists','id','external_url','preview_url','popularity','acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence']]
    feature_df = feature_df.reset_index(drop = True)
    return feature_df

def top_n_similar_songs(song_vector, song_database, num_songs=10):
    """Run Cosine Similarity Metric with song_vector and your database to find the top 10 out of 100 most similar songs based on these 
    audio features: 'acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence'"""
    song_database["distances"] = cosine_similarity(song_database.iloc[:,7:], song_vector)
    list_of_indexes = list(song_database["distances"].nlargest(num_songs).index)
    top_n_similar_songs = song_database.iloc[list_of_indexes, :]    
    return top_n_similar_songs

def getReccomendedSongs(youtube_link):
    with ydl:
        video = ydl.extract_info(youtube_link, download=False)
    id = get_spotify_id(video['track'],video['artist'])
    song_vector = get_song_vector(id)
    song_database = generateInitialReccomendationDataset(id)
    top_n = top_n_similar_songs(song_vector,song_database)
    top_n_dropped = top_n.drop(["id","popularity", 'acousticness','danceability','duration_ms','energy','instrumentalness','key','liveness','loudness','speechiness','tempo','valence','distances'], axis = 1)
    return top_n_dropped

def __main__():
    print(getReccomendedSongs("https://www.youtube.com/watch?v=XXYlFuWEuKI&ab_channel=TheWeekndVEVO"));

if __name__ == "__main__":
    __main__()