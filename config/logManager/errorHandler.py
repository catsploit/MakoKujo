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
		if hasattr(ctx.command, 'on_error'):
			return

		command = ctx.cog 
		if command:
			if command._get_overridden_method(command.cog_command_error):
				return

		ignored = (commands.CommandNotFound, commands.MissingPermissions)
		error = getattr(error, 'original', error)

		if isinstance(error, ignored):
			return

		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Missing required argument :/')

		elif isinstance(error, commands.BadArgument):
			await ctx.send('Could not find that sorry :(')

		elif isinstance(error, commands.errors.NSFWChannelRequired):
			await ctx.send('Use this in NSFW channels you fucking pervert')

		else:
			LoggerHandler.msg('WARN', f'Exception raised in command "{ctx.command}" ({error}):')
			traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
	bot.add_cog(commandErrorHandler(bot))