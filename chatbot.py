import re

def chatbot(user_input) :
    user_input = user_input.lower()

    if re.search(r"\b(hello|hi|hey)\b", user_input) :
        return "Hello, how are you ?"

    elif re.search(r"\b(name)\b", user_input) :
        return "I am a simple python chatbot"

    elif re.search(r"\b(how are you)\b", user_input) :
        return "I am fine ! What about you ?"

    elif re.search(r"\b(time)\b", user_input) :
        return "Sorry, I cannot tell the current time."

    elif re.search(r"\b(bye|goodbye)\b", user_input) :
        return "Goodbye ! Have a nice day."

    else :
        return "Sorry, I didn't understand that."


print("Chatbot : Hello ! start chatting with me.")
print("Type 'bye' to exit.")

while True :
    user = input("You : ")
    response = chatbot(user)
    print("Chatbot : ", response)

    if re.search(r"\b(bye|goodbye)\b", user.lower()) :
        break