import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Type $ready to start!"))
	print('Bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('--------------------------')
	
@bot.command()
async def ready(ctx):
	await ctx.send('I\'m a bot mad by Michkaro. Here are my main commands:\
	ping - shows you my ping,\
	8ball - ask a question and I\'ll look into my ball to see if it\'s true or false\
I\'m still being upgraded so you\'ll have to wait for now.')

@bot.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
	
@bot.command()
async def announce(ctx, *, channel, arg):
	await ctx.send(channel, arg)
	
	
@bot.command()
async def Hello():
	await bot.say('Hey mate!')


bot.run('NTcxMzk4MjE5OTU1OTYxODU2.XMQP4w.1cv3VyIOS20LACtNU-SCZ__6Q5I')


	


	
	
	





	










