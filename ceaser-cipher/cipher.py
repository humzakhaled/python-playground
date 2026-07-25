alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
            continue 
        position = alphabet.index(letter)
        new_position  = position + shift_amount
        if new_position >= len(alphabet):
            new_position = new_position % len(alphabet)
        
        encrypted_text += alphabet[new_position]
    print(f"The encoded text is {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
            continue
        position = alphabet.index(letter)
        new_position  = position - shift_amount
        if new_position < 0:
            new_position = new_position % len(alphabet)
        
        decrypted_text += alphabet[new_position]
    print(f"The decoded text is {decrypted_text}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
