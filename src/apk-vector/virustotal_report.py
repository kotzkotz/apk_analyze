import requests,time,glob,simplejson

def report():
	apikey = "5f0de8a30a0d0d0524260079cbd9c87936d3bf92432bdbd3120f45bdb50b557e"
	url = "https://www.virustotal.com/vtapi/v2/file/report"
	data = file("../data/result.1227").read().split("\n")
	for line in data:
		[filename , json]  = line.split("\t")
		if not "permalink" in json:
			fd = open("../data/report.1227", "a")
			fd.write("%s\t%s\n" %(filename, "NULL"))
			fd.close()
			continue
		dict = simplejson.loads(json)
		md5 =  dict["md5"]
		data = {"resource": md5, 
			"apikey": apikey}
		try:
			report_data = requests.post(url, data = data).text
		except:
			continue
		fd = open("../data/report.1227", "a")
		fd.write("%s\t%s\n" %(filename, report_data))
		fd.close()		
		time.sleep(60)

#print "DOWNLOAD REPORT START"
#report()
#print "DONE"

def read_report(filename):
	report = "../data/report.1227"
	for l in file(report).read().split("\n"):
		if len(l.split("\t")) != 2:
			continue
		json = l.split("\t")[1]
		if json == "NULL":
			return "NULL"
		d = simplejson.loads(json)
		return d["total"] , d["positives"]
	return -1,-1

scan_list = ['Bkav', 'MicroWorld-eScan', 'nProtect', 'CMC', 'CAT-QuickHeal', 'ALYac', 'Malwarebytes', 'VIPRE', 'AegisLab', 'TheHacker', 'BitDefender', 'K7GW', 'K7AntiVirus', 'NANO-Antivirus', 'F-Prot', 'Symantec', 'Norman', 'TotalDefense', 'TrendMicro-HouseCall', 'Avast', 'ClamAV', 'Kaspersky', 'Alibaba', 'Agnitum', 'ViRobot', 'Rising', 'Ad-Aware', 'Sophos', 'Comodo', 'F-Secure', 'DrWeb', 'Zillya', 'TrendMicro', 'McAfee-GW-Edition', 'Emsisoft', 'Cyren', 'Jiangmin', 'Kingsoft', 'Microsoft', 'SUPERAntiSpyware', 'AhnLab-V3', 'GData', 'ByteHero', 'McAfee', 'AVware', 'VBA32', 'Panda', 'Zoner', 'ESET-NOD32', 'Tencent', 'Ikarus', 'Fortinet', 'AVG', 'Baidu-International', 'Qihoo-360', 'Antiy-AVL', 'Avira']
def read_report2():
	di = {}
	report = "../data/report.1227"
	sd = []
	for l in file(report).read().split("\n"):
		if len(l.split("\t")) != 2:
			continue
		json = l.split("\t")[1]
		filename = l.split("\t")[0]
		if json == "NULL":
			continue
		d = simplejson.loads(json)
		if d["response_code"] == -1:continue
		m = d["scans"]	
		result_list = ""
		for i in scan_list:
			if not i in m:
				result_list += "2"#not scanned
			elif m[i]["detected"] == True:
				result_list += "1"#positive
			else:
				result_list += "0"#negetive
		#print result_list
		di[filename]  = result_list + "\t" + str(d["total"]) + "\t"+ str(d["positives"])
	return di
