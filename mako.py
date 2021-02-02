#!/usr/bin/python3
#-*- coding:utf-8 -*-

import requests
import discord
import logging

from config.functions.environment import setenvironment
from config.logevents.logger import Logger_custom
from discord.ext import commands

## Setting up
mod_auditory, commands_ch, testing, general, owner, muted, bots, mod = setenvironment()
intents = discord.Intents.default() #ACTIVATE SERVER MEMBERS INTENT IN YOUR BOT
intents.members = True

bot = commands.Bot(command_prefix='.', description='Community bot made by @catsploit', intents=intents)
log = logging.getLogger('discord')
log.setLevel(logging.WARNING)

# - Import external commands - #
bot.load_extension('config.command.specialties.specialties')
bot.load_extension('config.logevents.commandlog')
bot.load_extension('config.command.mod.mute')
bot.load_extension('config.command.fun.fun')
bot.load_extension('config.command.mc.mc')

# - Personal logger - #
logger = Logger_custom()

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('(%(asctime)s) > [%(levelname)s]: %(message)s'))
log.addHandler(handler)


# - Other functions - #
def read_token(filename='../token.txt'): #1. REPLACE WITH YOUR TOKEN DIRECTORY
	token = open(filename).read()
	return token


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