#!/usr/bin/python3 
#-*- coding:utf-8 -*-

from config.functions.getenvvalue import getvalue
from discord.ext import commands


class CommandLog(commands.Cog):
	def __init__(self, bot):
		self.auditory = getvalue()['channel_aliasses']['mod_auditory'] 
		self.bot = bot
	
	@commands.command()
	@commands.has_role(getvalue()['rol_aliasses']['bots'])
	async def log(self, ctx, *, to, why, action): 
		channel = self.bot.get_channel(self.auditory)
		await channel.send(f"""```css
							> Infraction
							I======================I
							[Action]   => {action}
							[Affected] => {to}
							[Author]   => {ctx.message.author}
							[Reason]   => {why}
							```""")

def setup(bot):
	bot.add_cog(CommandLog(bot))