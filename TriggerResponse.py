import re

class TriggerResponse:
    trigger = ""    #list of trigger regex phrases
    debug = ""      #debug message
    response = []   #list of response phrases
    is_emoji = False   #whether to react with an emoji or not
    emojis = []
    def __init__(self, trigger, debug, response, is_emoji, emojis):
        self.trigger = r"(?=("+'|'.join(trigger)+r"))"
        self.debug = debug
        self.response = response
        self.is_emoji = is_emoji
        self.emojis = emojis