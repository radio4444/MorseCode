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
}


def morseCode_EM(english: str) -> str:  # Convert English sentence to Morse Code
    dummy_morse_code = ""
    for cha in english:
        for key in morse_code_dict:
            if cha.capitalize() == key:  # Ignore case-sensitive in order for the statement to be true.
                dummy_morse_code += morse_code_dict.get(key) + "   "
    if english != "":  # you could comment this out. Not really needed.
        print(f"Original : {english} | Morse Code: {dummy_morse_code}")
        return dummy_morse_code


def morseCode_ME(morse_code: str) -> str:  # Convert Morse code to English
    dummy_english = ""
    for index in morse_code.split(" "):  # morse_code.split(" ") is a list, where index iterate through it
        for key_index in morse_code_dict.keys():
            if index == morse_code_dict.get(key_index):
                dummy_english += key_index

    print(f"Original : {morse_code} | English: {dummy_english}")
    return dummy_english


# Open the input file in read mode and output file in write mode
# old version.
with open("Morse message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
    for sentence in r_file:  # iterate through the file line by line
        w_file.write(morseCode_ME(sentence))

# Problem:
# 	- Output file would have leading (spaces at the beginning) and trailing (spaces at the end) characters
# 		because of the newline character in input file
#	- Because of the newline character, it would mess up morse code to english.
#   - English to morse code will be fine but the morse code would have trailing and leading character
# Solution:
# 	- using strip to remove any leading and trailing character
# 	- create newline character, after readline execute.

# with open("Morse message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
# 	for sentence in r_file:  # iterate through the file line by line
# 		sentence = sentence.strip()
# 		w_file.write(morseCode_ME(sentence).strip())
# 		w_file.write("\n")
# with open("English message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
# 	for sentence in r_file:  # iterate through the file line by line
# 		sentence = sentence.strip()
# 		w_file.write(morseCode_EM(sentence).strip())
# 		w_file.write("\n")
