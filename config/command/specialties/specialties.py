#!/usr/bi/python3
#-*- coding:utf-8 -*-

from discord.ext import commands
import requests
import os


class Specialties(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def ping(self, ctx):
		await ctx.send('Pong!')


	@commands.command()
	async def stats(self, ctx):
		"""usage: .stats (show server stadistics (members, id, etc))"""

		await ctx.send(f"""```css
		> {ctx.guild.name}'s stats
		I=================================================I
		[Server created at] => {ctx.guild.created_at.strftime('%H:%M:%S %p')}
		[Members]           => {len([m for m in ctx.guild.members if not m.bot])}
		[Owner]             => {ctx.guild.owner}
		[SERVER_ID]         => {ctx.guild.id}
		I=================================================I
		```""")


	@commands.command()
	async def help(self, ctx):
		cogs = self.bot.cogs
		general_chain = ""
		mod_chain = ""

		for cmd in self.bot.walk_commands():
			if cmd.help is None:
				continue

			if cmd.help.startswith('MODS ONLY'):
				mod_chain += '{0.name:<10} : {0.help}\n\t\t'.format(cmd)

			else:
				general_chain += '{0.name:<10} : {0.help}\n\t\t'.format(cmd)

		string = f"""```css
		[Commands]

		GENERAL
		-------
		{general_chain}
		MOD
		---
		{mod_chain}
		```"""
		await ctx.send(string)


def setup(bot):
	bot.add_cog(Specialties(bot))