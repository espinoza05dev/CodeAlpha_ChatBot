class RuleEngine:
    def __init__(self):
        self.rules = {
            'greeting': 'respond_greeting',
            'goodbye': 'respond_goodbye',
            'help': 'provide_help',
            'thanks': 'acknowledge_thanks',
            'unknown': 'ask_clarification'
        }

    def apply_rules(self, text,in_text):
        return  self.rules.get(text, 'unknown')