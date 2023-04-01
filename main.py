# Credit to https://morsecode.world/international/translator.html
# Using this website, to test my code. XD
import encode_decode as ed

# Input from the user:
while True:  # Loop till no input message
    choice_SorF = input("Write message(W) or Input file(I): ").upper()
    if choice_SorF == "Write message" or choice_SorF == "W":
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
    elif choice_SorF == "Input file" or choice_SorF == "I":
        file = input("Press enter to exit or Input file: ")
        # Later: input will be able to detect me or em without user specifying it.
        while file != "":
            choice_EorM = input("Type English to Morse(EM) or Morse to English(ME): ").upper()
            if choice_EorM == "ME" or choice_EorM == "Morse to English":
                with open("English message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
                    for sentence in r_file:  # iterate through the file line by line
                        sentence = sentence.strip()
                        w_file.write(ed.morseCode_EM(sentence).strip())
                        w_file.write("\n")
                break
            elif choice_EorM == "EM" or choice_EorM == "English to Morse":
                with open("English message.txt", 'r') as r_file, open("Convert message.txt", 'w') as w_file:
                    for sentence in r_file:  # iterate through the file line by line
                        sentence = sentence.strip()
                        w_file.write(ed.morseCode_EM(sentence).strip())
                        w_file.write("\n")
                break
            else:  # Ask the user again, if they didn't enter either.
                print("Please type EM or ME")
    else:  # End the program.
        print("Thank you for using \"morse program.\"")
        break

