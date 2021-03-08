#!/usr/bin/python3
#-*- coding:utf-8 -*-

import discord
from NHentai import NHentai
from discord.ext import commands
from config.logManager.logger import LoggerHandler


class NhentaiAPI(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.nhentai = NHentai()


	@commands.group()
	@commands.is_nsfw()
	async def nhentai(self, ctx):
		"""usage: .nhentai [random, home] <name>"""
		
		if ctx.invoked_subcommand is None:
			await ctx.send('GIMME ARGUMENT >:( usage: nhentai <[search, random, home]>')


	async def interface(self, ctx, douj):
		embed = discord.Embed(title=douj.title, 
			                  url=f'https://nhentai.net/g/{douj.id}',
			                  color=discord.Color.lighter_grey(),
			                  description=f"""
			                  **ID**       : {douj.id}
			                  **Language** : {douj.languages[0]}
			                  **Parodies** : {douj.parodies}
			                  **Author**   : {douj.artists[0]}""")

		embed.add_field(name='Characters', value=f"{', '.join(douj.characters)}", inline=False)
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.set_footer(text=f'Pages: {douj.total_pages}')
		embed.set_thumbnail(url=douj.images[0])

		return embed


	async def replace_fields(self, ctx, douj):
		for field in [a for a in dir(douj) if not a.startswith('__')]:
			attr = getattr(douj, field)
			if not attr:
				setattr(douj, field, 'empty')

		return douj


	@nhentai.command()
	async def search(self, ctx, *, search : str):
		"""usage: .nhentai search <doujin/number>"""

		if not search.isnumeric():
			douj = self.nhentai.search(query=search, sort='popular', page=1)
			search = douj.doujins[0].id

		douj = self.nhentai._get_doujin(id=search)
		douj = await self.replace_fields(ctx, douj)
		interface = await self.interface(ctx, douj)
		await ctx.send(embed=interface)


	@nhentai.command()
	async def random(self, ctx):
		douj = self.nhentai.get_random()
		interface = await self.interface(ctx, douj)
		await ctx.send(embed=interface)


	@nhentai.command()
	async def home(self, ctx, index : int = 0): 
		douj = self.nhentai.get_pages(page=1).doujins[index]
		embed = discord.Embed(title=douj.title,
							  url=f'https://nhentai.net/g/{douj.id}',
							  color=discord.Color.lighter_grey(),
							  description=f"""
			                  **ID**       : {douj.id}
			                  **Language** : {douj.lang}""")

		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		embed.set_footer(text='Trending right now!')
		embed.set_thumbnail(url=douj.cover)

		await ctx.send(embed=embed)


	##Local Handlers
	@search.error
	async def search_handler(self, ctx, error):
		error = getattr(error, 'original', error)

		if isinstance(error, discord.HTTPException):
			await ctx.send('Error while formatting embed, call a dev')

		elif isinstance(error, IndexError):
			await ctx.send('Sauce not found :(')

		else:
			LoggerHandler.msg('WARN', f'Exception raised in "nhentai search" branch: {error}')


	@random.error
	async def random_handler(self, ctx, error):
		error = getattr(error, 'original', error)

		if isinstance(error, discord.HTTPException):
			await ctx.send('Corrupted doujin :( try again')


def setup(bot):
	bot.add_cog(NhentaiAPI(bot))