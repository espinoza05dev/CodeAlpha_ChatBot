from Components.inputs_process import In_OutPut as IO

def chatbot():
    chat = True
    clean_In = IO()
    token = IO()
    print("WELLCOME I AM YOUR CHAT BOT ")
    print("WRITE ANYTHING I GOING TO TRY TO HELP YOU")
    while chat:
        msg = token.tokenize(clean_In.CleanInput(input("Write something: ")))

        if msg == 'exit': chat = False

if __name__ == "__main__":
    chatbot()
