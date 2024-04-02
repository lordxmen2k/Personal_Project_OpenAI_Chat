import os
import openai

openai.api_key = os.getenv("OPENAI_SECRET_KEY")


class ChatApp:
    def __init__(self):
        # API Key is set via an environment variable for better security practices
        if not openai.api_key:
            raise ValueError("The OPENAI_SECRET_KEY environment variable is not set.")
        self.conversation_history = [{"role": "system", "content": "You are a helpful assistant."}]

    def send_message(self, user_message):
        # Add the user message to the conversation history
        self.conversation_history.append({"role": "user", "content": user_message})

        try:
            # Call OpenAI API
            response = openai.chat.completions.create(model="gpt-3.5-turbo",
            messages=self.conversation_history,max_tokens=50)
            # Get the assistant's latest message
            # The structure of the response object might vary; 
            # please adjust the following line according to the actual response structure:
            assistant_message = response.choices[0].message.content

            # Add the assistant message to the conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_message})

            return assistant_message
        except Exception as e:
            print(f"An error occurred while connecting to OpenAI API: {e}")
            return "I'm unable to connect to the AI right now."