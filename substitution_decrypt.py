import string
from collections import Counter

def decrypt(ciphertext):
    frequency = Counter(ciphertext)
    most_common_letters = 'etaoinshrdlcumwfgypbvkjxqz'

    for most_common_letter in most_common_letters:
        key = ord(frequency.most_common(1)[0][0]) ^ ord(most_common_letter)
        plaintext = ""
        for c in ciphertext:
            plaintext += chr(ord(c) ^ key)
        print(plaintext)
        print(most_common_letter)
        if "FLAG:" in plaintext:
            start = plaintext.index("FLAG:")
            return plaintext[start:]
    return None

ciphertext = "rgf'z afgv YSQU: ziol ol q rxddn ysqu"
plaintext = decrypt(ciphertext)
print(plaintext)