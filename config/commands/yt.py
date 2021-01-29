#!/usr/bin/python3
#-*- coding:utf-8 -*-

from urllib import request, parse
import re


def youtube_search(search):
	url = parse.urlencode({'search_query': search})
	response = request.urlopen('http://www.youtube.com/results?' + url)
	results = re.findall(r'watch\?v=(\S{11})', response.read().decode())

	return f'https://www.youtube.com/watch?v={results[0]}'
