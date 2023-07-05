import openai
from pprint import pprint as pp

initial_prompt_message = "You are an AI assistant implementing the SMART framework, ask five separate questions, one at a time, to create study goals and recommendations for students to complete the module. If the answer is not related to the course content, reply with 'please answer the question'. "

initial_response = "Hi! I am a StudyPlanning Bot. I will help you develop your learning goals towards creative technology education and provide you with a personalised study recommendation. However, please do remember that I am a bot and I am still learning. My recommendation is suggestive and you should always think about your own learning goals and what you want to achieve. " 


class ChatGPTClient:
    def __init__(self, openai_api_key) -> None:
        self.messages = []
        openai.api_key = openai_api_key
    
    def make_chatgpt_request(self, history) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history,
            temperature=0.9,
            max_tokens=150 #200? 
        )
        return response['choices'][0]['message']['content']
    
    def start_conversation(self, user_message: str) -> str:
        self.messages = []
        
        self.messages.append({"role": "assistant", "content": initial_prompt_message}) #first message to initiate conversation 
        self.messages.append({"role": "user", "content": user_message}) #user input 
        self.messages.append({"role": "system", "content": initial_response}) 
        
        return initial_response
    
    def get_response(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})
        response = self.make_chatgpt_request(self.messages)
        self.messages.append({"role": "assistant", "content": response})
        return response 
