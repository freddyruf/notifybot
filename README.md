# notifybot

Hi, this bot is for being notified when we are sent a message containing one or more pieces of a string that I choose, which can be updated with telegram commands and not via code. 

The bot uses a list containing the pieces of string you will have given it and will check every single message you receive on your account to see if it contains any of those elements

The bot takes advantage of its own account(to bypass the inability of bots to join as members on servers) and a backing bot. Let's start with the explanation to set it up:

0) You must have installed python with pip, and the libraries used in the code, such as tgcrypto and pyrogram.

1) Download the 3 files in the reposity

2)Go to https://my.telegram.com/apps and register with your number in international format, after that follow the instructions it asks for. Then you have to copy and paste API ID and API Hash found on the site into the file dettails.py, then save and exit, open the two remaining files in the reposity and replace where specified with *******___****** (found in both at the end of the files), you have to enter in one your own username and in the other the username of the support bot, in the way specified between the asterisks, then save.

3) Create two folders, in one put Main Bot and in the other Main Userbot, then copy dettails.py and paste it into both folders

4) Start all two files, they will ask you bot token/phone number, you have to enter your bot token in the run of Main Bot file and your number in the run of Main Userbot, then follow the steps given

5)the bot is ready


To use it there are the following commands whose use is obvious:

/add*
/remove*
/print
/reset
/modify*

*Commands need a parameter to work, it will be asked only after sending message containing the command, not together

The bot when it receives a message containing something you entered to it with /add will send a message to the bot that will send it back to you (With § present at the end to avoid endless loops)


Translated with www.DeepL.com/Translator (free version)
