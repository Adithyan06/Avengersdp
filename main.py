import pyrogram

from pyrogram import Client, filters

from pyrogram.types import Message


    "Anime bot",

    bot_token = os.environ["BOT_TOKEN"],

    api_id = int(os.environ["API_ID"]),

    api_hash = os.environ["API_HASH"]

)
