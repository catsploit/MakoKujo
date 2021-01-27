#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import discord
import logging
import re

from config.commands.mc import mc_minehutscan
from config.logger import Logger_custom
from discord.ext import commands
from urllib import request, parse

# - Setting up - #
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description='Community bot made by @catsploit', intents=intents)
log = logging.getLogger('discord')
log.setLevel(logging.WARNING)

# - ch. Aliasses - #
general = "¥-𝙜𝙚𝙣𝙚𝙧𝙖𝙡-¥"
commands = "ß-𝙘𝙤𝙢𝙖𝙣𝙙𝙤𝙨-ß" 
testing  = "testing-chat"

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
	stats_string = f"""```css
	> {ctx.guild.name}'s stats
	I=================================================I
	[Server created at] => {ctx.guild.created_at.strftime('%H:%M:%S %p')}
	[Owner]             => {ctx.guild.owner}
	[SERVER_ID]         => {ctx.guild.id}
	[Members]           => {ctx.guild.member_count}
	I=================================================I
	```"""

	await ctx.send(stats_string)


@bot.command()
async def yt(ctx, *, search):
	youtube_url = parse.urlencode({'search_query': search})
	html_response = request.urlopen('http://www.youtube.com/results?' + youtube_url)
	youtube_results = re.findall(r'watch\?v=(\S{11})', html_response.read().decode())

	logger.msg('INFO', f"searched '{search}' by {ctx.author}")
	await ctx.send('https://www.youtube.com/watch?v=' + youtube_results[0])


@bot.command()
async def mc(ctx, server, channels=[commands, testing, general]):
	if str(ctx.channel) in channels:
		author = ctx.author
		mc_info = request_api('https://api.minehut.com/server/', server, author, byname=0)

		try:
			if mc_info['ok'] == False:
				error = "`[request failed with api.minehut.com]`"	
				await ctx.send(error)

		except KeyError:
			results = mc_minehutscan(mc_info)
			await ctx.send(results[0])
			await ctx.send(results[1])


# - Other functions - #
def read_token(filename='../token.txt'): #1. REPLACE WITH YOUR TOKEN DIRECTORY
	token = open(filename).read()
	return token


def request_api(url, arg, author, byname=1):
	keyword = ['?byName=true', '']

	request = requests.get(url + arg + keyword[byname])
	json_response = request.json()
	logger.msg('INFO', f'requested {url} from {author}')

	return json_response


# - Events - # 
@bot.event
async def on_ready():
	logger.msg('INFO', 'bot started succesfully')


@bot.event
async def on_connect():
	logger.msg('INFO', f'logged in as {bot.user.name} ID:{bot.user.id}')


if __name__ == '__main__':
	try:
		bot.run(read_token()) #2. OR REPLACE WITH THE ACTUAL TOKEN STRING INSTEAD OF READ_TOKEN FUNC

	except IOError:
		exit(logger.msg('ERROR', 'token file not found'))