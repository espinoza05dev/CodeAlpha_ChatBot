class In_OutPut:
    def CleanInput(self,text):
        if not text:
            return ""
        return "".join(text.lower().strip().replace(' ','_').replace('!','').replace('?',''))
    def tokenize(self,text):
        return text.split()