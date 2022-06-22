import asyncio
from datetime import date, datetime, time, timedelta
import discord
import re
import random
from triggers import * #for custom phrases and stuff
import config

stuff = Triggers(config.author_mention)
MAX_EMOJI_LIMIT = 20

TASK_WHEN = time(12, 0, 0) #noon UTC time
CHANNEL_ID = 0             #put your channel ID here

class DiscordBot(discord.Client):
    #set up stuff like timed messages
    async def setup_hook(self) -> None:
        self.loop.create_task(self.timer())

    # Handles sending the message at the time of day
    async def timer(self):
        await self.wait_until_ready()
        now = datetime.utcnow()
        if now.time() > TASK_WHEN:
            tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
            seconds = (tomorrow - now).total_seconds()
            await asyncio.sleep(seconds)
        while not self.is_closed():
            now = datetime.utcnow()
            target_time = datetime.combine(now.date(), TASK_WHEN) #replace with your 
            seconds_until_target = (target_time - now).total_seconds()
            await asyncio.sleep(seconds_until_target)
            await self.task() #replace with your own function
            tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
            seconds = (tomorrow - now).total_seconds()
            await asyncio.sleep(seconds)
    
    # Main function you want to run at the time
    async def task(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)
        await channel.send("I am sentient!")

bot = DiscordBot(command_prefix='$',
                 activity = discord.Activity(type=discord.ActivityType.playing,
                                             name="the system"),
                 status = discord.Status.online)

@bot.event
async def on_message(message):
    #we want to make sure the bot doesn't accidentally respond to itself infinitely
    if message.author == bot.user:
        return
    
    config.author_mention = message.author.mention
    stuff = Triggers(message.author.mention)

    """Dad jokes"""
    dad_starts = [r"([Ii]\s)?[Aa][Mm]\s",
                 r"[Ii]([\'\’\"\`])?[Mm]\s",
                 r"\b[Ee]stoy\s",
                  r"\b[Ss]oy\s",
                  r"\b[Jj]e\ssuis\s"]
    punctuation = ['.', ',', ';', ':', '!', '?', '&', '-', '~']
    for x in dad_starts:
        if bool(re.search(x, message.content)):
            substring_array = re.split(x, message.content, 2)
            new_name = ""
            for char in substring_array[2]:
                    if char not in punctuation:
                        new_name += char
                    else:
                        break
            greetings = ["Hello ", "Salutations ", "Hi ", "Hi ", "Hi ", "Good day ", "Greetings "]
            greeting = random.choice(greetings)
            endings = ["", "?", "!", ".", " :)", " ;)", " :(", " >:(", "", "", "", ".", ".", "", "."]
            ending = random.choice(endings)
            await message.channel.send(greeting + new_name + ", I'm Dad" + ending)

            
    content = message.content.lower()
    """Other triggers"""
    for x in stuff.trigger_responses:
        if x.server == message.guild.id or x.server == 0:
            if bool(re.search(x.trigger, content)):
                if x.response is not None:
                    await message.channel.send(random.choice(x.response))
                if x.is_emoji:
                    if x.is_emoji == RANDOM_EMOJI:
                        try:
                            await message.add_reaction(random.choice(x.emojis))
                        except:
                            await message.add_reaction(random.choice(universal_emojis))
                    elif x.is_emoji == ALL_EMOJIS:
                        await message.add_reaction(x.emojis[0])
                        i = 0
                        while i < MAX_EMOJI_LIMIT:
                            try:
                                await message.add_reaction(random.choice(x.emojis))
                                i += 1
                            except:
                                pass

# this part's important. make sure to replace the content's of the text file with your bot's token
# never share this
with open("BOT_TOKEN.txt", "r") as token_file:
    TOKEN = token_file.read()
    print("Token file read")
    
    bot.run(TOKEN)