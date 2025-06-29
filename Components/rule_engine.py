import json
from random import choice
import os
COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21:"fallback_responses",22:"conversation_starters"
}

class RuleEngine:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_path = os.path.join(self.current_dir, '..', 'data_json', 'chatbot_responses_template.json')
        self.response_data = self.load_responses()

    def load_responses(self):
        """Carga las respuestas desde el archivo JSON"""
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.template_path}")
            return {"response_templates": {}}
        except json.JSONDecodeError:
            print("Error: El archivo JSON de respuestas está mal formateado")
            return {"response_templates": {}}

    def apply_rules(self, cmd):
        """Aplica las reglas y devuelve una respuesta apropiada"""
        if cmd in COMMANDS:
            intent = COMMANDS[cmd]
            if intent in self.response_data.get("response_templates", {}):
                responses = self.response_data["response_templates"][intent].get("responses", [])
                if responses:
                    return choice(responses)

        # Respuesta por defecto si no se encuentra
        fallback_responses = [
            "Interesante... ¿podrías contarme más?",
            "No estoy seguro de entender. ¿Puedes reformular tu pregunta?",
            "Cuéntame más sobre eso, me interesa saber tu opinión."
        ]
        return choice(fallback_responses)
