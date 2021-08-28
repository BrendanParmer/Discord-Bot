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
    dad_start = r"((.*?)\b[Ii]\s[Aa][Mm]\b\s)|((.*?)\b[Ii]\'?[Mm]\b\s?)"
    dad_debug = "Dad joke"
    if bool(re.match(dad_start, message.content)):
        print(dad_debug)
        start = re.search(dad_start, message.content).end()

        substring_array = re.split(dad_start, message.content, 2)
        dad_end = r"([\.\,\?\!\;\:]|$)"
        end = re.search(dad_end, substring_array[5]).start() + start

        new_name = message.content[start : end]

        greetings = ["Hello ", "Salutations ", "Hi ", "Hi ", "Hi ", "Good day "]
        greeting = random.choice(greetings)
        endings = ["", "?", "!", ".", " :)", " ;)", " :(", " >:(", "", "", "", ".", ".", "", "."]
        ending = random.choice(endings)
        await message.channel.send(greeting + new_name + ", I'm Dad" + ending)

    #Phrase triggers defined in example_stuff.py
    for x in stuff.trigger_responses:
        if bool(re.match(x.trigger, message.content)):
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