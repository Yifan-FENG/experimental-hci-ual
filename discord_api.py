from pprint import pp
import discord # pip install discord.py 
import re

start_commands = ['/studybot','/edubot']

class DiscordClient(discord.Client):
    def __init__(self, chatgpt_client, *args, **kwargs):
        intents = discord.Intents.default() #create intents 
        intents.message_content = True #create intents message content to true

        super().__init__(*args, **kwargs, intents=intents)
                
        self.chatgpt_client = chatgpt_client
        
    async def on_ready(self):  #print to terminal when bot is successfully connected 
        print('Logged on as: ', self.user)

    async def on_message(self, message): #print content message by client to console 
        print(message.content) 
        if message.author == self.user: 
            return
        
        user_message = None  #check user message
        
        match = re.match(r'^/(studybot|edubot)\s(.*)$', message.content)
        
        response = " "
                
        if (match):
            user_message = match.group(2)
            pp(user_message)
            response = self.chatgpt_client.start_conversation(user_message)
        else:
            user_message = message.content
            response = self.chatgpt_client.get_response(user_message)
            
        await message.channel.send(f"Answer: {response}")
