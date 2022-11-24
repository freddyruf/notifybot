
from pyrogram import Client
from pyrogram import filters
from dettails import api_hash 
from dettails import api_id
import tgcrypto
import random
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


lista=[]
x=False
y=0                         #initialising variables
yy=0

bot = Client("my_account", api_id=api_id, api_hash=api_hash,)



REPLY_MESSAGE_BUTTONS = [[]]
MAIN_BUTTONS = [["/add","/remove","/edit","/reset","/print"]]

@bot.on_message(filters.command(commands=['start']))
def start(client,message):
    global MAIN_BUTTONS
    reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
    message.reply(text="Hi! use /add to add smoething in the notice list, send it and after send another message with the text, also with /edit /remove. You can also use /reset and /print", reply_markup=reply_markup)

@bot.on_message(filters.command(commands=['print']))
def printed(client,message):
    global lista
    lista.sort()
    z=True
    for c in range(len(lista)):
        z=False            #print avery element in lista
        message.reply_text(text=str(lista[c]))               #print fuction
    if(z):
        message.reply_text(text="There's nothing!") #nothing option
    global MAIN_BUTTONS
    reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
    message.reply(text="Buttons:", reply_markup=reply_markup)               #this to line is for create a Markup, this don't work every tie(Bacouse there is a UBot not a bot)

@bot.on_message(filters.command(commands=['edit']))
def modify(client,message):
    global y
    global REPLY_MESSAGE_BUTTONS
    y=1
    REPLY_MESSAGE_BUTTONS[0].clear()         
    for c in range(len(lista)):
       REPLY_MESSAGE_BUTTONS[0].append(str(lista[c])) 
    reply_markup=ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
    message.reply(text="Cosa vuoi modificare?",reply_markup=reply_markup) 



@bot.on_message(filters.command(commands=['remove']))
def remove(client,message):
    global REPLY_MESSAGE_BUTTONS
    global lista
    text="What do you want to remove?"
    REPLY_MESSAGE_BUTTONS[0].clear()
    for c in range(len(lista)):
        REPLY_MESSAGE_BUTTONS[0].append(str(lista[c]))
    reply_markup=ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
    message.reply(text=text,reply_markup=reply_markup)
    global x
    x=True

#@bot.on_message(filters.command(commands=['distruggi']))
#def destroyed(client,message):
#    global x
#    x=True
#    message.reply_text(text="Dimmi cosa vuoi eliminare:")

@bot.on_message(filters.command(commands=['reset']))
def reset(client,message):
    global lista
    global x
    lista=[]
    x=False
    global MAIN_BUTTONS
    reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
    message.reply(text="Resettata", reply_markup=reply_markup)

zz=False
@bot.on_message(filters.command(commands=['add']))
def adding(client,message):
    global zz
    zz=True
    message.reply(text="What do you want to add?")

@bot.on_message(filters.text)

def Main(client,message):
    global lista
    global x
    global y
    global yy
    global zz
    global MAIN_BUTTONS
    global REPLY_MESSAGE_BUTTONS
    
    if(zz and x==False and y==0):
        zz=False
        lista.append(message.text)                    #notice addition
        reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)    
        message.reply(text="Added!", reply_markup=reply_markup)
        
    if(x):
        lista.remove(message.text)
        x=False                                  #notice remove
        reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
        message.reply(text="Removed!", reply_markup=reply_markup)
    if(y==1):
        
        yy=lista.index(message.text)
        y=3                         #Asking what modify
                              
        message.reply(text="What do you want to modify it with?")
        return 
    if(y==3):
        lista[yy]=message.text
        yy=0                          #notice modify
        reply_markup=ReplyKeyboardMarkup(MAIN_BUTTONS,one_time_keyboard=True,resize_keyboard=True)
        message.reply(text="Modified!", reply_markup=reply_markup)
    if y!=3 and y!=1 and x==False and zz==False and (("§" in message.text)!=True): 
        for c in range(len(lista)):
            if(lista[c] in message.text):
                bot.send_message(chat_id="****** echo bot username with @ ******",text=message.text+" §") #adding § to not create a infinity cycle with the other bot

    

bot.run()
