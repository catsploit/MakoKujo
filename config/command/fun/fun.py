#!/usr/bin/python3
#-*- coding:utf-8 -*-

from urllib import request, parse
from NHentai import NHentai
from discord.ext import commands
import discord
import re


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def yt(self, ctx, *, search):
		url = parse.urlencode({'search_query': search})
		response = request.urlopen('http://www.youtube.com/results?' + url)
		results = re.findall(r'watch\?v=(\S{11})', response.read().decode())

		await ctx.send(f'https://www.youtube.com/watch?v={results[0]}')




	#@commands.is_nsfw()
	@commands.group()
	async def nhentai(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('GIMME ARGUMENT >:( usage: nhentai <[search, random, homepage]>')


	@nhentai.command()
	async def search(self, ctx, *, search : str):
		nhentai = NHentai()
		if not search.isnumeric():
			douj = nhentai.search(query=search, sort='popular', page=1)
			if douj.total_results == 0:
				raise commands.BadArgument

			search = douj.doujins[0].id

		douj = nhentai._get_doujin(id=str(search))
		if douj is None:
			raise commands.BadArgument

		embed = discord.Embed(title=f'{douj.title}', 
			                  url=f'https://nhentai.net/g/{douj.id}',
			                  color=discord.Color.lighter_grey(),
			                  description=f"""
			                  **[id]**       : {douj.id}
			                  **[Pages]**    : {douj.total_pages}
			                  **[Language]** : {douj.languages[0]}
			                  **[Parodies]** : {douj.parodies}
			                  **[Author]**   : {douj.artists[0]}""")

		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.add_field(name='Characters', value=f"{', '.join(douj.characters)}", inline=False)
		embed.set_thumbnail(url=douj.images[0])

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Fun(bot))
