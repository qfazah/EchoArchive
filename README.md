# EchoArchive 🎧

EchoArchive is a Python-based automation tool that acts as a musical time machine. Give it a year, and it will scrape Wikipedia to find the top 100 songs of that specific year, search for them on Spotify, and automatically generate a custom playlist directly in your Spotify account.

## ✨ Features
* **Historical Web Scraping:** Extracts accurate data from Wikipedia's "Billboard Year-End Hot 100 singles" or equivalent lists for any given year.
* **Automated Playlist Creation:** Seamlessly connects to your Spotify account using OAuth authentication.
* **Smart Matching:** Searches for tracks by combining both artist name and song title to ensure the most accurate matches.

## 🛠️ Built With
* **Python 3**
* **BeautifulSoup4 & Requests:** For web scraping the Wikipedia tables.
* **Spotipy:** A lightweight Python library for the Spotify Web API.

## 🚀 Getting Started

### Prerequisites
1. A **Spotify Account** (Premium or Free).
2. A Spotify Developer Account to get your API keys.

### Spotify API Setup
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
2. Click **Create an App**.
3. Name your app and add a description.
4. Edit the app settings and set the **Redirect URI** to `http://example.com` (or any valid local URL).
5. Copy your **Client ID** and **Client Secret**.

### Installation & Environment Configuration
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/EchoArchive.git](https://github.com/YOUR_USERNAME/EchoArchive.git)
   cd EchoArchive
