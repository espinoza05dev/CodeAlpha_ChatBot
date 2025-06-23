import json
from random import choice
import os
COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

path_pattern = r"../data_json/patterns.json"
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..', 'data_json', path_pattern)

class PatternMatcher:
    def match(self, cmd):
        with open(path_pattern, "r", encoding="utf-8") as f:
            data = json.load(f)
            if cmd in COMMANDS: return choice(data["patterns"][COMMANDS[cmd]]["keywords"])
            else: return ""

if __name__ == '__main__':
    res = PatternMatcher()
    print(res.match(1))
