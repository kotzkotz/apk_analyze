import postfile,time,glob

def upload(d):
	for file in glob.glob(d + "/*"):
		fd = open('../data/normal.600','a')
		json = postfile.post_file(file)
		if "<html>" in json:
			fd_err = open("../data/error.1227", "a")
			fd_err.write(file + "\n")
			fd_err.close()
			time.sleep(40)
			continue
		json = postfile.post_file(file)	
		msg = "%s\t%s\n" %(file.split("/")[-1], json)
		fd.write(msg)
		fd.close()
		time.sleep(20)


print "UPLOAD START"
upload("../apk-list")
print "DONE"
