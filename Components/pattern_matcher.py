import json
from random import choice
import os
COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

class PatternMatcher:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.patterns_path = os.path.join(self.current_dir, '..', 'data_json', 'patterns.json')
        self.patterns_data = self.load_patterns()

    def load_patterns(self):
        try:
            with open(self.patterns_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.patterns_path}")
            return {"patterns": {}}
        except json.JSONDecodeError:
            print("Error: El archivo JSON de patrones está mal formateado")
            return {"patterns": {}}

    def match(self, user_input):
        user_words = user_input.lower().split()
        best_match = 5  # default: unknown
        max_matches = 0

        for cmd_num, intent in COMMANDS.items():
            if intent in self.patterns_data.get("patterns", {}):
                keywords = self.patterns_data["patterns"][intent].get("keywords", [])
                matches = sum(1 for keyword in keywords if keyword.lower() in user_input.lower())

                if matches > max_matches:
                    max_matches = matches
                    best_match = cmd_num

        return best_match

    def get_pattern_keywords(self, cmd):
        if cmd in COMMANDS:
            intent = COMMANDS[cmd]
            if intent in self.patterns_data.get("patterns", {}):
                return self.patterns_data["patterns"][intent].get("keywords", [])
        return []

