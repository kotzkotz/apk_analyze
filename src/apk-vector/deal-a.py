import sys
a = [i.strip().split("\t") for i in file(sys.argv[1]).read().split("\n")][:-1]
b = [i.strip().split("\t") for i in file(sys.argv[2]).read().split("\n")][:-1]
assert(len(a) == len(b))
fd = open("asd","w")
for i in xrange(len(a)):
	assert(a[i][1] == b[i][1])
	fd.write( a[i][0] + b[i][0] + "\t" + a[i][1] + "\n")
fd.close()
