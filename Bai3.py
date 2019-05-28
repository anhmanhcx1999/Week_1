class Path:
	path = '';
	file_name = '';
	def __init__(self, path, file_name):
    	self.path=path
    	self.file_name=file_name
	def Input(self):
		self.path = [i for i in input()]
		self.file_name = input()
	def Check(self):
		with open('D:/Python/Buoi1/path.json','a+') as f:
			s = f.read()
			f.close()
		if s=='':
			return False
		else:
			return True
	def Output(self):
		if self.Check()==True
			with open('D:/Python/Buoi1/path.json','w+') as f:
				self.path = str(self.path)
				f.write(self.path)
				f.close()

a = Path('D:/Python/Buoi1/path.json','bai3.txt')
print(a.path)
print(a.file_name)
	







		