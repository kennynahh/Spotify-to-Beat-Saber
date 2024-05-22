import configparser
import csv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def fetch_liked_songs():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # spotify credientials must be set up
    client_id = config['SPOTIFY']['CLIENT_ID']
    client_secret = config['SPOTIFY']['CLIENT_SECRET']
    redirect_uri = config['SPOTIFY']['REDIRECT_URI']

    # read access to user's liked songs
    scope = 'user-library-read'

    # auth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope=scope))

    # fetching liked songs
    liked_songs = []
    results = sp.current_user_saved_tracks()
    while results:
        for item in results['items']:
            track = item['track']
            liked_songs.append({'title': track['name'], 'artist': track['artists'][0]['name']})
        if results['next']:
            results = sp.next(results)
        else:
            results = None
    
    return liked_songs

def save_songs_to_csv(liked_songs):
    with open('liked_songs.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Artist'])
        for song in liked_songs:
            writer.writerow([song['title'], song['artist']])

if __name__ == '__main__':
    liked_songs = fetch_liked_songs()
    if liked_songs:
        save_songs_to_csv(liked_songs)
    else:
        print("No liked songs found.")
