import discord 
from discord.ext import commands
import asyncio
from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="Type $ready to start!"))
	print('Bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	print('--------------------------')
	
@bot.command() #Ready command
async def ready(ctx):
	await ctx.send('I\'m a bot made by Michkaro. Here are my main commands:\
	ping - shows you my ping,\
	8ball - ask a question and I\'ll look into my ball to see if it\'s true or false. \
I\'m still being upgraded so you\'ll have to wait for now.')

@bot.command() #Ping command
async def ping(ctx):
	await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
	
@bot.command()
async def announce(ctx, *, arg):
	await ctx.send(arg)
	
	
@bot.command()
async def Hello():
	await bot.say('Hey!')
	
@bot.command() #Info about player
async def info(ctx, *, member: discord.Member):
	fmt = '{0} joined on {0.joined.on} and has {1} roles'
	await ctx.send(fmt.format(member, len(member.roles)))

@info.error
async def info_error(ctx, error):
	if insistance (error, commands.BadArgument):
		await ctx.send('I could not find the user...')

bot.run(token)


	


	
	
	





	










