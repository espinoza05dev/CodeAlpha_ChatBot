from Components.inputs_process import In_OutPut as IO
from Components.rule_engine import RuleEngine as RE
from Components.pattern_matcher import PatternMatcher as PM
from Components.manage_context import ManageContext as MC

COMMANDS = {
    1: "greeting", 2: "goodbye", 3: "help", 4: "thanks", 5: "unknown",
    6: "yes", 7: "no", 8: "apologize", 9: "compliment", 10: "complaint",
    11: "small_talk", 12: "contact", 13: "hours", 15: "weather",
    16: "name", 17: "capability", 18: "joke", 19: "repeat", 20: "unclear",
    21: "fallback_responses", 22: "conversation_starters"
}


def chatbot():
    clean_In = IO()
    rule = RE()
    pattern = PM()
    context = MC()

    chat = True

    print("=" * 50)
    print("WELLCOME, I AM YOUR CHAT BOT")
    print("WRITE ANYTHING, I WILL TRY OT HELP YOU")
    print("WRITE 'adiós', 'bye' or 'exit' TO END THE CONVERSATION")
    print("=" * 50)

    while chat:
        try:
            user_input = input("\nTú: ").strip()

            if not user_input:
                print("Bot: Por favor, escribe algo para poder ayudarte.")
                continue

            cleaned_input = clean_In.CleanInput(user_input)

            matched_command = pattern.match(cleaned_input)

            if matched_command == 2:  # goodbye
                response = rule.apply_rules(matched_command)
                print(f"Bot: {response}")
                chat = False
                continue

            intent = COMMANDS.get(matched_command, "unknown")
            response = context.generate_response(user_input, intent)

            print(f"Bot: {response}")

            # Debug info (opcional - comentar en producción)
            # print(f"[DEBUG] Comando: {matched_command}, Intención: {intent}")

        except KeyboardInterrupt:
            print("\nBot: ¡Hasta luego! Gracias por chatear conmigo.")
            break
        except Exception as e:
            print("Bot: Ups, algo salió mal. ¿Puedes intentar de nuevo?")
            print(f"[ERROR] {e}")


if __name__ == "__main__":
    chatbot()