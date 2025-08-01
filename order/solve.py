import itertools

# Load and clean hex
with open("message.txt") as f:
    hex_data = f.read().replace("\n", "").strip()

# Convert hex to bytes
cipher_bytes = bytes.fromhex(hex_data)

# Characters to use in brute-force key search
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Try all 4-character keys
for key in itertools.product(charset, repeat=4):
    key_bytes = bytes("".join(key), "utf-8")
    plaintext = bytearray()

    for i in range(len(cipher_bytes)):
        plaintext.append(cipher_bytes[i] ^ key_bytes[i % len(key_bytes)])

    try:
        decoded = plaintext.decode("utf-8")
        if "THM{" in decoded or "ORDER:" in decoded:
            print(f"[+] Key: {''.join(key)}")
            print(f"[+] Decrypted:\n{decoded}")
            break
    except UnicodeDecodeError:
        continue

