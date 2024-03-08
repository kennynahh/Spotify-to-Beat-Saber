import csv
import requests
import os
import zipfile

# Function to search BeatSaver for a map given a song title and artist
def search_beatsaver(title, artist):
    query = f"{title} {artist}"
    url = f"https://api.beatsaver.com/search/text/0?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['docs']:
            return data['docs'][0]['versions'][-1]['downloadURL']
    return None

# Updated function to download and extract a map
def download_and_extract_map(url, title):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            # Generate a valid filename from the title
            safe_title = "".join(x for x in title if x.isalnum() or x in " -_").rstrip()
            zip_filename = f"{safe_title}.zip"
            directory_name = safe_title  # Folder name for the extracted content

            with open(zip_filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {zip_filename}")

            # Extract the ZIP file into a directory named after the song
            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                extract_path = os.path.join(download_dir, directory_name)
                zip_ref.extractall(extract_path)
            print(f"Extracted to: {extract_path}")

            # Optionally, delete the ZIP file after extraction
            os.remove(zip_filename)
        else:
            print("Failed to download map.")
    else:
        print("Map not found.")

# Set the script directory and CSV file path
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, 'liked_songs.csv')

# Ensure a directory exists for the downloads and change into it
download_dir = os.path.join(script_dir, 'beat_saber_maps')
os.makedirs(download_dir, exist_ok=True)

# Process each song in the CSV file
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for title, artist in reader:
        print(f"Searching for: {title} by {artist}")
        map_url = search_beatsaver(title, artist)
        if map_url:
            download_and_extract_map(map_url, title)
        else:
            print(f"No map found for: {title} by {artist}")