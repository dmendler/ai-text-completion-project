# AI Text-Completion App

*Danny Mendler*

This Command-Line AI Text-Completion App in Python allows you to send prompts to an Generative AI model (Cohere) like you would on their website (like sending a prompt on ChatGPT's website). You can specifiy the temperature (creativness) and max_tokens (response length) before sending prompts to the model.

To run this app, first you need to install some dependencies:
> To install cohere:
>> python -m pip install cohere --upgrade
>
> You will also need to create an account on Cohere's website and use their trial API key (found under API Keys tab):
> > [Cohere Website](https://cohere.com/)
>
> You can create a .env file and define COHERE_API_KEY, or you can hardcode the API key to the API_KEY variable.
>
> If you use the .env method, you will need to install:
>> pip install python-dotenv

You can easily run the script by typing in the command line:
>  python ./text_completion_app.py 
