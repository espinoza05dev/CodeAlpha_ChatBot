from json_data import JsonData as JD
class RuleEngine:
    def __init__(self,cmd):
        self.pattern = JD.Responses_Template(cmd)

    def apply_rules(self, cmd):
        return  self.pattern.get(cmd)