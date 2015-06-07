import requests 

def download(url):
	r = requests.get(url) 
	with open(url.split("/")[-1], "wb") as code:
		code.write(r.text)

import openanything

import urllib2
 

if __name__=='__main__':
	fd = open("../data/apk_down", "w")	
	for url in file("../data/apk_link.txt"):
		a = openanything.get(url.strip()) + "\n"
		fd.write(a)
	fd.close()
