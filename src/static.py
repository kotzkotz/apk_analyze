import os,glob,zipfile,upload

apk_dir = "../../Genome"
permission_list = file("../data/permissions.txt").read().split("\r\n")[:-1]

def dump_a(apk_name):
	try:
		fd = zipfile.ZipFile(apk_name)
	except:
		return -1
	apk_raw_name = apk_name.split("/")[-1].split(".")[0] 
	for file in fd.namelist():
		if file == "AndroidManifest.xml":
			fd.extract(file, "../tmp/"+apk_raw_name)
	fd.close()
	return apk_raw_name

def dump_f(d):
	apk_list = []
	for file in glob.glob(d + "/*.apk"):
		apk_list.append(file)
	return apk_list	

def dump_p(raw_name):
	os.system("java -jar AXMLPrinter2.jar ../tmp/%s/AndroidManifest.xml > ../tmp/%s/And.xml" %(raw_name, raw_name))
	l = ""
	context = file("../tmp/%s/And.xml" %raw_name).read()
	for i in permission_list:
		if i in context:
			l += "1"
		else:
			l += "0"
	return l

import virustotal_report
def dump_all():
	apk_list = dump_f(apk_dir)
	result_list = virustotal_report.read_report2()
	fd_ret = open("../data/ret.1227", "w")
	for i in apk_list:
		raw_name = dump_a(i)
		if raw_name == -1: continue
		vector = dump_p(raw_name)
		if not raw_name + ".apk" in result_list:
			continue
		fd_ret.write("%s\t%s\t%s\n" %(raw_name, vector, result_list[raw_name + ".apk"]))
	fd_ret.close()

if __name__ == "__main__":
	dump_all()
'''
	raw = dump_a(dump_f(apk_dir)[0])
	print dump_p(raw)
'''
