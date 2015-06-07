import sys

a = [i.split("\t") for i in file(sys.argv[1]).read().split("\n")][:-1]
l = len(a[0][0])
fd = open("aaa","w")
for i in a:
	fd.write(i[0][:l] + "\t" + i[1] + "\n")
fd.close()
