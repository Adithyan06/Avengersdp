import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

import requests

# Set up your Spotify credentials

client_id = os.environ["Client_ID"]
client_secret = os.environ["Client_secret"]

# Set up your Telegram bot token

app = Client(

    "Logo Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

# Set up Spotify client

spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

# Define a function to search for a song on Spotify

def search_song(query: str):

    results = spotify_client.search(query, limit=1, type='track')

    if results['tracks']['items']:

        return results['tracks']['items'][0]

    return None

# Define a function to download the song from Spotify

def download_song(track_id: str):

    track_info = spotify_client.track(track_id)

    audio_file = track_info['preview_url']

    if audio_file:

        response = requests.get(audio_file)

        return response.content

    return None

# Define a function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to the Song Downloader Bot! Send me the name of a song, and I'll try to find and download it for you."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

@app.on_message(filters.text)

def handle_message(client: Client, message: Message):

    # Get the user's message

    user_message = message.text

    # Search for the song on Spotify

    track = search_song(user_message)

    if track:

        # Download the song from Spotify

        audio_data = download_song(track['id'])

        if audio_data:

            # Save the song as an audio file

            file_path = f"{track['name']} - {track['artists'][0]['name']}.mp3"

            with open(file_path, 'wb') as audio_file:

                audio_file.write(audio_data)

            # Send the song file to the user

            client.send_audio(chat_id=message.chat.id, audio=file_path)

            os.remove(file_path)  # Remove the temporary audio file

        else:

            error_message = "Sorry, I couldn't download the song. Please try again later."

            client.send_message(chat_id=message.chat.id, text=error_message)

    else:

        not_found_message = "Sorry, I couldn't find the song on Spotify. Please try a different song."

        client.send_message(chat_id=message.chat.id, text=not_found_message)

# Run the Pyrogram client

app.run()

