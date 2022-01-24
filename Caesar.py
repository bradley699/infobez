from collections import Counter
from itertools import islice
import re

start = "а"
alphabet = ""

for i in range(32):
    alphabet += chr(ord(start) + i)

alphabet = alphabet.upper()

def caesar_encrypt(text, shift=4):
    text = text.upper()
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(table)
    
def caesar_decrypt(text, shift=4):
    plainText = ""
    for char in text:
        if char in alphabet:
            char_index = (alphabet.find(char) - shift) % len(alphabet)
            plainText += alphabet[char_index]
        else:
            plainText += char
    return plainText

def mono_encrypt(cipher, text):
    text = text.upper()
    mono1 = re.findall("\w{1}", text)
    text_mono_count = Counter(islice(mono1, 0, None))

    mono2 = re.findall("\w{1}", cipher)
    cipher_mono_count = Counter(islice(mono2, 0, None))

    for i, y in zip(cipher_mono_count.most_common(), text_mono_count.most_common()):
        cipher = cipher.replace(i[0], y[0])

    return cipher
    
def bigram_encrypt(cipher, text):
    text = text.upper()
    bi1 = re.findall("\w{2}", text)
    text_bi_count = Counter(islice(bi1, 0, None))

    bi2 = re.findall("\w{2}", cipher)
    cipher_bi_count = Counter(islice(bi2, 0, None))

    for i, y in zip(cipher_bi_count.most_common(), text_bi_count.most_common()):
        cipher = cipher.replace(i[0], y[0])

    return cipher


text = open('WarAndPeace.txt', 'r', encoding='utf-8').read()

cipherText = caesar_encrypt(text)
plainText = caesar_decrypt(cipherText)


print("Шифр цезаря: ")
print(cipherText)
print("--------------------------------------------------------------------------------")

mono_cipher = mono_encrypt(cipherText, text)
bigram_cipher = bigram_encrypt(cipherText, text)
print("Монограммы: ")
print(mono_cipher)
print("--------------------------------------------------------------------------------")
print("Биграммы:")
print(bigram_cipher)
print("--------------------------------------------------------------------------------")