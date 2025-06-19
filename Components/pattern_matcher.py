from json_data import JsonData as JD
class PatternMatcher:
    def __init__(self, cmd):
        self.patterns = JD.Patterns(cmd)

    def match(self, cmd):
        return self.patterns.get(cmd)
