class In_OutPut:
    def CleanInput(self,text):
        return text.lower().strip().replace(' ','_').replace('!','').replace('?','')

    def tokenize(self,text):
        return text.split()