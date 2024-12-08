from pyrogram import Client, filters
import os
import requests
import yt_dlp
from pyrogram.types import Message
from youtube_search import YoutubeSearch

# Initialize your Pyrogram client
api_id = "5445756"
api_hash = "2a924a2f877aba6beed255e250f2ec2b"
bot_token = "2054068506:AAEpURXBDGdcZNUq_jmyAv9u2YnrrzAq7N0"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
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
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
# Define a command handler for the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Welcome to MusicBot! Send me a voice message or an audio file, and I'll recognize the music and send it back to you in FLAC format.")


@app.on_message(filters.command(["yts", "ytsearch"]))
async def yt_search(client, message):
    query = get_text(message)
    print(f"ytsearch:{query}")
    if not query:
        return await message.reply_text("`Give me Something to Search in YouTube!`😇")
    try:
        msg = await message.reply("🔎")
        results = YoutubeSearch(query, max_results=10).to_dict()
