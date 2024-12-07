from pyrogram import Client, filters
import os
import requests
import shazamio
import youtube_dl

# Initialize your Pyrogram client
api_id = "5445756"
api_hash = "2a924a2f877aba6beed255e250f2ec2b"
bot_token = "2054068506:AAEpURXBDGdcZNUq_jmyAv9u2YnrrzAq7N0"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Initialize Shazam client for music recognition
shazam = shazamio.Shazam()

# Function to recognize music using Shazam API
def recognize_music(audio_file):
    try:
        track = shazam.recognize_song(audio_file)
        return track
    except Exception as e:
        print(f"Error recognizing music: {e}")
        return None

# Function to download music in FLAC format
def download_music(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '320',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Define a command handler for the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Welcome to MusicBot! Send me a voice message or an audio file, and I'll recognize the music and send it back to you in FLAC format.")

# Define a message handler for audio messages
@app.on_message(filters.audio)
def handle_audio(client, message):
    audio_file = message.audio.file_id
    audio_path = client.download_media(audio_file)
    recognized_track = recognize_music(audio_path)
    if recognized_track:
        track_title = recognized_track['track']['title']
        track_artist = recognized_track['track']['subtitle']
        message.reply_text(f"Recognized track: {track_title} by {track_artist}")
        download_music(recognized_track['track']['key'])
        # Send the downloaded music file to the user
        client.send_audio(chat_id=message.chat.id, audio='path_to_downloaded_file.flac', title=track_title, performer=track_artist)
    else:
        message.reply_text("Sorry, I couldn't recognize the music.")

# Run the bot
app.run()      
