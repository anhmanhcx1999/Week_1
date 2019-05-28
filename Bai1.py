def ReadText():
	file_object = open('D:/Python/Buoi1/Bai1.txt')
	data = file_object.read()
	file_object.close()
	print(data)
ReadText()
