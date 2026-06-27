import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylistCreator:
    def __init__(self, client_id, client_secret, redirect_uri, username):
        """
        Constructor: Initializes the credentials and logs into Spotify.
        """
        self.client_id = ""
        self.client_secret = ""
        self.redirect_uri = ""
        self.username = "Fazah Qamar"
        self.scope = "playlist-modify-public"

        # This automatically logs us in when the class object is created
        self.sp = self._authenticate()

    def _authenticate(self):
        """
        Internal helper method to handle the Spotify security handshake.
        """
        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
            username=self.username
        ))

    def extract_songs_from_file(self, file_path):
        """
        Reads a local text file and extracts song names into a clean list.
        """
        song_list = []
        print(f"📂 Reading songs from {file_path}...")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    cleaned_song = line.strip()
                    if cleaned_song:
                        song_list.append(cleaned_song)
            print(f"✅ Successfully extracted {len(song_list)} songs.")
            return song_list
        except FileNotFoundError:
            print(f"❌ Error: The file '{file_path}' was not found.")
            return []

    def get_track_uris(self, song_list):
        """
        Loops through text names and converts them into Spotify tracking URIs.
        """
        track_uris = []
        print("🔍 Searching for tracks on Spotify...")

        for song in song_list:
            result = self.sp.search(q=song, type='track', limit=1)
            try:
                track_uri = result['tracks']['items'][0]['uri']
                track_uris.append(track_uri)
            except IndexError:
                print(f"⚠️ Could not find '{song}' on Spotify. Skipping.")

        return track_uris

    def create_playlist_from_file(self, file_path, playlist_name):
        """
        The main orchestrator method that connects all the steps together.
        """
        # Step 1: Get the songs from your file
        songs = self.extract_songs_from_file(file_path)
        if not songs:
            return

        # Step 2: Convert names to Spotify IDs
        uris = self.get_track_uris(songs)
        if not uris:
            print("❌ No valid tracks found on Spotify. Playlist creation aborted.")
            return

        # Step 3: Create the empty playlist on Spotify
        print(f"🔨 Creating playlist: '{playlist_name}'...")
        user_playlist = self.sp.user_playlist_create(
            user=self.username,
            name=playlist_name,
            public=True
        )
        playlist_id = user_playlist['id']

        # Step 4: Dump all the IDs into the playlist
        self.sp.playlist_add_items(playlist_id=playlist_id, items=uris)
        print(f"🎉 Success! '{playlist_name}' is ready on your Spotify account.")

