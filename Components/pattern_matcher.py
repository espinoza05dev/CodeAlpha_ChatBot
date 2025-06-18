class PatternMatcher:
    def __init__(self):
        self.patterns = {
            'greeting': ['hello', 'hi', 'hey', 'good morning'],
            'goodbye': ['bye', 'goodbye', 'see you', 'farewell'],
            'help': ['help', 'assist', 'support'],
            'thanks': ['thank', 'thanks', 'appreciate']
        }

    def match(self, in_text):
        for text, keywords in self.patterns.items():
            if any(keywords in in_text for keyword in keywords):
                return text
        return 'unknown'
