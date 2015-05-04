#encoding utf-8
import requests,json
from time import *

#upload apk file
def upload(filename):
	url = 'http://m.qq.com/security_lab//upload_file.jsp'
	files = {'file': open('jimm.apk', 'rb'), 'type': 'apk'}
	r = requests.post(url, files=files)
	text = r.text
	apk_name = text.split(";")[0].split("\"")[-2] 
	return apk_name

#check status
def check_status(apk_name):
	url = 'http://m.qq.com/security_lab//check_state_json.jsp'
	data = {'type':'apk', 'data':apk_name.split(".")[0]}
	i = 0
	while i < 10:
		r = requests.post(url, data=data)
		if "\"1\"" in r.text:
			return True
		i += 1
		sleep(0.5)
	return False

#get result
def check_result(apk_name):
	url = 'http://m.qq.com/security_lab//check_result_json.jsp'
	data = {'type':'apk', 'data':apk_name.split(".")[0]}
	r = requests.post(url, data=data)
	return r.text


def check():
	apk_name = upload("jimm.apk")
	if check_status(apk_name):
		print check_result(apk_name)
	else:
		print "ERROR"

if __name__ == "__main__":
	check()
