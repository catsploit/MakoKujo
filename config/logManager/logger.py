#!/usr/bin/python3
#-*- coding:utf-8 -*-

from config.colors import *
import datetime


class LoggerHandler:
	def __init__(self):
		pass


	@staticmethod
	def msg(level, message):
		timestamp = datetime.datetime.now().strftime('%H:%M:%S %p')
		levelstatus = {'INFO': lcyan,
					   'WARN': lyellow,
					   'ERROR': lred}

		levelstr = f'{levelstatus.get(level)}{level}'
		return print(f'{lblack}({timestamp}) [ {levelstr + lblack} ] {white + message}')