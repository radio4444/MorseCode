# It will stop reading, whenever there is a period (.) and then store in sentence variable.
# Then, it will depend on the user, if they want to me or em. (for now). [later automatic detection]


# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
	print(each)

# Python code to illustrate read() mode
file = open("file.txt", "r")
print(file.read())  # extract a string that contains all characters in the file, use file.read
print(file.read(5))
