from random import choice
import json

class ManageContext:
    def __init__(self):
        self.current_context = None
        self.conversation_history = []
        self.data = self.load_json_data()

    def set_context(self, context):
        self.current_context = context

    def get_context(self):
        return self.current_context

    def should_add_follow_up(self):
        # Agregar follow_up si es el primer mensaje o contexto inicial
        return (self.current_context == "initial_greeting" or
                len(self.conversation_history) == 0)

    def get_follow_up(self, intent):
        if intent in self.data["response_templates"]:
            follow_ups = self.data["response_templates"][intent].get("follow_up", [])
            if follow_ups and self.should_add_follow_up():
                return choice(follow_ups)
        return None

    def generate_response(self, user_input):
        intent = self.detect_intent(user_input)  # Tu función de detección

        # Respuesta principal
        main_response = choice(
            self.data["response_templates"][intent]["responses"]
        )

        # Establecer contexto
        context = self.data["response_templates"][intent].get("context")
        if context:
            self.set_context(context)

        # Agregar follow_up si corresponde
        follow_up = self.get_follow_up(intent)

        # Construir respuesta final
        if follow_up:
            final_response = f"{main_response} {follow_up}"
        else:
            final_response = main_response

        return final_response

    def load_json_data(self):
        COMMANDS = {
            1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown", 6: "yes", 7: "no", 8: "apologize",
            9: "compliment", 10: "complaint",
            11: "small_talk", 12: "contact", 13: "hours", 15: "weather", 16: "name", 17: "capability", 18: "joke",
            19: "repeat", 20: "unclear",
            21: "fallback_responses", 22: "conversation_starters"
        }

        path_template = r"../data_json/chatbot_responses_template.json"
        with open(path_template,"r",encoding="utf-8") as f:
            data = json.load(f)
            return choice(data["response_templates"]["greeting"]["responses"])


if __name__ == "__main__":
    manage_context = ManageContext()
    print(manage_context.load_json_data())