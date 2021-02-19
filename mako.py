#!/usr/bin/python3
#-*- coding:utf-8 -*-

import discord
import os 
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='.', description='Community bot made by @catsploit', intents=intents)
bot.remove_command('help')

# SET UP HANDLERS
bot.load_extension('config.logManager.commandLog')
bot.load_extension('config.logManager.errorHandler')
bot.load_extension('config.eventHandler')


# ADD COGS
for filename in os.listdir('config/command/'):
	for module in os.listdir(f'config/command/{filename}'):
		if module.endswith('.py'):
			bot.load_extension(f'config.command.{filename}.{module[:-3]}')


def read_token(filename='../token.txt'):
	token = open(filename).read()
	return token


if __name__ == '__main__':
	try:
		bot.run(read_token())

	except IOError:
		exit(logger.msg('ERROR', 'token file not found'))