import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

from jiosaavnapi import JioSaavn
# client_id = os.environ["Client_ID"]
# client_secret = os.environ["Client_secret"]

# Set up your Telegram bot token

app = Client(

    "Logo Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

# Set up Spotify client

jiosaavn = JioSaavn()
# Function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to JioSaavn Bot! Send me the name of a song to download."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

@app.on_message(filters.text)

def handle_song_download(client: Client, message: Message):

    # Get the song name from the user's message

    song_name = message.text.strip()

    # Search for the song on JioSaavn

    results = jiosaavn.search_for_song(song_name)

    # Check if any results found

    if results:

        # Get the first result

        song = results[0]

        # Download the song

        song_path = song.download()

        # Send the downloaded song to the user

        client.send_audio(chat_id=message.chat.id, audio=song_path, title=song.title, performer=song.artist)

    else:

        error_message = "Sorry, I couldn't find the song you requested."

        client.send_message(chat_id=message.chat.id, text=error_message)

# Run the Pyrogram client

app.run()
