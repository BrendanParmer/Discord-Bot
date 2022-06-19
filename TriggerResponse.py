import re

class TriggerResponse:
    trigger = ""    #list of trigger regex phrases
    debug = ""      #debug message
    response = []   #list of response phrases
    is_emoji = 0   #whether to react with an emoji or not
    """
    - 0 : NO_EMOJIS    - won't react with any emoji
    - 1 : RANDOM_EMOJI - will react with one random emoji
    - 2 : ALL_EMOJIS   - will react with every emoji
    """
    emojis = []
    server = 0
    def __init__(self, trigger, debug, response, is_emoji, emojis, server):
        self.trigger = r"(?=("+'|'.join(trigger)+r"))"
        self.debug = debug
        self.response = response
        self.is_emoji = is_emoji
        self.emojis = emojis
        self.server = server