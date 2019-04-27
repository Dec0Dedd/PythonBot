import discord 
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
	print('Bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('--------------------------')

@bot.command(pass_context=True)
async def ping():
	await bot.say('Pong!')
	
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
	
    role=discord.utils.get(ctx.message.server.roles,name='Muted')	
	
    await bot.add_roles(target,role)

@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    await bot.send_message(target,'You got warned!!')
	
@bot.command(pass_context = True)
async def kick(ctx,target:discord.Member):
	await bot.kick(target)

@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
	await bot.ban(target)


bot.run('NTcxMzk4MjE5OTU1OTYxODU2.XMQP4w.1cv3VyIOS20LACtNU-SCZ__6Q5I')
