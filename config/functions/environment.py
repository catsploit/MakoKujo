#!/usr/bin/python3
#-*- coding:utf-8 -*-

import json

def setenvironment():
	with open('config/environment.json') as file:
		env =  json.load(file)
		file.close()

	#Channels
	channels = env['channel_aliasses']
	mod_auditory = channels['mod_auditory']
	commands_ch = channels['commands_ch']
	testing = channels['testing']
	general = channels['general']

	#Roles
	roles = env['rol_aliasses']
	owner = roles['owner']
	muted = roles['muted']
	bots = roles['bots']
	mod = roles['mod']

	return mod_auditory, commands_ch, testing, general, owner, muted, bots, mod