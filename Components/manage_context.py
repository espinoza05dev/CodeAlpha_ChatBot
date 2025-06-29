from random import choice
import json
import os


class ManageContext:
    def __init__(self):
        self.current_context = None
        self.conversation_history = []
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.template_path = os.path.join(self.current_dir, '..', 'data_json', 'chatbot_responses_template.json')
        self.data = self.load_json_data()

    def load_json_data(self):
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: FILE not found {self.template_path}")
            return {"response_templates": {}}
        except json.JSONDecodeError:
            print("Error: WRONG FORMAT")
            return {"response_templates": {}}

    def set_context(self, context):
        self.current_context = context

    def get_context(self):
        return self.current_context

    def add_to_history(self, user_input, bot_response):
        self.conversation_history.append({
            "user": user_input,
            "bot": bot_response,
            "context": self.current_context
        })

    def should_add_follow_up(self):
        return (self.current_context == "initial_greeting" or
                len(self.conversation_history) == 0)

    def get_follow_up(self, intent):
        if intent in self.data.get("response_templates", {}):
            follow_ups = self.data["response_templates"][intent].get("follow_up", [])
            if follow_ups and self.should_add_follow_up():
                return choice(follow_ups)
        return None

    def generate_response(self, user_input, intent):
        if intent not in self.data.get("response_templates", {}):
            return "I'm sorry, but I don't understand what you meant."

        responses = self.data["response_templates"][intent].get("responses", [])
        if not responses:
            return "I'm sorry, I don't have an answer for that."

        main_response = choice(responses)

        context = self.data["response_templates"][intent].get("context")
        if context:
            self.set_context(context)

        follow_up = self.get_follow_up(intent)

        if follow_up:
            final_response = f"{main_response} {follow_up}"
        else:
            final_response = main_response

        self.add_to_history(user_input, final_response)

        return final_response
