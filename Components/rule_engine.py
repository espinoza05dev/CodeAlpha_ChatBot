from json_data import JsonData as JD
class RuleEngine:
    def __init__(self):
        self.pattern = JD.Responses_Template()

    def apply_rules(self, cmd):
        return  self.pattern.get(cmd)

if __name__ == '__main__':
    res = RuleEngine()
    print(res.apply_rules(1))