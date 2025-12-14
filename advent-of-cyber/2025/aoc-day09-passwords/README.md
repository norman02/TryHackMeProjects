
# 🎄 Advent of Cyber 2025 – Day 9  
## Passwords – A Cracking Christmas

**Room:** Passwords – A Cracking Christmas  
**Difficulty:** Easy  
**Focus:** Password attacks, offline cracking, encrypted files  
**Status:** Completed  

---

## 🧾 TL;DR

This room demonstrates how attackers recover data from encrypted files by **guessing weak passwords**, not by breaking encryption. Using dictionary attacks against an encrypted PDF and ZIP file, both passwords were cracked quickly, reinforcing that **human password choice is often the weakest link**.

---

## 🧠 Objective

Recover flags stored inside:
- an encrypted **PDF**
- an encrypted **ZIP archive**

Both files are protected with passwords that must be cracked using offline techniques.

---

## 🖥️ Environment Setup

From the TryHackMe VM, switch to the Desktop directory:

```bash
cd ~/Desktop
ls
````

You should see:

* `flag.pdf`
* `flag.zip`

---

## 🔍 Step 1 – Identify File Types

Before choosing tools, confirm the file formats:

```bash
file flag.pdf
file flag.zip
```

### Why this matters

Different encrypted formats require **different cracking tools** and workflows.

---

## 📕 Step 2 – Crack the Encrypted PDF

### Tool: `pdfcrack`

PDFs often use weak user passwords and are good candidates for dictionary attacks.

```bash
pdfcrack -f flag.pdf -w /usr/share/wordlists/rockyou.txt
```

### What’s happening

* The tool hashes each wordlist entry
* Compares it against the PDF encryption
* Stops when a matching password is found

Once recovered, open the PDF:

```bash
xdg-open flag.pdf
```

📌 **Flag 1 is found inside the document.**

---

## 🗜️ Step 3 – Crack the Encrypted ZIP

ZIP cracking is a **two-stage process**.

---

### Stage 1 – Extract a Crackable Hash

John the Ripper works with hashes, not ZIP files directly.

```bash
zip2john flag.zip > ziphash.txt
```

---

### Stage 2 – Crack with John

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt ziphash.txt
```

John will output the recovered password if successful.

---

## ⚠️ Common Pitfall – `unzip` Fails

Attempting extraction with `unzip` may result in:

```
unsupported compression method 99
```

### Why this happens

* The ZIP uses **AES encryption**
* `unzip` does not support this format

---

## ✅ Correct Extraction Tool – `7z`

```bash
7z x flag.zip
```

Enter the cracked password when prompted.

Then retrieve the flag:

```bash
cat flag.txt
```

📌 **Flag 2 is revealed.**

---

## 🧠 Key Takeaways

* Encryption is strong — passwords are weak
* Dictionary attacks succeed because users reuse passwords
* Offline cracking produces **no authentication logs**
* Tool choice matters (e.g., `7z` vs `unzip`)
* Attackers adapt tools mid-chain

---

## 🛡️ Defender Perspective

Because cracking is offline:

* No failed logins
* No lockouts
* No SIEM auth alerts

### Detection must focus on:

* Process execution (`john`, `hashcat`, `pdfcrack`)
* Wordlist access (`rockyou.txt`)
* CPU/GPU utilization spikes
* Potfiles and hash artefacts

---

## 🔐 Defensive Recommendations

* Use long, random passwords (password managers)
* Prefer key-based encryption over passwords
* Monitor endpoints for cracking tools
* Restrict wordlists on production systems
* Enforce MFA where applicable

---

## ⚖️ Ethical Note

All actions were performed **only in an authorized TryHackMe lab**.
Password cracking techniques should be used solely for:

* education
* defensive testing
* incident response

Never against systems without permission.

---

## 🏁 Outcome

* Successfully cracked:

  * an encrypted PDF
  * an AES-encrypted ZIP archive
* Demonstrated real-world password attack workflows
* Reinforced that **passwords remain a critical security weakness**


