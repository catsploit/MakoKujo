#!/usr/bin/python3
#-*- coding:utf-8 -*-

import json
import pickle

def getvalue():
	with open('config/environment.json') as file:
		return json.load(file)