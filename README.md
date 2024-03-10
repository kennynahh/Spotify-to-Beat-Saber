# Spotify to Beat Saber
Download your Spotify liked songs directly into Beat Saber!

This was built so I could get as many of my 2500+ Spotify liked songs into Beat Saber. I was sick of searching for individual songs.

## Configuration

Before running the script, you need to set up your Spotify API credentials. Follow these steps:

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to create an app.
2. Open `config.ini` and replace `your_client_id_here`, `your_client_secret_here`, and `your_redirect_uri_here` with your Spotify application's credentials.
3. It is reccommended you set `your_redirect_uri_here` as "http://localhost:8888/callback" (in both config.ini and in the Spotify Developer Dashboard for your app.)

You may also need to install the following packages:

`pip3 install spotipy`

## Using the script

run `script.py` first, wait for the .csv file to be generated (may take a while depending on the size of your library), and then run `beatsaver.py`. This will leave you with a folder of custom songs that match the names of your liked songs, which you can then move into wherever your Beat Saber custom songs folder is.

## Things to know

There are just too many random songs out there mapped in Beat Saver with similar (or identical) names to popular songs. This means that a percentage of the downloaded songs will not be what you wanted. To delete songs quickly and easily while in-game, I suggest using the SongBrowser mod. Maybe I'll add additional song-checking methods in the future, but I am by no means a good programmer, so this is what I've got for ya.

You may also run into API rate limitations if your library is exceptionally large.