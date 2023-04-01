# Credit to https://morsecode.world/international/translator.html
# Using this website, to test my code. XD
from encode_decode_file import encode_decode as ed

# Input from the user:
while True:  # Loop till no input message
    choice_SorF = input("Write message(W) or Input file(I): ").upper()
    if choice_SorF == "Write message" or choice_SorF == "W":
        sentence = input("Press enter to exit or Input message: ")
        while sentence != "":
            choice_EorM = input("Type English to Morse(EM) or Morse to English(ME): ").upper()
            # Later: input will be able to detect me or em without user specifying it.
            if choice_EorM == "ME" or choice_EorM == "Morse to English":
                ed.morse_code_mef(sentence)
                break
            elif choice_EorM == "EM" or choice_EorM == "English to Morse":
                ed.morse_code_emf(sentence)
                break
            else:  # Ask the user again, if they didn't enter either.
                print("Please type EM or ME")
        else:  # Prompt (Write message or Input file) again
            print("Thank you for using \"write message.\"")
    elif choice_SorF == "Input file" or choice_SorF == "I":
        print("Yes you are at file")
        with open("Original message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
            for sentence in r_file:  # iterate through the file line by line
                w_file.write(str(ed.morse_code_mef(sentence)))
    else:  # End the program.
        print("Thank you for using \"morse program.\"")
        break

