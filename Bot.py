import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print('Bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	
bot.run('NTcxMzk4MjE5OTU1OTYxODU2.XMQP4w.1cv3VyIOS20LACtNU-SCZ__6Q5I')
