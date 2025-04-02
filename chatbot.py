import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random
import datetime

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define response patterns
responses = {
    "greeting": ["Hello! How can I help you today?", "Hi there! What’s on your mind?", "Hey! How’s it going?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You’re welcome!", "Happy to help!", "Anytime!"],
    "weather": ["I can’t check real weather, but it’s probably sunny somewhere!", "Want to know about weather? I’d say it’s a great day to chat!"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')} (as of my clock on April 1, 2025)."],
    "who_are_you": ["I’m Grok, a friendly AI built by xAI, here to answer your questions!", "I’m Grok, your chat buddy from xAI!"],
    "what_can_you_do": ["I can chat about weather, time, or just say hi! Ask me anything!", "I’m here to answer simple questions and have a good time!"],
    "default": ["Hmm, I’m not sure about that. Try asking something else!", "I didn’t catch that—can you rephrase it?"]
}

# Define intent recognition rules
def get_intent(user_input):
    tokens = [lemmatizer.lemmatize(token.lower()) for token in word_tokenize(user_input)]
    
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "later"]):
        return "goodbye"
    elif any(word in tokens for word in ["thanks", "thank", "appreciate"]):
        return "thanks"
    elif any(word in tokens for word in ["weather", "rain", "sun"]):
        return "weather"
    elif any(word in tokens for word in ["time", "clock", "hour"]):
        return "time"
    elif any(word in tokens for word in ["who", "what", "you"]):
        if "are" in tokens or "you" in tokens:
            return "who_are_you"
    elif any(word in tokens for word in ["can", "do", "help"]):
        return "what_can_you_do"
    else:
        return "default"

# Chatbot response function
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Main chat loop
def run_chatbot():
    print("Chatbot: Hello! I’m Grok, your AI assistant. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        if not user_input:
            print("Chatbot: Please say something!")
            continue
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()