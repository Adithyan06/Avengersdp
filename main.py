import os
import ffmpeg
from pyrogram import Client, filters

from pyrogram.types import Message


app = Client(

    "Broadcast Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

# Handler for /start command

@app.on_message(filters.command("start"))

def start_handler(client: Client, message: Message):

    client.send_message(

        chat_id=message.chat.id,

        text="Welcome! Please send me a video file to compress."

    )

# Handler for video compression command

@app.on_message(filters.video)

def compress_video(client: Client, message: Message):

    video = message.video
    if video:

        # Download the video file

        video_file = client.download_media(video)

        

        # Compress the video using ffmpeg

        compressed_file = f"compressed_{video.file_id}.mp4"

        os.system(f"ffmpeg -i {video_file} -vf 'scale=640:480' -c:a copy {compressed_file}")

        

        # Send the compressed video back to the user

        client.send_video(

            chat_id=message.chat.id,

            video=compressed_file,

            caption="Here is your compressed video."

        )

        

        # Delete the temporary files

        os.remove(video_file)

        os.remove(compressed_file)

    else:

        client.send_message(

            chat_id=message.chat.id,

            text="Please send a video file to compress."

        )

# Start the bot

app.run()
        
