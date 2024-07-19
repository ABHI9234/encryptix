def chatbot(user_input):
    #converting the user input into the lowercase
    user_input = user_input.lower()

    # pre-defining the rules and responses
    greetings = ['hi','hello','hey','hey,whats up','good morning','good afternoon','good evening','greetings']
    Farewells = ['goodbye','bye','see you ','see you later','farewell','nice to meet you']
    questions = ['who are you','how are you','what is your name','what do you do','what is your favourite color', 'what is your favourite sport','what is your favourite food','what is your age']
    response_default = 'i am a simple chatbot , you can greet me to ask something '

    #checking for matches and according to matches it will provide the response 
    if any(Farewell in user_input for Farewell in Farewells):
        return "goodbye!!! HAVE A NICE DAY..."
    elif any(greeting in user_input for greeting in greetings):
        if "good morning" in user_input:
            return " GOOD MORNING ,how can i help you "
        elif "good evening" in user_input:
            return "GOOD EVENING , how can i help you"
        elif "good afternoon" in user_input:
            return "GOOD AFTERNOON , how can i help you"
        else:
            return "HELLO, how can i help you today?"
    elif any(question in user_input for question in questions):
        if "how are you" in user_input:
            return " I am Alright!!! How can i assist you?"
        elif "what is your name" in user_input:
            return "I am a simple chatbot.."
        elif "what do you do" in user_input:
            return "i am here , to chat with you and answer your questions, How can i help you??"
        elif "what is your favourite colour" in user_input:
            return " I dont have a favorite color "
        elif "who are you" in user_input:
            return "I am a simple chatbot, i am here to chat with you"
        elif "what is your favourite sport" in user_input:
            return "As a program , i don't have any favourite sport. i am a simple chatbot"
        elif "what is you favourite food " in user_input:
            return "NONE "
        elif "what is your age" in user_input:
            return "as a program, i don't have any specific age like HUMAN, i am simple chatbot..."
    else:
        return response_default


# EXAMPLE USAGE
print('i am a chatbot , how can i help you?')
print("========================================")
while True:
    user_input = input ("YOU: ")
    if user_input.lower()== "exit":
        print("CHATBOT: goodbye!!!")
        break
    else:
        response = chatbot(user_input)
        print("CHATBOT: ",response)