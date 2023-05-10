import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

import openai

# Set up your OpenAI credentials

openai.api_key = "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"

# Set up your Telegram bot token
app = Client(

    "Logo Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)

# Set up your OpenAI chat model ID

model_id = "gpt-3.5-turbo"

# Define a function to generate a response using OpenAI's GPT-3.5

def generate_response(message: str) -> str:

    response = openai.Completion.create(

        engine="text-davinci-002",  # or "text-davinci-002" for GPT-3 (non-turbo)

        prompt=message,

        max_tokens=50,

        temperature=0.7,

        n=1,

        stop=None,

    )

    return response.choices[0].text.strip()

# Define a function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to the ChatBot! Send me a message, and I'll respond."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

@app.on_message(~filters.command("start"))

def handle_message(client: Client, message: Message):

    # Get the user's message

    user_message = message.text

    # Generate a response using OpenAI

    response = generate_response(user_message)

    # Send the response back to the user

    client.send_message(chat_id=message.chat.id, text=response)

# Run the Pyrogram client

app.run()

