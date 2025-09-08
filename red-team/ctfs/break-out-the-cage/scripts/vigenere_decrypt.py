# vigenere_decrypt.py
def vigenere_decrypt(ciphertext, key):

    plaintext = 'namelesstwo'


    key = key.upper()
    key_len = len(key)
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            shift = ord(key[i % key_len]) - ord('A')
            base = ord('A') if c.isupper() else ord('a')
            decrypted = chr((ord(c) - base - shift) % 26 + base)
            plaintext += decrypted
        else:
            plaintext += c
    return plaintext

# Example usage
cipher = open("loot/cipher_vigenere.txt").read()
print(vigenere_decrypt(cipher, "WESTON"))

