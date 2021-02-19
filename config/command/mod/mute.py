#!/usr/bin/python3
#-*- coding:utf-8 -*-

from discord.ext import commands
from discord.member import Member
from config.functions.getValue import getvalue
from config.logManager.commandLog import CommandLog


class Mute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def mute(self, ctx, member : Member, reason='no specified'):
		"""MODS ONLY: .mute <user> <reason(optional)>"""

		mute = ctx.guild.get_role(getvalue()['rol_aliasses']['muted'])
		await member.add_roles(mute)

		# Log
		await ctx.send(f'**{member}** has been _muted_ by **{ctx.message.author}**')
		await ctx.invoke(self.bot.get_command('log'), to=member, why=reason, action=type(self).__name__)


	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def unmute(self, ctx, member : Member):
		"""MODS ONLY: .unmute <user>"""

		mute = ctx.guild.get_role(getvalue()['rol_aliasses']['muted'])
		await member.remove_roles(mute)

		# Log
		await ctx.send(f'**{member}** has been _unmuted_ by **{ctx.message.author}**')


def setup(bot):
	bot.add_cog(Mute(bot))