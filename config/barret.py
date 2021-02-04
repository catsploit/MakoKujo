#!/usr/bin/python3
#-*- coding:utf-8 -*-

import discord
import datetime

from config.logger import Logger_custom
from discord.ext import commands


# - Logger - #
actual_time = datetime.datetime.now().strftime('%H:%M:%S %p')
logger = Logger_custom(actual_time)
logger.msg('INFO', 'working')