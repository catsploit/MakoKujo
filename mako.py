#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
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
	stats_string = f"""```css
	> {ctx.guild.name}'s stats
	I=================================================I
	[Server created at] => {ctx.guild.created_at}
	[Owner]             => nick.sh
	[SERVER_ID]         => {ctx.guild.id}
	I=================================================I
	```"""

	await ctx.send(stats_string)


@bot.command()
async def yt(ctx, *, search):
	youtube_url = parse.urlencode({'search_query': search})
	html_response = request.urlopen('http://www.youtube.com/results?' + youtube_url)
	youtube_results = re.findall(r'watch\?v=(\S{11})', html_response.read().decode())

	await ctx.send('https://www.youtube.com/watch?v=' + youtube_results[0])


@bot.command()
async def mc(ctx, server):
	mc_info = request_api('https://api.minehut.com/server/', server, byname=0) #Minehut api request
	try:
		if mc_info['ok'] == False:
			error = """```css
			[request failed with api.minehut.com]```"""	
			await ctx.send(error)

	except KeyError:
		server_motd = str(mc_info['server']['motd'])
		server_online = str(mc_info['server']['playerCount'])

		response = f"""```css
					[{server_motd:^10}]
					I===========================================================I
					Online players : {server_online}
					I===========================================================I
					```"""

		await ctx.send(response)


# - Other functions - #
def read_token(filename='../token.txt'): #1. REPLACE WITH YOUR TOKEN DIRECTORY
	token = open(filename).read()
	return token


def request_api(url, arg, byname=1):
	keyword = ['?byName=true', '']

	request = requests.get(url + arg + keyword[byname])
	json_response = request.json()

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