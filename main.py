# Credit to https://morsecode.world/international/translator.html
# Using this website, to test my code. XD

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


# Input from the user:
while True:
	sentence = input("Input the message: ")
	if sentence != "":
		choice = input("Type English to Morse(EM) or Morse to English(ME): ")
	# Later: input will be able to detect me or em without user specifying it.
		if choice.upper() == "ME" or choice.upper() == "Morse to English":
			morse_code_mef(sentence)
		elif choice.upper() == "EM" or choice.upper() == "English to Morse":
			morse_code_emf(sentence)
		else:
			print("Please type EM or ME")
		if sentence == "":
			break
	else:
		break
