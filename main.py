import discord
from datetime import datetime



class MyClient(discord.Client):
    time_since = datetime.now()
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        if message.content == "&time":
            td = abs(self.time_since - datetime.now())
            since = (td.seconds//60)
            await message.channel.send("We lasted {} minutes and counting. Congrats!".format(since))
       
        if 'lick' in message.content.lower() and message.author != self.user:
            auth = message.author
            td = abs(self.time_since - datetime.now())
            since = (td.seconds//60)%60
            await message.channel.send("We lasted {} minutes without licking someone. Way to go {}!".format(since, auth))
            time_since = datetime.now()

print(datetime.now())
client = MyClient()

client.run('InsertBotKeyHere')