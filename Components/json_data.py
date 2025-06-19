import json
from random import random

COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

class JsonData:
    def Responses_Template(self,cmd):
        with open("chatbot_responses_template.json","r",encoding="utf-8") as f:
            data = json.load(f)
            if cmd in COMMANDS: return random.choice(" ".join(data["response_templates"][COMMANDS[cmd]]["responses"]))
            else: return ""

    def Patterns(self,cmd):
        with open("patterns.json","r",encoding="utf-8") as f:
            data = json.load(f)
            if cmd in COMMANDS: return random.choice(" ".join(data["patterns"][COMMANDS[cmd]]["keywords"]))
            else: return ""
