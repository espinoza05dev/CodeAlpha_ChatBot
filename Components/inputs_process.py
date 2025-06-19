class In_OutPut:
    def CleanInput(self,text):
        return "".join(text.lower().strip().replace(' ','_').replace('!','').replace('?',''))

    def tokenize(self,text):
        return "".join(text.split())