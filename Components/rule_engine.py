import json
from random import choice
import os
COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

path_template = "chatbot_responses_template.json"
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..', 'data_json', path_template)

class RuleEngine:
    def apply_rules(self,cmd):
        with open(json_path,"r",encoding="utf-8") as f:
            data = json.load(f)
            if cmd in COMMANDS:return choice(data["response_templates"][COMMANDS[cmd]]["responses"])
            else: return ""

if __name__ == '__main__':
    res = RuleEngine()
    print(res.apply_rules(2))