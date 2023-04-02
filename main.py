# Credit to https://morsecode.world/international/translator.html
# Using this website, to test my code. XD
import encode_decode as ed
import os

cwd = os.getcwd()  # get current directory


# Input from the user:
while True:  # Loop till no input message
    choice_SorF = input("Write message(W) or Input file(I) or Press Enter to exit: ").upper()
    if choice_SorF == "WRITE MESSAGE" or choice_SorF == "W":
        sentence = input("Press enter to exit or Input message: ")
        # Later: input will be able to detect me or em without user specifying it.
        while sentence != "":
            choice_EorM = input("Type English to Morse(EM) or Morse to English(ME): ").upper()
            if choice_EorM == "ME" or choice_EorM == "Morse to English":
                ed.morseCode_ME(sentence)
                break
            elif choice_EorM == "EM" or choice_EorM == "English to Morse":
                ed.morseCode_EM(sentence)
                break
            else:  # Ask the user again, if they didn't enter either.
                print("Please type EM or ME")
        else:  # Prompt (Write message or Input file) again
            print("Thank you for using \"write message.\"")
    elif choice_SorF == "INPUT FILE" or choice_SorF == "I":
        r_file = input("Press enter to exit or Input the filename: ")
        r_filepath = os.path.join(cwd, 'encode_decode_file', r_file+'.txt') # reading file from encode_decode_file directory
        # Later: input will be able to detect me or em without user specifying it.
        while r_file != "":
            w_file = input("Output the filename: ")
            w_filepath = os.path.join(cwd, 'encode_decode_file', w_file + '.txt')
            choice_EorM = input("Type English to Morse(EM) or Morse to English(ME): ").upper()
            if choice_EorM == "ME" or choice_EorM == "Morse to English":
                with open(r_filepath, 'r') as r_file, open(w_filepath, 'w') as w_file:
                    for sentence in r_file:  # iterate through the file line by line
                        sentence = sentence.strip()  # for the print message.
                        w_file.write(ed.morseCode_ME(sentence).strip())  # for the output file message.
                        w_file.write("\n")
                break
            elif choice_EorM == "EM" or choice_EorM == "English to Morse":
                with open(r_filepath, 'r') as r_file, open(w_filepath, 'w') as w_file:
                    for sentence in r_file:  # iterate through the file line by line
                        sentence = sentence.strip()  # for the print message.
                        w_file.write(ed.morseCode_EM(sentence).strip())  # for the output file message.
                        w_file.write("\n")
                break
            else:  # Ask the user again, if they didn't enter either.
                print("Please type EM or ME")
    else:  # End the program.
        print("Thank you for using \"morse program.\"")
        break
