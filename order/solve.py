import itertools

with open("message.txt") as f:
    hex_data = f.read().replace("\n", "").strip()

cipher_bytes = bytes.fromhex(hex_data)
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

for key_len in [4, 5]:
    for key in itertools.product(charset, repeat=key_len):
        key_bytes = bytes("".join(key), "utf-8")
        plaintext = bytearray()

        for i in range(len(cipher_bytes)):
            plaintext.append(cipher_bytes[i] ^ key_bytes[i % len(key_bytes)])

        try:
            decoded = plaintext.decode("utf-8")
            if "THM{" in decoded:
                print(f"[+] Key: {''.join(key)}")
                print(f"[+] Decrypted:\n{decoded}")
                exit()
        except:
            continue

