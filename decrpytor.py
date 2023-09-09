import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f'key: {key}')
#print(f'chars: {chars}')


#encryption
plaintext = input("Enter the text to be encypted: ")
encrypted_text = ""

for letter in plaintext:
    index = chars.index(letter)
    encrypted_text += key[index]

print(f"Original Message: {plaintext}")
print(f"Encrypted Message: {encrypted_text}")

#decryption
dencrypted_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    dencrypted_text += chars[index]

print(f"Encrypted Message: {encrypted_text}")
print(f"Decrypted Message: {dencrypted_text}")