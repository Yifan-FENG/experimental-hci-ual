from dotenv import load_dotenv 
import os 
import chatgpt
from pprint import pprint as pp


load_dotenv() # Load .env file 

chatgpt.api_key = os.getenv('ChatGPT_API_KEY') # Get token from .env file

initial_prompt_message = "You are a AI asisstant for developing study goals for online education student by implementing SMART framework."
initial_response = "Hi! I am a StudyPlanning Bot. I will help you develop your learning goals towards creative technology education and provide you with a personalised study recommendation. However, please do remember that I am a bot and I am still learning. My recommendation is suggestive and you should always think about your own learning goals and what you want to achieve. " 

class ChatGPTClient:
    def __init__(self) -> None:
        self.messages = []
    
    def make_chatgpt_request(self, history):
        response = chatgpt.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history,
            temperature=0.9,
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    
    def start_conversation(self, user_input):
        self.messages = []
        
        self.messages.append({"role": "assistant", "content": initial_prompt_message})
        self.messages.append({"role": "user", "content": user_input})
        self.messages.append({"role": "system", "content": initial_response})
        
        return initial_response
    
    def get_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = self.make_chatgpt_request(self.messages)
        self.messages.append({"role": "assistant", "content": response})
        return response
