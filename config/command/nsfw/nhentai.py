#!/usr/bin/python3
#-*- coding:utf-8 -*-

import discord
from NHentai import NHentai
from discord.ext import commands
from config.logManager.logger import LoggerHandler


class NhentaiAPI(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	@commands.is_nsfw()
	async def nhentai(self, ctx):
		"""usage: .nhentai [random, home] <name>"""
		
		if ctx.invoked_subcommand is None:
			await ctx.send('GIMME ARGUMENT >:( usage: nhentai <[search, random, homepage]>')


	@nhentai.command()
	async def search(self, ctx, *, search : str):
		nhentai = NHentai()
		if not search.isnumeric():
			douj = nhentai.search(query=search, sort='popular', page=1)
			search = douj.doujins[0].id

		douj = nhentai._get_doujin(id=search)
		for field in [a for a in dir(douj) if not a.startswith('__')]:
			attr = getattr(douj, field)
			if not attr:
				setattr(douj, field, 'empty')

		embed = discord.Embed(title=f'{douj.title}', 
			                  url=f'https://nhentai.net/g/{douj.id}',
			                  color=discord.Color.lighter_grey(),
			                  description=f"""
			                  **[id]**       : {douj.id}
			                  **[Language]** : {douj.languages[0]}
			                  **[Parodies]** : {douj.parodies}
			                  **[Author]**   : {douj.artists[0]}""")

		embed.add_field(name='Characters', value=f"{', '.join(douj.characters)}", inline=False)
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.set_footer(text=f'Pages: {douj.total_pages}')
		embed.set_thumbnail(url=douj.images[0])

		await ctx.send(embed=embed)


	##Local Handlers
	@search.error
	async def nhentai_handler(self, ctx, error):
		error = getattr(error, 'original', error)

		if isinstance(error, discord.HTTPException):
			await ctx.send('Error while formatting embed, call a dev')

		elif isinstance(error, IndexError):
			await ctx.send('Sauce not found :(')

		else:
			LoggerHandler.msg('WARN', f'Exception raised in "nhentai" branch: {error}')


def setup(bot):
	bot.add_cog(NhentaiAPI(bot))