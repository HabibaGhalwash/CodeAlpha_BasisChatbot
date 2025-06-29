def chatbot():
    print("ChatBot: Hello! Type something to start a conversation or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("ChatBot: Hi!")
        elif user_input in ["how are you", "how are you doing"]:
            print("ChatBot: I'm fine, thanks!")
        elif user_input in ["bye", "goodbye"]:
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: I'm not sure how to respond to that.")

chatbot()
