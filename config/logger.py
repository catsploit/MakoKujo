#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.colors import *
import datetime
import os


class Logger_custom:
	def __init__(self):
		pass

	def msg(self, level, message):
		timestamp = datetime.datetime.now().strftime('%H:%M:%S %p')

		level_color_dict = {'INFO': lcyan,
					   		'WARN': lyellow,
					   		'ERROR': lred}

		level_color = level_color_dict.get(level)
		level_formatt = f'{level_color}{level}'

		output_message = "{2}({4}) [ {0} {2}] {3}{1}".format(level_formatt, message, lblack, white, timestamp)
		return print(output_message)
