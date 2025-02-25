import nltk
from nltk.chat.util import Chat, reflections

# Define some pairs of patterns and responses
pairs = [
    (r"Hi|Hello|Hey", ["Hello!", "Hi there!", "Hey, how can I help you?"]),
    (r"How are you?", ["I'm doing great, thank you!", "I'm good, how about you?"]),
    (r"What's your name?", ["I am a chatbot, but you can call me Bot."]),
    (r"Tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]),
    (r"Where are you from?", ["I exist in the digital world, so no specific location!"]),
    (r"(.*) your (.*)", ["I’m not sure what you're asking. Could you rephrase?"]),
    (r"Bye|Goodbye", ["Goodbye! It was nice talking to you.", "Take care!"]),
]

# Create a chatbot instance with defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Start the chat
def chat():
    print("Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I didn't understand that.")

# Run the chatbot
if __name__ == "__main__":
    chat()
