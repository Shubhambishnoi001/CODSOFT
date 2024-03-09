responses = {
    "hello": "Hello! How can I assist you today?",
    "weather": "The weather in your area is sunny with a high of 35°c.",
    "bye": "Goodbye! Have a nice day!",
}

while True:
    user_input = input("You: ").lower()  

   
    if "hello" in user_input:
        print("Chatbot:", responses["hello"])
    elif "weather" in user_input:
        print("Chatbot:", responses["weather"])
    elif "bye" in user_input:
        print("Chatbot:", responses["bye"])
        break
    else:
        print("Chatbot: I'm sorry, I didn't understand your query.")
