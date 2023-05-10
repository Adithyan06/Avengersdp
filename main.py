import os

import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message

import openai

# Set up your OpenAI credentials

openai.api_key = "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"

# Set up your Telegram bot token

bot_token = "2054068506:AAHWDguBfxi7uingDrz3ozodZp16TAQK3Og"

# Set up your OpenAI chat model ID

model_id = "gpt-3.5-turbo"

# Create a Pyrogram client

app = Client("my_chat_bot", bot_token=bot_token)

# Define a function to generate a response using OpenAI's GPT-3.5

def generate_response(message: str) -> str:

    response = openai.Completion.create(

        engine="text-davinci-003",  # or "text-davinci-002" for GPT-3 (non-turbo)

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

