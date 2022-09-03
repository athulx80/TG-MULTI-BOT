import os
import re
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from variables import *

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.id = me.id
       self.name = me.first_name
       self.mention = me.mention
       self.username = me.username

       
print('bot started......⚡️')  
bot = App()
bot.run()


        










