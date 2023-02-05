import string

def decrypt(ciphertext):
    for key in range(1, 26):
        plaintext = ""
        for c in ciphertext:
            if c.isalpha():
                shift = ord(c) + key
                if c.isupper():
                    if shift > ord('Z'):
                        shift -= 26
                    plaintext += chr(shift)
                else:
                    if shift > ord('z'):
                        shift -= 26
                    plaintext += chr(shift)
            else:
                plaintext += c
        if "FLAG:" in plaintext:
            start = plaintext.index("FLAG:")
            return plaintext[start:]
    return None

ciphertext = "qba'g xabj SYNT: guvf vf fbzr qhzzl synt"
plaintext = decrypt(ciphertext)
print(plaintext)
