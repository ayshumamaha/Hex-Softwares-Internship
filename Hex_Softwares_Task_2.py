import datetime
import webbrowser

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    return current_time

def get_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    return current_date

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid calculation"

print("===== AI VIRTUAL ASSISTANT =====")
print("Type 'bye' to exit\n")

while True:

    command = input("User: ").lower()

    if command == "bye":
        print("Assistant: Goodbye! Have a great day.")
        break

    elif "hello" in command or "hi" in command:
        print("Assistant: Hello! How can I help you today?")

    elif "time" in command:
        print("Assistant: Current Time:", get_time())

    elif "date" in command:
        print("Assistant: Today's Date:", get_date())

    elif "calculate" in command:
        expression = command.replace("calculate", "")
        print("Assistant: Result =", calculate(expression))

    elif "open google" in command:
        print("Assistant: Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        print("Assistant: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "artificial intelligence" in command or "ai" in command:
        print("Assistant: Artificial Intelligence enables machines to simulate human intelligence.")

    else:
        print("Assistant: Sorry, I do not understand that command.")
