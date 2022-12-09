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

client = MyClient('intents')
client.run('MTA1MDc0Nzg4NTc4NTk4OTE1MQ.G1ngIR.P-qy6Ic5Bea06pcKxga8DNjchUqiepNiPeU2pw')