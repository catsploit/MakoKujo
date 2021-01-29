#!/usr/bin/python3
#-*- coding: utf-8 -*-


def read_properties(server_properties):
	string = ""

	for field, field_value in server_properties.items():
		line = f"{field:<30} : {str(field_value)}\n"
		string += line

	formatted_str = f"""```fix
			[server_properties.txt]
			{string}
			 ```"""

	return formatted_str


def mc_minehutscan(mc_info):
	server_properties = read_properties(mc_info['server']['server_properties'])
	fields = mc_info['server']

	backups = str(fields['backup_slots'])
	online = str(fields['playerCount'])
	activity = str(fields['online'])
	_max = str(fields['maxPlayers'])
	owner = str(fields['owner'])
	motd = str(fields['motd'])
	_id = str(fields['_id'])

	info = f"""```css
				{motd:^10}
				I===========================================================I
				Online players    : {online} / {_max}
				Owner Minehut ID  : {owner}
				Server Minehut ID : {_id}
				Activity:         : {activity}
				Backups           : {backups}
				I===========================================================I
				```"""

	response = [info, server_properties]
	return response
