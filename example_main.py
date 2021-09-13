#from logging import exception
from discord import channel
from discord.ext import commands
import re
import random
from example_stuff import * #for custom phrases and stuff
import config

stuff = ExampleStuff(config.author_mention)
bot = commands.Bot('!')

@bot.event
async def on_message(message):
    print("Message received")

    #we want to make sure the bot doesn't accidentally respond to itself infinitely
    if message.author == bot.user:
        print("Message is from me\n")
        return
    
    config.author_mention = message.author.mention #kinda hacky way to get author mention string to the private file
    stuff = ExampleStuff(message.author.mention)

    #Dad jokes
    dad_starts = [r"\b([Ii]\s)?[Aa][Mm]\s\b",
                 r"\b[Ii]([\'’])?[Mm]\s\b"]
    dad_debug = "Dad joke"
    for x in dad_starts:
        if bool(re.search(x, message.content)):
            print(dad_debug)

            substring_array = re.split(x, message.content, 2)
            print(substring_array)

            new_name = substring_array[2]
            print(new_name)

            greetings = ["Hello ", "Salutations ", "Hi ", "Hi ", "Hi ", "Good day "]
            greeting = random.choice(greetings)
            endings = ["", "?", "!", ".", " :)", " ;)", " :(", " >:(", "", "", "", ".", ".", "", "."]
            ending = random.choice(endings)
            await message.channel.send(greeting + new_name + ", I'm Dad" + ending)

    #Phrase triggers defined in example_stuff.py
    for x in stuff.trigger_responses:
        if bool(re.search(x.trigger, message.content)):
            print(x.debug)
            await message.channel.send(random.choice(x.response))
            if x.is_emoji:
                try:
                    await message.add_reaction(random.choice(x.emojis))
                except:
                    await message.add_reaction(random.choice(universal_emojis))
                    print("Tried to use unknown emoji\n")

# this part's important. make sure to replace the content's of the text file with your bot's token
# never share this
with open("EXAMPLE_BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    
    bot.run(TOKEN)