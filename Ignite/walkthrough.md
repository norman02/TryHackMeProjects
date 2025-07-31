
## 📄 `Ignite/walkthrough.md`

````markdown
# TryHackMe Room: Ignite

- [Room Link](https://tryhackme.com/room/ignite)
- Difficulty: ✅ Misleadingly labeled "Easy"
- Status: ❌ Incomplete due to broken RCE handling and shell restrictions
- Tags: Fuel CMS, CVE-2018-16763, RCE, PHP injection

---

## 🧠 Overview

The room presents a vulnerable installation of **Fuel CMS 1.4.1**, exploitable via **CVE-2018-16763**. While RCE is technically possible, severe PHP input parsing limitations prevent practical shell access.

---

## 🔍 Enumeration

### Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt ignite.thm
````

* Port 80 open
* Apache 2.4.18
* `/fuel/` found in `robots.txt`

### Gobuster

```bash
gobuster dir -u http://ignite.thm -w /usr/share/wordlists/dirb/common.txt -x php,txt,html -o gobuster.txt
```

* `/fuel/` confirmed
* `/offline`, `/home`, `/index.php` visible

---

## ⚔️ Exploitation Attempt

### CVE-2018-16763

```bash
searchsploit fuel cms
```

* Fuel CMS 1.4.1 RCE via vulnerable `filter=` parameter
* Used modified Python exploit: `fuel_rce.py`
* Confirmed command execution via `whoami`, `id`, `uname`

### Example:

```bash
cmd: whoami
→ systemwww-data
```

---

## 🧨 Reverse Shell Attempts

Tried:

* Bash reverse shell
* Base64-decoded payload
* PHP shell upload (`.php`, `.phtml`, `.php.jpg`)
* Named pipe shell (`mkfifo`)
* Metasploit (`fuelcms_traversal`) — module missing or unindexed

**All failed due to PHP's `create_function()` breaking on shell syntax.**

---

## 🏁 Flags

Unable to retrieve flags due to:

* RCE being too limited for file reads
* No accessible `/home/<user>` or `/root` content
* `cat` commands breaking PHP

---

## 🧵 Lessons Learned

* CVE exploitation ≠ guaranteed shell
* Web-based RCEs may be heavily restricted
* Always test flag paths early if shell is unstable

---

## ✅ GitHub Summary

* Added:

  * `nmap.txt`
  * `gobuster.txt`
  * `fuel_rce.py` (modified exploit)
  * `walkthrough.md`
* Marked room as **incomplete but documented**

