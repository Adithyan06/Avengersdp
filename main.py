import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

import logo_maker 

app = Client(

    "Logo Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)
# logo_maker = LogoMaker()

# Function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to Logo Maker Bot! Send me a text to create a logo."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

@app.on_message(filters.text)

def handle_logo_creation(client: Client, message: Message):

    # Get the text from the user's message

    text = message.text.strip()

    # Create the logo using LogoMaker

    logo_path = logomaker.create_logo(text)

    # Send the logo to the user

    client.send_photo(chat_id=message.chat.id, photo=logo_path)

# Run the Pyrogram client

app.run()

