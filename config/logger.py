#!/usr/bin/python3
#-*- coding:utf-8 -*-


class Logger_custom:
	def __init__(self):
		pass

	def msg(self, level, message):
		from config.colors import lcyan, lyellow, lred, lblack, white

		level_color_dict = {'INFO': lcyan,
					   		'WARN': lyellow,
					   		'ERROR': lred}

		level_color = level_color_dict.get(level)
		level_formatt = f'{level_color}{level}'

		output_message = "{2}[ {0} {2}] {3}{1}".format(level_formatt, message, lblack, white)
		return print(output_message)