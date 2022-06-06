import discord
import requests
import Keep_Alive


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if (message.channel.id == int(930829886149500929)):
            if (message.content != ''):
                channel = client.get_channel(int(976396264646258698))
                await channel.send('**'+str(message.author)+'**: '+str(message.content))
        if '>history' in message.content:
            n = int(message.content.split()[1])
            his = [message async for message in message.channel.history(limit=n)]
            for i in his:
                await message.channel.send('**'+str(i.author)+'**:   '+str(i.content))
        if '>getPhotos' in message.content:
            n = int(message.content.split()[1])
            access_Token = 'access-tk-face'
            idGroup = 'id-gr-face'
            data = requests.get("https://graph.facebook.com/v14.0/"+idGroup +
                                "?fields=feed.limit("+str(n)+")%7Bfull_picture%7D&access_token="+access_Token)
            data = data.json()['feed']['data']
            for feed in data:
                try:
                    await message.channel.send(feed['full_picture'])
                except:
                    print("failed")


Keep_Alive.keep_alive()
client = MyClient()
client.run('bot-token')
