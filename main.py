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
	"Z": "--.."
}

# this is scratch.

# Create a dummy word_variable, which convert the word to morse code
word_variable = "Ehsan"
morse_code = ""
for cha in word_variable:
	for key in morse_code_dict:
		if cha.capitalize() == key: # Ignore case-sensitive in order for the statement to be true.
			morse_code += morse_code_dict.get(key) + "   "
print(f"Original : {word_variable} | Morse Code: {morse_code}")

