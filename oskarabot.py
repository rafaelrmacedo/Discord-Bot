import emoji
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            print(emoji.emojize(f'{member}, você está atrasado para a reunião, meu caro :wine_glass::moyai:'))

client = MyClient()
client.run('your discord bot token goes here')