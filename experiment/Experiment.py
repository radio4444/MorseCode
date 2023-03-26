with open("experiment", "w+") as file:
	file.write("Testing\n")
	file.write("Testing 123")
	file.seek(0)
	print(file.readlines())
