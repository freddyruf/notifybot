from pyrogram import Client
from pyrogram import filters
from dettails import api_hash 
from dettails import api_id
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

import time
 
 
bot = Client("my_account", api_id=api_id, api_hash=api_hash,)
 
@bot.on_message(filters.text)
 
def Main(client,message):
    bot.send_message(chat_id="******Your personal username with @******",text=message.text) 


 
    
 
bot.run()
 

