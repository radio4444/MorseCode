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


# Input and output file function.

with open("Original message.txt", 'r') as r_file:
	# Keep reading the file till there is none?
	sentence = r_file.readline()
	with open("Convert message.txt", 'w') as w_file:
		w_file.write(str(morse_code_mef(sentence)))
