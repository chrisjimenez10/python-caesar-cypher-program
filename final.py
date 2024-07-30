#Caesar Cipher
import re
import clear
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar():

    while True:
        clear.clear_console()
        text_display = ""

        while True:
            direction = input(F"{art.logo}\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction == "encode" or direction == "decode":
                break
            else:
                print("Please type \"encode\" or \"decode\"")

        while True:
            text = input("Type your message:\n").lower()
            #Here, we are using a regext pattern and match() function from "re" module to ensure that input is alphabetical ONLY --> NOTE: To ensure that we check the entire string from beginning to end, we need to use the ^ at the start and $ at the end - The + symbol is used to allow and check for multiple occurences, otherwise our regext test would accept only ONE character from the input within the character class
            if re.match("^[a-z]+$", text):
                break
            else:
                print("Please enter a valid alphabetical word without numbers, symbols, or spaces")

        while True:
            shift = input("Type the shift number:\n")
            try:
                shift = int(shift)
                if shift <= 0 or shift >= 26:
                    #In Python, we use the "raise" keyword rather than "throw" like in JavaScript to raise a specific type of error
                    raise ValueError (F"{shift} is out of range. Please provide a valid integer number between 1 and 25 inclusive")
                break
            except ValueError:
                print("Please provide an integer number between 1 and 25 inclusive")

        if direction == "encode":
            for char in text:
                position = alphabet.index(char)
                new_position = position + shift
                text_display += alphabet[new_position]
            print(F"The {direction}d text is: {text_display}")
        elif direction == "decode":
            for char in text:
                position = alphabet.index(char) + 26
                new_position = position - shift
                text_display += alphabet[new_position]
            print(F"The {direction}d text is: {text_display}")
        
        reset = input("Would you like to 'encode' or 'decrypt' another message? - Type Y or yes or anything else to exit\n").lower()
        if reset != "y":
            print("Exiting...")
            return

caesar()