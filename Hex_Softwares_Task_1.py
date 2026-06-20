knowledge_base = {
    "hello": "Hello! How can I assist you today?",

    "artificial intelligence":
    "Artificial Intelligence is the simulation "
    "of human intelligence by machines.",

    "how are you":
    "I'm functioning perfectly and ready to help.",

    "machine learning":
    "Machine Learning enables computers to learn "
    "patterns from data and improve their "
    "performance without explicit programming.",

    "python":
    "Python is a versatile programming language "
    "widely used in AI, Machine Learning, "
    "Data Science, and Web Development."
}

print("===== AI CHATBOT =====")

while True:

    query = input("You: ").lower().strip()

    if query == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    found = False

    for key in knowledge_base:
        if key in query:
            print("Bot:", knowledge_base[key])
            found = True
            break

    if not found:
        print("Bot: I do not have information "
              "about that topic.")
