#!/usr/bi/python3
#-*- coding:utf-8 -*-

from discord.ext import commands
import requests


class Specialties(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def ping(self, ctx):
		await ctx.send('Pong!')


	@commands.command()
	async def stats(self, ctx):
		await ctx.send(f"""```css
		> {ctx.guild.name}'s stats
		I=================================================I
		[Server created at] => {ctx.guild.created_at.strftime('%H:%M:%S %p')}
		[Members]           => {len([m for m in ctx.guild.members if not m.bot])}
		[Owner]             => {ctx.guild.owner}
		[SERVER_ID]         => {ctx.guild.id}
		I=================================================I
		```""")


def setup(bot):
	bot.add_cog(Specialties(bot))


#Note: have to test if asynchronous tasks like requests work here
#pls work im tired i need to sleep