import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

import requests

app = Client(

    "Anime bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

# Function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to Anime Bot! Send me an image and I'll convert it to anime style."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

@app.on_message(filters.photo)

def handle_image_conversion(client: Client, message: Message):

    # Get the photo file ID

    photo_file_id = message.photo[-1].file_id

    # Get the file path of the photo

    file_info = client.get_file(photo_file_id)

    file_path = file_info.file_path

    # Download the photo file

    photo_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"

    photo_path = f"image.jpg"

    response = requests.get(photo_url)

    with open(photo_path, "wb") as f:

        f.write(response.content)

    # Convert the image to anime style using waifu2x-ncnn-vulkan

    anime_path = f"anime.jpg"

    os.system(f"waifu2x-ncnn-vulkan -i {photo_path} -o {anime_path}")

    # Send the converted image back to the user

    client.send_photo(chat_id=message.chat.id, photo=anime_path)

# Run the Pyrogram client

app.run()

