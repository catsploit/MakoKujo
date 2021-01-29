#!/usr/bin/python3
#-*- coding:utf-8 -*-


def statsfunc(ctx):
	created_at = ctx.guild.created_at.strftime('%H:%M:%S %p')
	members = len([m for m in ctx.guild.members if not m.bot])

	stats_string = f"""```css
	> {ctx.guild.name}'s stats
	I=================================================I
	[Server created at] => {created_at}
	[Members]           => {members}
	[Owner]             => {ctx.guild.owner}
	[SERVER_ID]         => {ctx.guild.id}
	I=================================================I
	```"""

	return stats_string