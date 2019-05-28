with open('D:/Python/Buoi1/path.txt') as f:
	a = list(f.read().split("\n"))
f.close()
with open('D:/Python/Buoi1/path.json',"w") as f:
	for i in a:
		b = list(i.split('/'))
		d = dict()
		d["path"]=i
		d["File_name"]=b[len(b)-1]
		f.write(str(d)+'\n')
	f.close()