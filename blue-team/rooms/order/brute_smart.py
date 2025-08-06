import itertools

# Full ciphertext from message.txt
cipher_hex = (
    "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
    "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
)

cipher = bytes.fromhex(cipher_hex)

# Expanded charset: uppercase, lowercase, numbers
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

print("[*] Starting brute force...")

# Try 4- and 5-character keys
for key_len in [4, 5]:
    for key_tuple in itertools.product(charset, repeat=key_len):
        key = bytes("".join(key_tuple), "utf-8")
        decrypted = xor_decrypt(cipher, key)

        # Skip non-printable output
        if all(32 <= b <= 126 for b in decrypted):
            decoded = decrypted.decode("utf-8")
            if "THM{" in decoded or "thm{" in decoded.lower():
                print(f"\n[+] Key: {key.decode()}")
                print(f"[+] Output:\n{decoded}")

