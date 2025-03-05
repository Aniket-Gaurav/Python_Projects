# List of all the letters in the alphabet
alphabet = [
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


def encryption(plain_text, shift_keys):
    """
    Encrypts the given text using the Caesar cipher method.
    """
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position by adding the shift key
            new_position = (position + shift_keys) % 26
            # Append the character at the new position to the cipher text
            cipher_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, just append it to the cipher text
            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")


def decryption(cipher_text, shift_keys):
    """
    Decrypts the given text using the Caesar cipher method.
    """
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position by subtracting the shift key
            new_position = (position - shift_keys) % 26
            # Append the character at the new position to the plain text
            plain_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, just append it to the plain text
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")


wanna_end = False
while not wanna_end:
    # Ask the user what to do
    what_to_do = input("Type 'encrypt' to encryption, type 'decrypt' to decryption: ")
    # Ask the user for the text
    text = input("Enter the text: ").lower()
    # Ask the user for the shift number
    shift = int(input("Enter the shift number: "))
    # Encrypt or decrypt based on user's input
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_keys=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_keys=shift)
    # Ask the user if they want to play again
    play_again = input("Type 'yes' to continue or 'no' to end: ")
    # If the user doesn't want to play again, end the program
    if play_again.lower() != "yes":
        wanna_end = True
        print("Goodbye")

