#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import discord
import logging
import sys

from config.functions.environment import setenvironment
from config.command.statsc import statsfunc
from config.command.mc import mc_minehutscan
from config.command.yt import youtube_search

from config.logger import Logger_custom
from discord.ext import commands

## Setting up
mod_auditory, commands_ch, testing, general, owner, muted, bots, mod = setenvironment()
intents = discord.Intents.default() #ACTIVATE SERVER MEMBERS INTENT IN YOUR BOT
intents.members = True

bot = commands.Bot(command_prefix='.', description='Community bot made by @catsploit', intents=intents)
log = logging.getLogger('discord')
log.setLevel(logging.WARNING)

# - Import external commands - #
bot.load_extension('config.command.mod.mute')
bot.load_extension('config.commandlog')

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
	stadistics = statsfunc(ctx)
	await ctx.send(stadistics)


@bot.command()
async def yt(ctx, *, search):
	response = youtube_search(search)
	await ctx.send(response)


@bot.command()
async def mc(ctx, server, channels=[commands_ch, testing, general]):
	if str(ctx.channel) in channels:
		mc_info = request_api('https://api.minehut.com/server/', server, byname=0)

		try:
			if mc_info['ok'] == False:
				error = "`[server not found]`"	
				await ctx.send(error)

		except KeyError:
			results = mc_minehutscan(mc_info)
			await ctx.send(results[0])


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