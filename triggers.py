from discord import channel, message
from TriggerResponse import *
import config
import random

#useful for if you don't want a specific set of emojis for each individual trigger response
universal_emojis = ["😀", "🤣", "🤗"]

"""Server IDs"""
ALL_SERVERS = 0  #will be used in all servers the bot is in
#replace with your server ID
MY_SERVER = 1234 #will only be used in a specific server

"""Emoji Enums"""
NO_EMOJIS    = 0
RANDOM_EMOJI = 1
ALL_EMOJIS   = 2

#Example TriggerResponse object

#These are the phrases the bot will respond to
greeting_trigger = [r"hello", r"howdy", r"hola"] 
#This will be printed to the terminal whenever the bot detects a phrase in the list
greeting_debug = "Greeted\n"

#This is a list of possible responses, chosen at random
#Setting this list to None will just have the bot react with an emoji
greeting_respond = ["Hello there!", "Hi!", "How are you today?"]


#if you set the react parameter to RANDOM_EMOJI when making your TriggerResponse object
# it'll react with a random emoji from this list
greeting_emojis = ["😊", "😃", "👋"]

#Tying it all together...
greeting = TriggerResponse(greeting_trigger, greeting_debug, greeting_respond, RANDOM_EMOJI, greeting_emojis, ALL_SERVERS)


#here's an example where you can mention the author message
mention_trigger = [r"mention me"]
mention_debug = "User wants mentioned"
#note how we don't have a response yet here. 
#We need to declare that variable when a message is sent, with the ExampleStuff Class

class Triggers:
    author_mention = "shouldn't see this"

    #if you want to mention the author in a list, you must declare it in this class and in the __init__ function
    mention_respond = ["Hello, " + author_mention + "!", "Good to see you, " + author_mention + "!"]
    mention = TriggerResponse(mention_trigger, mention_debug, mention_respond, NO_EMOJIS, greeting_emojis, MY_SERVER)

    #This is a list of all the trigger_responses objects you've made
    trigger_responses = [greeting, mention]

    def __init__(self, author_mention):
        self.author_mention = author_mention

        #we need to redeclare the responses involving the message author
        global mention_respond
        self.mention_respond = ["Hello, " + author_mention + "!", "Good to see you, " + author_mention + "!"]
        self.mention = TriggerResponse(mention_trigger, mention_debug, self.mention_respond, NO_EMOJIS, greeting_emojis, MY_SERVER)
        self.trigger_responses = [greeting, self.mention]