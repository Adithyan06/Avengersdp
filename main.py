import asyncio
import os
import random
import re
import urllib
# import config

import requests
# from telethon.tl import functions
# from telethon import TelegramClient, events

from pyrogram import Client, filters
# from pyrogram.api import functions


Avengers=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)


url = "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf"


COLLECTION_STRING = [
    "avengers-logo-wallpaper",
    "avengers-hd-wallpapers-1080p",
    "avengers-iphone-wallpaper",
    "iron-man-wallpaper-1920x1080",
    "iron-man-wallpapers",
]

def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile(r"/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(url, "f.ttf")
    img = requests.get(fy)
    with open("donottouch.jpg", "wb") as outfile:
        outfile.write(img.content)
    return "donottouch.jpg"


async def Avengers_main():
    while True:
        await animepp()
        file = await Avengers.set_profile_photo(photo="donottouch.jpg")        
        me = await Avengers.get_me()
        photos = await Avengers.get_profile_photos("me")
            
        os.system("rm -rf donottouch.jpg")
  
        await asyncio.sleep(60)   
