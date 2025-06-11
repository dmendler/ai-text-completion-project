import cohere

# load API key from environment variable
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

def get_response(prompt, temp=None, max_tokens=None):
    ''' Function to get response from Cohere API based on user input prompt. '''
    try:
        co = cohere.ClientV2(API_KEY)
        response = co.chat(
            model="command-a-03-2025",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=max_tokens,
        )
        for item in response.message.content:
            if item.type == "text":
                return item.text # Return only the text part of the response
    except Exception as e:
        return f"An error occurred: {e}"

def get_data():
    ''' Function to get temperature and max tokens from user input. '''
    while True:
        try: # check that the input is a digit (not a string)
            temp = input("Enter temperature (0.0 to 1.0, leave blank to omit): ")
            if temp and not temp.replace('.', '', 1).isdigit():
                raise ValueError("Invalid temperature value. Please enter a number between 0.0 and 1.0.")
            max_tokens = input("Enter max tokens (leave blank to omit): ")
            if max_tokens and not max_tokens.isdigit():
                raise ValueError("Invalid max tokens value. Please enter a positive integer.")
        except ValueError as e:
            print(f"An error occurred: {e}")
            continue
        break
    return temp, max_tokens

def main():
    ''' Main function to run the AI Text Completion App. '''
    print("Welcome to the AI Text Completion App!\n")
    if not API_KEY:
        print("Error: COHERE_API_KEY is not set. Please set it in your environment variables.")
        return
    temp, max_tokens = get_data()

    while True:
        user_input = input("Enter prompt (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break
        if not user_input:
            print("Prompt cannot be empty. Please try again.")
            continue

        print("Response: ", get_response(user_input, temp=float(temp) if temp else None, max_tokens=int(max_tokens) if max_tokens else None))
        print("\n")
    return
if __name__ == "__main__":
    main()