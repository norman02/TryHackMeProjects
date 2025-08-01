import itertools
import re

# Full hex string
cipher_hex = (
    "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
    "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
)

cipher = bytes.fromhex(cipher_hex)
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

for key_len in [4, 5]:
    for key_tuple in itertools.product(charset, repeat=key_len):
        key = bytes("".join(key_tuple), "utf-8")
        decrypted = xor_decrypt(cipher, key)
        try:
            decoded = decrypted.decode("utf-8")
            # Look for a legit-looking flag with 1337-style patterns
            match = re.search(r"THM\{[A-Za-z0-9_]{8,40}\}", decoded)
            if match:
                print(f"[+] Key: {key.decode()}")
                print(f"[+] Flag: {match.group(0)}")
                exit()
        except:
            continue

