# Billboard Top 100 to Spotify Playlist

Create a Spotify playlist containing the top 100 songs from Billboard Hot 100 chart for a specific date.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 
- BeautifulSoup (`pip install beautifulsoup4`)
- Requests (`pip install requests`)
- Spotipy (`pip install spotipy`)
- dotenv (`pip install python-dotenv`)

## Usage

1. **Set up Spotify API credentials**:
    - Create a Spotify Developer account and register your application to get client ID and client secret.
    - Set up environment variables in a `.env` file containing your Spotify client ID, client secret, redirect URI, and Spotify username.

2. **Run the script**:
    - Execute the Python script `billboard_to_spotify.py`.
    - Enter the date you want in the format YYYY-MM-DD.

3. **Generate the playlist**:
    - The script will scrape the Billboard Hot 100 chart for the specified date and fetch the top 100 songs.
    - It will then search for each song on Spotify and add them to a new playlist.
    - The playlist will be named as "{Date} Billboard 100" and will be created in your Spotify account.
