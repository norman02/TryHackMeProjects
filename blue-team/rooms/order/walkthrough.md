# 🧠 TryHackMe Walkthrough — Order

> Room Link: [https://tryhackme.com/room/order](https://tryhackme.com/room/order)  
> Status: ✅ Completed  
> Date: 2025-08-01  
> Flag: `THM{the_hackfinity_highschool}`

---

## 🧩 Challenge Summary

We were given an encrypted message in hex, encoded with a **repeating-key XOR cipher**. The challenge hinted that Cipher always uses a **standard message header**. Our task was to decrypt the message and recover the flag.

---

## 📝 Step 0: Initial Thoughts & False Starts

We began with some false assumptions that guided early efforts:

### ❌ Mistake #1: We assumed the message started with `THM{`
- Since all flags on THM follow this format, we began by XORing the first 4 ciphertext bytes with `"THM{"` to recover a partial key.
- This gave us some garbage and misleading partial flags like:
```

THM{Q7?pyafEp\:hJ#i\~Fc;'rzhn\[w7?...

````
- Many failed attempts followed using regex and brute-force searching for `THM{.*}` patterns.

### ❌ Mistake #2: Brute-forcing too broadly
- We wrote a script to try all 4–5 character uppercase alphanumeric keys (`A–Z`, `0–9`)
- This ran for minutes without results
- We then tried looser regex patterns and even leetspeak-style sanitization — but still no valid flag

---

## 🔎 Step 1: Real Clue — `"ORDER:"` Header

Eventually, we re-read the challenge and saw the **critical hint**:

> "*...every message always starts with the header: `ORDER:`*"

💡 This gave us a reliable **known plaintext** segment, 7 characters long.

---

## 🔐 Step 2: XOR Known-Plaintext Attack

We extracted the first 7 ciphertext bytes:

```hex
1c 1c 01 04 19 63 73
````

Converted `"ORDER:"` to ASCII:

```text
79 82 68 69 82 58  → b"ORDER:"
```

And XOR'd:

```python
key = bytes([cipher[i] ^ known[i] for i in range(7)])
```

✅ Resulting Key:

```text
b'SNEAKY'
```

---

## 🔓 Step 3: Decrypt the Message

We repeated the key across the full ciphertext length and XOR'd again:

```python
full_key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]
plaintext = bytes([c ^ k for c, k in zip(cipher, full_key)])
```

---

## 📬 Step 4: Final Decrypted Message

```text
ORDER: Attack at dawn. Target: THM{the_hackfinity_highschool}.
```

---

## 🏁 Final Flag

```text
THM{the_hackfinity_highschool}
```

---

## ✅ Key Takeaways

* ✅ Known-plaintext attacks are powerful against XOR
* ✅ Avoid overengineering — sometimes the challenge gives you exactly what you need
* ✅ Don’t ignore header hints — they’re often the entry point to the whole cipher
* ❌ Don’t brute-force blindly without refining the goal

---

## 🔧 Tools Used

* Python 3
* Manual XOR calculations
* Regex and bruteforce scripts (as false paths)
* `bytes.fromhex`, `zip`, list comprehensions

---

## 🧠 Reflections

What seemed like a hard crypto task was just one clue away from being elegantly solvable. Recognizing the predictable structure in encrypted messages is key to many real-world attacks.

