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
	" ": "/"
}


# this is scratch.


# turn this into function:
def morse_code(sentence):  # English to Morse Code
	dummy_morse_code = ""
	for cha in sentence:
		for key in morse_code_dict:
			if cha.capitalize() == key:  # Ignore case-sensitive in order for the statement to be true.
				dummy_morse_code += morse_code_dict.get(key) + "   "
	print(f"Original : {sentence} | Morse Code: {dummy_morse_code}")


morse_code("Tanzil Ehsa")
