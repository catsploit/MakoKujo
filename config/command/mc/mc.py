#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.functions.getenvvalue import getvalue
from discord.ext import commands
import requests


class Mc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.chn = getvalue()['channel_aliasses']['commands_ch']


	@commands.command()
	async def mc(self, ctx, server):
		if ctx.channel.id == self.chn:
			mc_info = Mc.request_api(api='https://api.minehut.com/server/', arg=server, keywrd=1)
			if mc_info.get('ok') != None:
				ctx.send(Mc.minehutscan(mc_info))

			else:
				await ctx.send('**Error: server not found in api.minehut**')


	@staticmethod
	def request_api(api, arg, keywrd : int):
		keyword = ['', '?byName=true']
		with session.get(api + arg + keyword[keywrd]) as response:
			return response.json()


	@classmethod
	def minehutscan(cls, json):
		fields = mc_info['server']

		activity = str(fields['online'])
		backups = str(fields['backup_slots'])
		online = str(fields['playerCount'])
		owner = str(fields['owner'])
		_max = str(fields['maxPlayers'])
		motd = str(fields['motd'])
		_id = str(fields['_id'])

		return f"""```css
				{motd:^10}
				I===========================================================I
				Online players    : {online} / {_max}
				Owner Minehut ID  : {owner}
				Server Minehut ID : {_id}
				Activity:         : {activity}
				Backups           : {backups}
				I===========================================================I
				```"""


def setup(bot):
	bot.add_cog(Mc(bot))