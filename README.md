# Spotify to Beat Saber
Download your Spotify liked songs directly into Beat Saber!

I built this just so that I could get as many of my 2500+ Spotify liked songs into Beat Saber, as I was sick of searching for individual songs.

## Configuration

Before running the script, you need to set up your Spotify API credentials. Follow these steps:

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to create an app.
2. Open `config.ini` and replace `your_client_id_here`, `your_client_secret_here`, and `your_redirect_uri_here` with your Spotify application's credentials.
3. It is reccommended you set `your_redirect_uri_here` as "http://localhost:8888/callback" (in both config.ini and in the Spotify Developer Dashboard for your app.)

You may also need to install the following packages:

`pip3 install spotipy`