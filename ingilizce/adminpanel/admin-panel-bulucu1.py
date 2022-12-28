#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print('''


▄▀█ █▀▄ █▀▄▀█ █ █▄░█   █▀█ ▄▀█ █▄░█ █▀▀ █░░   █▀▀ █ █▄░█ █▀▄ █▀▀ █▀█
█▀█ █▄▀ █░▀░█ █ █░▀█   █▀▀ █▀█ █░▀█ ██▄ █▄▄   █▀░ █ █░▀█ █▄▀ ██▄ █▀▄
                                                                                                                                                                                                                                                                                                                                                                    
  ''')

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("data.txt","r");
	link = raw_input("Enter site link \n(example: www.example.com ): ")
	print "\n\nAppropriate Links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Found => ",req_link

findAdmin()
