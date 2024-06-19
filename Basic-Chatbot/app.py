import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Predefined responses for simplicity
responses = {
    "greet": ["Hello! How can I help you today?", "Hi there! How can I assist you?"],
    "bye": ["Goodbye! Have a nice day.", "Bye! Take care."],
    "thankyou": ["You're welcome!", "No problem!"],
    "default": ["I'm sorry, I don't understand. Can you please rephrase?", "I'm not sure I follow. Could you clarify?"]
}

def get_intent(text):
    doc = nlp(text)
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greet"
        elif token.lemma_ in ["bye", "goodbye", "see you"]:
            return "bye"
        elif token.lemma_ in ["thank", "thanks"]:
            return "thankyou"
    return "default"

def generate_response(user_input):
    intent = get_intent(user_input)
    return responses[intent][0]

def chat():
    print("Chatbot: Hello! I'm here to chat with you. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == '__main__':
    chat()
