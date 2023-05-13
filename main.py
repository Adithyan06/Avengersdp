import os
from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(

    "Logo Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)
# Function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Welcome to Broadcast Bot! Use /broadcast to send a message to all users."

    client.send_message(chat_id=message.chat.id, text=welcome_message)

# Function to handle /broadcast command

@app.on_message(filters.command("broadcast"))

def handle_broadcast_command(client: Client, message: Message):

    # Check if the message is sent by the bot owner

    if message.from_user.id == 1078407883:

        # Get the message text

        broadcast_message = message.text[11:]  # Remove the "/broadcast " part from the message

        # Get all the users in the bot's conversation list

        users = client.get_chat_members(chat_id=message.chat.id)

        # Send the broadcast message to each user

        for user in users:

            user_id = user.user.id

            try:

                client.send_message(chat_id=user_id, text=broadcast_message)

            except Exception as e:

                print(f"Failed to send message to user {user_id}: {e}")

        success_message = "Broadcast sent successfully!"

        client.send_message(chat_id=message.chat.id, text=success_message)

    else:

        error_message = "Sorry, you don't have permission to use this command."

        client.send_message(chat_id=message.chat.id, text=error_message)

# Run the Pyrogram client

app.run()

