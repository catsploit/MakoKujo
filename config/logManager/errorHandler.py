#!/usr/bin/python3
#-*- coding:utf-8 -*-

import traceback
import discord
import sys
from discord.ext import commands

from config.logManager.logger import LoggerHandler


class commandErrorHandler(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		channel = ctx.message.channel
		ignored = (commands.CommandNotFound, )

		if isinstance(error, ignored):
			return

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Missing required argument :/')

		elif isinstance(error, commands.BadArgument):
			await ctx.send('Could not find that sorry :(')

		else:
			LoggerHandler.msg('WARN', f'Exception raised in command "{ctx.command}" ({error}):')
			traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
	bot.add_cog(commandErrorHandler(bot))