from dotenv import load_dotenv
from discord_api import DiscordClient
from chatgpt import ChatGPTClient
import os

from chatgpt import ChatGPTClient

load_dotenv() # Load .env file

discord_api_key = os.getenv('DISCORD_API_KEY') # Get token from .env file
openai_api_key = os.getenv('CHATGPT_API_KEY') # Get token from .env file

if __name__ == '__main__':
    chatgpt_client = ChatGPTClient(openai_api_key)
    discord_client = DiscordClient(chatgpt_client)
    
    discord_client.run(discord_api_key)
    