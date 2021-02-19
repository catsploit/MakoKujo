#!/usr/bin/python3
#-*- coding:utf-8 -*-

from urllib import request, parse
from discord.ext import commands
import discord
import re


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def yt(self, ctx, *, search):
		"""usage: .yt <name>"""

		url = parse.urlencode({'search_query': search})
		response = request.urlopen('http://www.youtube.com/results?' + url)
		results = re.findall(r'watch\?v=(\S{11})', response.read().decode())

		await ctx.send(f'https://www.youtube.com/watch?v={results[0]}')


def setup(bot):
	bot.add_cog(Fun(bot))
