#!/usr/bin/python3
#-*- coding:utf-8 -*-

import discord
from discord.ext import commands


class Chat(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.has_permissions(manage_messages=True)
	@commands.command()
	async def clear(self, ctx, amount : int):
		"""MODS ONLY: .clear <amount> (clean <amount> messages)"""
		
		await ctx.channel.purge(limit=amount)


def setup(bot):
	bot.add_cog(Chat(bot))
