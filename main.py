import os
from pyrogram import Client, filters
from pyrogram.types import Message

app = Client(

    "Broadcast Bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)
# Authorized users (add your desired user IDs here)

authorized_users = [USER_ID_1, USER_ID_2, USER_ID_3]


users = set()

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

# Function to handle incoming messages

@app.on_message(filters.command("start"))

def handle_start_command(client: Client, message: Message):

    welcome_message = "Hello 💦"

    client.send_message(chat_id=message.chat.id, text=welcome_message)
    users.add(message.chat.id)

# Function to handle /broadcast command

@app.on_message(filters.command("ad"))

def handle_broadcast_command(client: Client, message: Message):

    # Check if the message is sent by an authorized user

    if message.from_user.id == 1078407883:

        # Get the message text

        broadcast_message = get_text(message)  # Remove the "/broadcast " part from the message

        # Send the broadcast message to each user

        for user_id in users:

            try:

                client.send_message(chat_id=user_id, text=f"**Kannan**: {broadcast_message}")

            except Exception as e:

                print(f"Failed to send message to user {user_id}: {e}")

        success_message = "Broadcast sent successfully!"

        client.send_message(chat_id=message.chat.id, text=success_message)

    else:

        error_message = "Sorry, you don't have permission to use this command."

        client.send_message(chat_id=message.chat.id, text=error_message)
        
 # Function to handle /users command

@app.on_message(filters.command("b"))

def handle_users_command(client: Client, message: Message):

    # Check if the message is sent by an authorized user

    if message.from_user.id == 1078407883:

        # Get the total number of users

        total_users = len(users)

        users_message = f"Total users: {total_users}"

        client.send_message(chat_id=message.chat.id, text=users_message)

    else:

        error_message = "Sorry, you don't have permission to use this command."

        client.send_message(chat_id=message.chat.id, text=error_message)
        
@app.on_message(filters.command("v"))
def handle_broadcast_command(client: Client, message: Message):

    # Check if the message is sent by an authorized user

    if message.from_user.id == 5737877514:

        # Get the message text

        broadcast_message = get_text(message)  # Remove the "/broadcast " part from the message

        # Send the broadcast message to each user

        for user_id in users:

            try:

                client.send_message(chat_id=user_id, text=f"**Abhiraj**: {broadcast_message}")

            except Exception as e:

                print(f"Failed to send message to user {user_id}: {e}")

        success_message = "Broadcast sent successfully!"

        client.send_message(chat_id=message.chat.id, text=success_message)

    else:

        error_message = "Sorry, you don't have permission to use this command."

        client.send_message(chat_id=message.chat.id, text=error_message)
       
@app.on_message(filters.command("ab"))
def handle_broadcast_command(client: Client, message: Message):

    # Check if the message is sent by an authorized user

    if message.from_user.id == 1414132123:

        # Get the message text

        broadcast_message = message.text[11:]  # Remove the "/broadcast " part from the message

        # Send the broadcast message to each user

        for user_id in users:

            try:

                client.send_message(chat_id=user_id, text=f"**Abhishek**: {broadcast_message}")

            except Exception as e:

                print(f"Failed to send message to user {user_id}: {e}")

        success_message = "Broadcast sent successfully!"

        client.send_message(chat_id=message.chat.id, text=success_message)

    else:

        error_message = "Sorry, you don't have permission to use this command."

        client.send_message(chat_id=message.chat.id, text=error_message)

        

        
# Run the Pyrogram client

app.run()
