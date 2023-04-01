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
	".": ".-.-.-",
	"\n": "\n"  # Create new line in the morse code.
}


def morse_code_emf(english: str) -> str:  # Convert English sentence to Morse Code
	dummy_morse_code = ""
	for cha in english:
		for key in morse_code_dict:
			if cha.capitalize() == key:  # Ignore case-sensitive in order for the statement to be true.
				dummy_morse_code += morse_code_dict.get(key) + "   "
	if english != "":  # you could comment this out. Not really needed.
		print(f"Original : {english} | Morse Code: {dummy_morse_code}")
		return dummy_morse_code


def morse_code_mef(morse_code: str) -> str:  # Convert Morse code to English
	dummy_english = ""
	for index in morse_code.split(" "):  # morse_code.split(" ") is a list, where index iterate through it
		for key_index in morse_code_dict.keys():
			if index == morse_code_dict.get(key_index):
				dummy_english += key_index

	print(f"Original : {morse_code} | English: {dummy_english}")
	return dummy_english


# Open the input file in read mode and output file in write mode
# Use it for reference, later delete
# with open("Original message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
# 	for sentence in r_file:  # iterate through the file line by line
# 		w_file.write(str(morse_code_mef(sentence)))
