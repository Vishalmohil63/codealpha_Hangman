# Basic Rule-based Chatbot (CodeAlpha TASK 4)
# Console I/O | Predefined replies | if-elif | functions | loops

import datetime

def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())

def get_response(msg: str) -> str:
    m = normalize(msg)

    # Greetings
    if any(word in m for word in ["hello", "hi", "hey", "namaste", "hlo"]):
        return "Hi! How can I help you today?"
    # How are you
    elif any(phrase in m for phrase in ["how are you", "kaise ho", "how r u"]):
        return "I'm doing great, thanks for asking! "
    # Name
    elif any(phrase in m for phrase in ["what is your name", "tumhara naam", "your name"]):
        return "I'm a simple rule-based chatbot made for your CodeAlpha task."
    # Time and Date (optional but handy)
    elif "time" in m:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}."
    elif "date" in m or "today" in m:
        return f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}."
    # Help
    elif "help" in m or "commands" in m:
        return ("You can try: hello, how are you, your name, time, date, "
                "joke, bye")
    # Simple joke
    elif "joke" in m:
        return "Why did the developer go broke? Because he used up all his cache. "
    # Bye
    elif any(word in m for word in ["bye", "goodbye", "tata", "see you"]):
        return "Goodbye! Have a great day."
    # Default fallback
    else:
        return "Sorry, I didn't understand that. Try 'help' to see what I can do."

def chat():
    print(" Chatbot ready! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if normalize(user) in ["bye", "goodbye", "tata", "see you"]:
            print("Bot:", get_response(user))
            break
        print("Bot:", get_response(user))

if __name__ == "__main__":
    chat()
