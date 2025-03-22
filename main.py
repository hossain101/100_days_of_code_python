# Caesar Cipher

alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]




def encrypt(text_1, shift_1):
    encrypted_string = ""
    for letters in text_1:
        if letters in alphabets:
            index_no = alphabets.index(letters)

            shifted_index = index_no + shift_1
            if shifted_index >= len(alphabets):
                shifted_index = shifted_index - len(alphabets)
            encrypted_string += alphabets[shifted_index]
        else:
            encrypted_string += letters
    print(f"The encrypted text is: {encrypted_string}")


def decrypt(text_1, shift_1):
    decrypted_string = ""
    for letters in text_1:
        if letters in alphabets:
            index_no = alphabets.index(letters)
            shifted_index = index_no - shift_1
            if shifted_index < 0:
                shifted_index = len(alphabets) - shifted_index
            decrypted_string += alphabets[shifted_index]
        else:
            decrypted_string += letters

    print(f"The decrypted text is: {decrypted_string}")

   
not_exit = True

while not_exit:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")

    text = input(f"Type your text to be {direction} : ").lower()

    shift = int(input("Type the shift of the letter: "))
    
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    result = input("Do you want to continue? Type 'yes' or 'no' \n")
    if result == "no":
        not_exit = False
        print("Goodbye")
    else:
        not_exit = True
        continue
