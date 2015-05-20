import postfile,time,glob

def upload(d):
	for file in glob.glob(d + "/*"):
		fd = open('../data/result.1227','a')
		json = postfile.post_file(file)
		if "<html>" in json:
			fd_err = open("../data/error.1227", "a")
			fd_err.write(file + "\n")
			fd_err.clsoe()
			time.sleep(40)
			continue
		json = postfile.post_file(file)	
		msg = "%s\t%s\n" %(file.split("/")[-1], json)
		fd.write(msg)
		fd.close()
		time.sleep(25)


print "UPLOAD START"
upload("../../Genome")
print "DONE"
