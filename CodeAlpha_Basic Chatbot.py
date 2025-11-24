def get_reply(user_message):
    user_message = user_message.lower()

    if user_message == "hello":
        return "Hi!"
    elif user_message == "how are you":
        return "I'm fine, thanks!"
    elif user_message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

# Main chatbot loop
print("Chatbot is running! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    reply = get_reply(user_input)
    print("Bot:", reply)

    if user_input.lower() == "bye":
        break