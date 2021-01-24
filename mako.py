#!/usr/bin/python3
#-*- coding:utf-8 -*-

import datetime
import discord
import logging
import re

from config.logger import Logger_custom
from discord.ext import commands
from urllib import request, parse

# - Setting up - #
bot = commands.Bot(command_prefix='.', description='Community bot made by @catsploit')
log = logging.getLogger('discord')
log.setLevel(logging.WARNING)

# - Personal logger - #
logger = Logger_custom()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('(%(asctime)s) > [%(levelname)s]: %(message)s'))
log.addHandler(handler)

# - Commands - #
@bot.command()
async def ping(ctx): #parse a context, async for not waiting bot proccess
	await ctx.send('Pong!')


@bot.command()
async def stats(ctx):
	embed = discord.Embed(title=f"{ctx.guild.name}'s stats", 
						 description='',
						 timestamp=datetime.datetime.utcnow(),
						 color=discord.Color.red())

	embed.add_field(name='Server created at', value=f'{ctx.guild.created_at}')
	embed.add_field(name='Owner', value=f'{ctx.guild.owner}')
	embed.add_field(name='ID', value=f'{ctx.guild.id}')
	embed.set_thumbnail(url='https://i.redd.it/eodhd6p0fz051.jpg')

	await ctx.send(embed=embed)


@bot.command()
async def yt(ctx, *, search):
	youtube_url = parse.urlencode({'search_query': search})
	html_response = request.urlopen('http://www.youtube.com/results?' + youtube_url)
	youtube_results = re.findall(r'watch\?v=(\S{11})', html_response.read().decode())

	await ctx.send('https://www.youtube.com/watch?v=' + youtube_results[0])


# - Other functions - #
def read_token(filename='../token.txt'): #1. REPLACE WITH YOUR TOKEN DIRECTORY
	try:
		token = open(filename).read()

	except IOError:
		exit(logger.msg('ERROR', 'token file not found'))

	else:
		return token

# - Events - # 
@bot.event
async def on_ready():
	logger.msg('INFO', 'bot started succesfully')


bot.run(read_token()) #2. OR REPLACE WITH THE ACTUAL TOKEN STRING INSTEAD OF READ_TOKEN FUNC


#Must write a function to get mc servers info by calling apis, minehut etc.
#in the other hand, without an api it must be written by hand doing a
#port scan with nmap or just raw sockets