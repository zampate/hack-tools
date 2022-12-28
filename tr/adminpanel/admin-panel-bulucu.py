#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print('''

 $$$$$$\        $$\               $$\                 $$$$$$$\                               $$\       $$$$$$$\            $$\                               
$$  __$$\       $$ |              \__|                $$  __$$\                              $$ |      $$  __$$\           $$ |                              
$$ /  $$ | $$$$$$$ |$$$$$$\$$$$\  $$\ $$$$$$$\        $$ |  $$ |$$$$$$\  $$$$$$$\   $$$$$$\  $$ |      $$ |  $$ |$$\   $$\ $$ |$$\   $$\  $$$$$$$\ $$\   $$\ 
$$$$$$$$ |$$  __$$ |$$  _$$  _$$\ $$ |$$  __$$\       $$$$$$$  |\____$$\ $$  __$$\ $$  __$$\ $$ |      $$$$$$$\ |$$ |  $$ |$$ |$$ |  $$ |$$  _____|$$ |  $$ |
$$  __$$ |$$ /  $$ |$$ / $$ / $$ |$$ |$$ |  $$ |      $$  ____/ $$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |      $$  __$$\ $$ |  $$ |$$ |$$ |  $$ |$$ /      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |$$ |  $$ |      $$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |$$ |$$ |  $$ |      $$ |     \$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      $$$$$$$  |\$$$$$$  |$$ |\$$$$$$  |\$$$$$$$\ \$$$$$$  |
\__|  \__| \_______|\__| \__| \__|\__|\__|  \__|      \__|      \_______|\__|  \__| \_______|\__|      \_______/  \______/ \__| \______/  \_______| \______/ 
                                                                                                                                                                                                                                                                                                                                                                    
  ''')

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("data.txt","r");
	link = raw_input("Site linki giriniz \n(örnek: www.örnek.com ): ")
	print "\n\nUygun linkler : \n"
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
			print "Bulundu => ",req_link

findAdmin()
