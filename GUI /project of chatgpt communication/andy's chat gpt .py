keys=""

import os

import openai
openai.api_key = "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"

 

def chat_with_ai(user_input):


    # Set the AI's role as a counselor and therapist

    context = "You are an AI therapist and counselor. Help the user with their concerns and provide emotional support and guidance."
    # Combine the context and user input

    prompt = f"{context} User: \"{user_input}\""
    # Request a response from the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.8
    )

 

    # Extract the AI's response

    ai_response = response.choices[0].text.strip()

 

    return ai_response

 

print("Welcome to the AI Counselor!")

print("Type 'exit' to end the session.")

 

while True:

    # Get the user's input

    user_input = input("Andy: ")

 

    # Check if the user wants to exit

    if user_input.lower() == "exit":

        print("Goodbye!")

        break

 

    # Get the AI's response

    ai_response = chat_with_ai(user_input)

 

    # Display the AI's response

    print("Andy's assistance:", ai_response)