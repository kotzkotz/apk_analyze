import sys

a = [i.split("\t") for i in file(sys.argv[1]).read().split("\n")][:-1]
l = len(a[0][0])
for i in a:
	if len(i[0]) != l:
		print i
print l
