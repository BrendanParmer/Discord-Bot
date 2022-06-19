from discord import channel, message
from TriggerResponse import *
import config
import random

#useful for if you don't want a specific set of emojis for each individual trigger response
universal_emojis = ["😀", "🤣", "🤗"]

#Example TriggerResponse object

#These are the phrases the bot will respond to
greeting_trigger = [r"\b[Hh]ello\b", r"\b[Hh]owdy\b", r"\b[Hh]ola\b"] 
#This will be printed to the terminal whenever the bot detects a phrase in the list
greeting_debug = "Greeted\n"
#This is a list of possible responses, chosen at random
greeting_respond = ["Hello there!", "Hi!", "How are you today?"]
#if you set the react parameter to True when making your TriggerResponse object
# it'll react with a random emoji from this list
greeting_emojis = ["😊", "😃", "👋"]

#Tying it all together...
greeting = TriggerResponse(greeting_trigger, greeting_debug, greeting_respond, True, greeting_emojis)


#here's an example where you can mention the author message
mention_trigger = [r"Mention me"]
mention_debug = "User wants mentioned"
#note how we don't have a response yet here. 
#We need to declare that variable when a message is sent, with the ExampleStuff Class

class Triggers:
    author_mention = "shouldn't see this"

    #if you want to mention the author in a list, you must declare it in this class and in the __init__ function
    mention_respond = ["Hello, " + author_mention + "!", "Good to see you, " + author_mention + "!"]
    mention = TriggerResponse(mention_trigger, mention_debug, mention_respond, False, greeting_emojis)

    #This is a list of all the trigger_responses objects you've made
    trigger_responses = [greeting, mention]

    def __init__(self, author_mention):
        self.author_mention = author_mention

        #we need to redeclare the responses involving the message author
        global mention_respond
        self.mention_respond = ["Hello, " + author_mention + "!", "Good to see you, " + author_mention + "!"]
        self.mention = TriggerResponse(mention_trigger, mention_debug, self.mention_respond, False, greeting_emojis)
        self.trigger_responses = [greeting, self.mention]