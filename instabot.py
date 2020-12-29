# imports

import os, random, shutil, glob, time
from itertools import count
from instabot import Bot 

# initializing the bot variables
hours = 12 # the bot will post once every set hours
bot = Bot() # initializing the bot
path = " " # set the path to the folder with all your pictures you want posted
username = " " # instagram username
password = " " # instagram password
caption = " " # instagram picture description

# infinite loop
for i in count(0):
	# logging in
	bot.login(username = username, password = password)

    # choosing a random picture from the specified folder
	picture = random.choice(os.listdir(path))
	print("[IonutSauciuc] Successfully chosen photo.")

    # post the photo
	bot.upload_photo(path + picture, caption = caption) 
	print("[IonutSauciuc] Successfully uploaded photo.")
    
    # deleting the picture
	os.unlink(os.path.join(path, picture + ".REMOVE_ME")) # REMOVE_ME because the instabot modifies the file name after posting to instagram
	print("[IonutSauciuc] Successfully deleted photo.")