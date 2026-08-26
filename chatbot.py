# ==========================================
# Project 1: Rule-Based AI Chatbot
# Artificial Intelligence
# ==========================================

print("==============================================")
print("          RULE-BASED AI CHATBOT")
print("==============================================")
print("Hello! I am your AI Chatbot.")
print("I can respond to different predefined messages.")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print("----------------------------------------------")


# Continuous conversation loop
while True:

    # Take input from the user
    user_input = input("You: ").lower().strip()

    # 1. Greetings
    if user_input == "hi" or user_input == "hello" or user_input == "hey":
        print("Bot: Hello! Nice to meet you. How can I help you?")

    # 2. Bot's name
    elif user_input == "what is your name" or user_input == "what's your name" or user_input == "your name":
        print("Bot: My name is RuleBot. I am a Rule-Based AI Chatbot.")

    # 3. How the bot is doing
    elif user_input == "how are you" or user_input == "how are you doing":
        print("Bot: I am doing great! Thanks for asking.")

    # 4. What the bot can do
    elif user_input == "what can you do" or user_input == "help":
        print("Bot: I can respond to greetings, answer simple questions,")
        print("Bot: tell you about AI, and have a basic conversation with you.")

    # 5. What is AI
    elif user_input == "what is ai" or user_input == "what is artificial intelligence":
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It is the field of creating systems that can perform")
        print("Bot: tasks that normally require human intelligence.")

    # 6. What is a chatbot
    elif user_input == "what is a chatbot" or user_input == "what is chatbot":
        print("Bot: A chatbot is a computer program designed to communicate")
        print("Bot: with users through text or voice.")

    # 7. Who created the bot
    elif user_input == "who created you" or user_input == "who made you":
        print("Bot: I was created as a Rule-Based AI project.")

    # 8. Thank you
    elif user_input == "thanks" or user_input == "thank you":
        print("Bot: You're welcome!")

    # 9. Compliments
    elif user_input == "you are good" or user_input == "you are great":
        print("Bot: Thank you! That's very kind of you.")

    # 10. Positive feelings
    elif user_input == "i am happy" or user_input == "i feel good":
        print("Bot: That's wonderful! Keep that positive energy going.")

    # 11. Sad feelings
    elif user_input == "i am sad" or user_input == "i feel sad":
        print("Bot: I'm sorry to hear that. I hope things get better soon.")

    # 12. Motivation
    elif user_input == "motivate me" or user_input == "i need motivation":
        print("Bot: Believe in yourself! Every small step takes you")
        print("Bot: closer to your goal. Keep going!")

    # 13. Joke
    elif user_input == "tell me a joke" or user_input == "joke":
        print("Bot: Why do programmers prefer dark mode?")
        print("Bot: Because light attracts bugs!")

    # 14. Study help
    elif user_input == "i need help studying" or user_input == "study help":
        print("Bot: Make a simple study plan, focus on one topic at a time,")
        print("Bot: and take short breaks to stay focused.")

    # 15. Programming
    elif user_input == "what is programming" or user_input == "what is coding":
        print("Bot: Programming is the process of writing instructions")
        print("Bot: that tell a computer what to do.")

    # 16. How the chatbot works
    elif user_input == "how do you work":
        print("Bot: I work using predefined rules.")
        print("Bot: I check your input and select a suitable response")
        print("Bot: using if-else decision-making.")

    # 17. Is the chatbot intelligent?
    elif user_input == "are you intelligent" or user_input == "are you smart":
        print("Bot: I am a basic rule-based chatbot.")
        print("Bot: I follow the rules programmed by my developer.")

    # 18. Morning greeting
    elif user_input == "good morning":
        print("Bot: Good morning! I hope you have a great day.")

    # 19. Afternoon greeting
    elif user_input == "good afternoon":
        print("Bot: Good afternoon! How can I help you?")

    # 20. Evening greeting
    elif user_input == "good evening":
        print("Bot: Good evening! Nice to chat with you.")

    # 21. Exit commands
    elif user_input == "bye" or user_input == "goodbye":
        print("Bot: Goodbye! It was nice talking to you.")
        break

    elif user_input == "exit" or user_input == "quit":
        print("Bot: Chat ended. Have a wonderful day!")
        break

    # 22. Unknown input
    else:
        print("Bot: Sorry, I don't understand that yet.")
        print("Bot: Try saying 'help' to see what I can do.")


# ==========================================
# End of Chatbot
# ==========================================