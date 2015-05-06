import os,glob,zipfile

apk_dir = "../apk-file"
permission_list = file("../data/permissions.txt").read().split("\r\n")[:-1]

def dump_a(apk_name):
	fd = zipfile.ZipFile(apk_name)
	apk_raw_name = apk_name.split("/")[-1].split(".")[0] 
	for file in fd.namelist():
		if file == "AndroidManifest.xml":
			fd.extract(file, "../tmp/"+apk_raw_name)
	fd.close()
	return apk_raw_name

def dump_f(d):
	apk_list = []
	for file in glob.glob(d + "/*.APK"):
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

def dump_all():
	apk_list = dump_f(apk_dir)
	fd_ret = open("../ret", "w")
	for i in apk_list:
		raw_name = dump_a(i)
		vector = dump_p(raw_name)
		fd_ret.write("%s\t%s\n" %(raw_name, vector))
	fd_ret.close()

if __name__ == "__main__":
	dump_all()
'''
	raw = dump_a(dump_f(apk_dir)[0])
	print dump_p(raw)
'''
