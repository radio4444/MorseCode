# Credit to https://morsecode.world/international/translator.html
# Using this website, to test my code. XD
from encode_decode_file import encode_decode

# Input from the user:
while True:  # Loop till no input message
	sentence = input("Input the message: | Or press enter again to exit")
	while sentence != "":
		choice = input("Type English to Morse(EM) or Morse to English(ME): ")
		# Later: input will be able to detect me or em without user specifying it.
		if choice.upper() == "ME" or choice.upper() == "Morse to English":
			encode_decode.morse_code_mef(sentence)
			break
		elif choice.upper() == "EM" or choice.upper() == "English to Morse":
			encode_decode.morse_code_emf(sentence)
			break
		else:  # Ask the user again, if they didn't enter either.
			print("Please type EM or ME")
	else:
		break
