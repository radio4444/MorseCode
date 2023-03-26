# # It will stop reading, whenever there is a period (.) and then store in sentence variable. (Solution: using split?)
# # Then, it will depend on the user, if they want to me or em. (for now). [later automatic detection]
#
#
# # # a file named "geek", will be opened with the reading mode.
# # file = open('geek.txt', 'r')
# # # This will print every line one by one in the file
# # for each in file:
# # 	print(each)
#
# # Python code to illustrate read() mode
# file = open("file.txt", "r")
# print(file.read(), "fileRead")  # extract a string that contains all characters in the file, use file.read
# print(file.read(5), "fileRead(5)")  # call a certain number of characters.
#
# # write() mode
# # Python code to create a file
# file = open('geek1.txt', 'w')  # created new file, since it did not exist
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()
#
# # Python code to illustrate append() mode
# file = open('geek.txt', 'a')
# file.write("This will add this line")  # adding in current line. does not print in newline.
# file.close()
#
# # rstrip(): This function strips each line of a file off spaces from the right-hand side.
# # lstrip(): This function strips each line of a file off spaces from the left-hand side.
#
#
# # - Cleaner syntax and exception handling.
# # - good practice
# # - auto-cleanup: any files opened will be closed automatically after one is done.
# # - meaning, no need to specify to close file
# # Python code to illustrate with()
# with open("file.txt") as file:
# 	data = file.read()
# # do something with data
#
# # Python code to illustrate with() along with write()
# with open("file.txt", "w") as f:
# 	f.write("Hello World!!!")

# Python code to illustrate split() function
with open("file.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print(word)
		print(type(str(line.split())))
