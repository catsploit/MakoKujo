#!/usr/bin/python3
#-*- coding:utf-8 -*-

import traceback
import discord
import sys
from discord.ext import commands


class commandErrorHandler(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		ignored = (commands.CommandNotFound, )

		if isinstance(error, ignored):
			return

		else:
			print(f'Exception raised in command "{ctx.command}"', file=sys.stderr)
			traceback.print_exception(type(error), error.__traceback__, file=sys.stderr)


def setup(bot):
	bot.add_cog(commandErrorHandler(bot))