#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.colors import *
import datetime


class Logger_custom:
	def __init__(self):
		#self.actual_time = actual_time
		pass

	def msg(self, level, message):
		#from config.colors import lcyan, lyellow, lred, lblack, white
		actual_time = datetime.datetime.now().strftime('%H:%M:%S %p')

		level_color_dict = {'INFO': lcyan,
					   		'WARN': lyellow,
					   		'ERROR': lred}

		level_color = level_color_dict.get(level)
		level_formatt = f'{level_color}{level}'

		output_message = "{2}({4}) [ {0} {2}] {3}{1}".format(level_formatt, message, lblack, white, actual_time)
		return print(output_message)