import emoji
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "m!", case_insensitive = True, intents=intents)

client.remove_command('help')

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = print(emoji.emojize(f'{member}, você está atrasado para a reunião, meu caro :wine_glass: :moyai:'))
            await guild.system_channel.send(message)

client.run('MTA1MDc0Nzg4NTc4NTk4OTE1MQ.GiZFwl.Opf6Aq5zOuyG8vm_zTGqwR_0hsge8ID--hqy18')