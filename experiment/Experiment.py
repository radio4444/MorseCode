# Practice file handling

# Create a file called "original message" [manually]
# -content: this is a sentence. | This is another sentence.
with open("Original message.txt", 'r') as r_file:  # after 'as', we declare variable to call the 'file'
	# Create a variable called "sentence", which store the content from the "Original message"
	sentence = r_file.read()
	# Create a new filed called: "Encode/decode message" and output the content from the "sentence"
	# cannot use / as it mean to be use for directory.
	with open("Convert message.txt", 'w') as w_file:
		w_file.write(sentence)

