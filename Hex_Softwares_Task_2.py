def detect_emotion(text):

    text = text.lower()

    happy_words = [
        "happy", "excited", "joy", "promotion",
        "great", "excellent", "wonderful"
    ]

    sad_words = [
        "sad", "lonely", "disappointed",
        "depressed", "upset"
    ]

    angry_words = [
        "angry", "furious", "mad",
        "annoyed", "rage"
    ]

    for word in happy_words:
        if word in text:
            return "Happy"

    for word in sad_words:
        if word in text:
            return "Sad"

    for word in angry_words:
        if word in text:
            return "Angry"

    return "Neutral"


print("===== EMOTION DETECTION SYSTEM =====\n")

while True:

    user_text = input("Enter Text: ")

    if user_text.lower() == "exit":
        break

    emotion = detect_emotion(user_text)

    print("\nDetected Emotion:")
    print(emotion)
    print()
