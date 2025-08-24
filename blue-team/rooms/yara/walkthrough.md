# 🛡️ TryHackMe Walkthrough – YARA Room

**Room:** YARA  
**Completion Date:** 2025-08-24  
**Status:** ✅ Completed  
**Difficulty:** Easy  
**Tags:** Blue Team, Threat Hunting, Malware Analysis, YARA, Loki, yarGen, Valhalla

---

## 🧾 Task 1 – Introduction
_No questions to answer._

---

## 🧾 Task 2 – What is YARA?
**Answer:** Pattern matching tool to identify malware samples based on rules.

---

## 🧾 Task 3 – Deploy
**VM Launched.**  
Target IP: `10.201.42.42`

---

## 🧾 Task 4 – Introduction to Yara Rules

**Q: How many sections are within a rule?**  
A: 3

**Q: What section must be included in every rule?**  
A: condition

**Q: A rule must start with what keyword?**  
A: rule

**Q: A string identifier must start with what symbol?**  
A: $

---

## 🧾 Task 5 – Expanding on Yara Rules

**Q: How many string modifiers are listed?**  
A: 6

**Q: What modifier ensures the search is case-insensitive?**  
A: nocase

**Q: What modifier treats a string as hexadecimal?**  
A: hex

**Q: What modifier will search for the string in wide format?**  
A: wide

**Q: What modifier makes a string a regular expression?**  
A: regex

---

## 🧾 Task 6 – Yara Modules

**Q: What keyword is used to import modules in Yara?**  
A: import

**Q: What function will return the extension of a file?**  
A: extname

**Q: What module would you use to find the number of sections in a PE file?**  
A: pe

**Q: What function would return the mime type of a file?**  
A: mimetype

---

## 🧾 Task 7 – Other tools and Yara
_No answers required._

---

## 🧾 Task 8 – Using LOKI and its Yara rule set

### File 1:
- **Loki Detection:** Suspicious
- **Matched YARA Rule:** webshell_php_eval
- **Classification:** HACKTOOL
- **Matching String:** `eval(gzinflate(base64_decode`
- **Hack Tool Name & Version:** WSO Web Shell v4.2.5
- **String Count in YARA File:** 5

### File 2:
- **Loki Detection:** Benign (initially)
- **Web Shell Name:** 1ndex.php – P.A.S. v3.1 (from manual inspection)

---

## 🧾 Task 9 – Creating Yara rules with yarGen

**yarGen command used:**
```bash
python3 yarGen.py -m /home/cmnatic/suspicious-files/file2 --excludegood -o /home/cmnatic/suspicious-files/file2.yar
```

**Run YARA manually:**
```bash
yara file2.yar file2
```

**Yara result:** Yay – rule matched

**Copied to Loki signature folder and ran:**
```bash
python3 ~/tools/Loki/loki.py -p ~/suspicious-files/file2
```

**Loki result:** Yay – rule matched

**Matched string variable:** `$s5`

**Number of strings in rule:** 7  
**File size condition (max):** 3000000

---

## 🧾 Task 10 – Valhalla

**File 1:**
- **SHA256:** (generated with `sha256sum file1/index.php`)
- **APT Attribution:** Nay

**File 2:**
- **SHA256:** (generated with `sha256sum file2/1ndex.php`)
- **First Detected Rule:** webshell_php_passthrucmd
- **YARA Scanner Name:** UnpacMe
- **All AVs detect as malicious:** Yay
- **Other extension recorded:** .txt
- **JavaScript Library used:** jQuery
- **Rule in Loki’s default YARA set?** Nay

---

## 🧾 Task 11 – Conclusion
Room completed 100%. Several tools were broken or outdated, requiring manual fixes and offline troubleshooting. Despite this, all flags were recovered and lessons learned.

---

