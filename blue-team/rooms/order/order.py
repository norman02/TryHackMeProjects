cipher_hex = (
    "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
    "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
)

cipher = bytes.fromhex(cipher_hex)

# Known plaintext at the start
known_plain = b"ORDER:"

# Extract first bytes of ciphertext
cipher_start = cipher[:len(known_plain)]

# Derive the repeating key
key = bytes([c ^ p for c, p in zip(cipher_start, known_plain)])
print(f"[+] Derived key: {key}")

# Repeat the key
full_key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]

# Decrypt full message
plaintext = bytes([c ^ k for c, k in zip(cipher, full_key)])

print("\n[+] Decrypted message:\n" + plaintext.decode("utf-8"))

