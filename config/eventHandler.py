#!/usr/bin/python3
#-*- coding:utf-8 -*-

from discord.ext import commands
from config.logManager.logger import LoggerHandler

class Events(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.logger = LoggerHandler()

	@commands.Cog.listener()
	async def on_connect(self):
		self.logger.msg('INFO', f'logged in as {self.bot.user.name} ID:{self.bot.user.id}')


	@commands.Cog.listener()
	async def on_ready(self):
		self.logger.msg('INFO', 'bot started succesfully')


def setup(bot):
	bot.add_cog(Events(bot))