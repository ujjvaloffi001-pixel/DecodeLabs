# Rule-Based AI Chatbot

print("Welcome to Rule-Based AI Chatbot")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    elif user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I assist you today?")

    elif "your name" in user_input:
        print("Bot: I am a Rule-Based AI Chatbot created using Python.")

    elif "how are you" in user_input:
        print("Bot: I am doing great! Thanks for asking.")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: Current time is {current_time}")

    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    elif "python" in user_input:
        print("Bot: Python is a popular programming language used for AI, Machine Learning, Web Development, and more.")

    elif "machine learning" in user_input:
        print("Bot: Machine Learning enables computers to learn patterns from data and make predictions.")

    elif "artificial intelligence" in user_input:
        print("Bot: Artificial Intelligence is the simulation of human intelligence in machines.")

    elif "who created you" in user_input:
        print('Bot: I was created by a DecodeLabs trainee "UJJVAL" using Python.')

    elif "help" in user_input:
        print("""
Bot: I can answer:
- Greetings (Hi, Hello)
- My name
- Current date
- Current time
- Python
- Machine Learning
- Artificial Intelligence
- Who created me
- Exit command
""")

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see what I can do.")