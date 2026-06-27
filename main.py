from getting_song import GettingSong
from spotify_playlist_make import SpotifyPlaylistCreator

def main():
    # 1. Scrape the Billboard data and save it to the text file
    song_scraper = GettingSong()
    song_scraper.scrapping_data()

    # 2. Setup your Spotify Credentials
    CONFIG = {
        "client_id": "YOUR_CLIENT_ID",
        "client_secret": "YOUR_CLIENT_SECRET",
        "redirect_uri": "http://127.0.0.1:8888/callback",  # Updated to loopback IP as requested by Spotify
        "username": "YOUR_SPOTIFY_USERNAME"
    }

    # 3. Instantiate the Class (Create the engine object)
    creator = SpotifyPlaylistCreator(**CONFIG)

    # 4. Run the complete process with one single command!
    creator.create_playlist_from_file(
        file_path="song_names.txt",
        playlist_name="My OOP Generated Playlist"
    )

if __name__ == "__main__":
    main()