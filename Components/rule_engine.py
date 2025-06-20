import json
from random import choice
COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

path_template = r"../data_json/chatbot_responses_template.json"

class RuleEngine:
    def apply_rules(self,cmd):
        with open(path_template,"r",encoding="utf-8") as f:
            data = json.load(f)
            if cmd in COMMANDS:return choice(data["response_templates"][COMMANDS[cmd]]["responses"])
            else: return ""

if __name__ == '__main__':
    res = RuleEngine()
    print(res.apply_rules(1))