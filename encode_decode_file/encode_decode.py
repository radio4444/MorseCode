morse_code_dict = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "-.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	" ": "/",
	".": ".-.-.-"
}


# Convert English sentence to Morse Code
def morse_code_emf(english: str) -> None:
	dummy_morse_code = ""
	for cha in english:
		for key in morse_code_dict:
			if cha.capitalize() == key:  # Ignore case-sensitive in order for the statement to be true.
				dummy_morse_code += morse_code_dict.get(key) + "   "
	if english != "":  # you could comment this out. Not really needed.
		print(f"Original : {english} | Morse Code: {dummy_morse_code}")


# Convert Morse code to English
def morse_code_mef(morse_code: str) -> None:
	dummy_english = ""
	for index in morse_code.split(" "):  # morse_code.split(" ") is a list, where index iterate through it
		for key_index in morse_code_dict.keys():
			if index == morse_code_dict.get(key_index):
				dummy_english += key_index

	print(f"Original : {morse_code} | English: {dummy_english}")


# Create a file called "original message" [manually]
# -content: this is a sentence. | This is another sentence.

with open("Original message.txt", 'r') as r_file:  # after 'as', we declare variable to call the 'file'
	# Create a variable called "sentence", which store the content from the "Original message"
	sentence = r_file.read()
	# Create a new filed called: "Encode/decode message" and output the content from the "sentence"
	# cannot use / as it mean to be use for directory.
	with open("Convert message.txt", 'w') as w_file:
		w_file.write(str(sentence))

# Two ways we could create stop.
	# Either using split method
	# Or if cha == '.' then