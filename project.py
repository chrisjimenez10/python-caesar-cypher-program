#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    #Add the list again after "z" --> Max Shift number to avoid crash is 26 (26 will be the same text)
def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for char in plain_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        encrypted_text += alphabet[new_position]
    print(F"The encrypted text is: {encrypted_text}")
    return encrypted_text

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text=text, shift_amount=shift)

#TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for char in encrypted_text:
        position = alphabet.index(char) + 26
        new_position = position - shift_amount
        decrypted_text += alphabet[new_position]
    print(F"The decrypted text is: {decrypted_text}")

# decrypt(encrypted_text="mjqqt", shift_amount=5)
#TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(encrypted_text=text, shift_amount=shift)

def caesar(algo, cipher_text, shift_amount):
    text_display = ""

    if algo == "encode":
        for char in cipher_text:
            position = alphabet.index(char)
            new_position = position + shift_amount
            text_display += alphabet[new_position]
        print(F"The encrypted text is: {text_display}")
    elif algo == "decode":
        for char in cipher_text:
            position = alphabet.index(char) + 26
            new_position = position - shift_amount
            text_display += alphabet[new_position]
        print(F"The decrypted text is: {text_display}")

caesar(algo=direction, cipher_text=text, shift_amount=shift)