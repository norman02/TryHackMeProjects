
# RootMe CTF – TryHackMe

## 📖 Overview
This repository contains notes and a full walkthrough of the [RootMe](https://tryhackme.com/room/rrootme) CTF room on TryHackMe.  
The goal of this room is to practice **web exploitation**, **file upload bypasses**, and **privilege escalation** using SUID misconfigurations.

---

## ⚡ Quick Info
- **Platform:** TryHackMe  
- **Room:** RootMe  
- **Difficulty:** Easy  
- **Objective:** Capture both `user.txt` and `root.txt`

---


## 🚩 Flags Captured

* **User Flag:** `THM{y0u_g0t_a_sh3ll}`
* **Root Flag:** `THM{pr1v1l3g3_3sc4l4t10n}`

---

## 🔑 Key Techniques Used

* **Reconnaissance** with `nmap` and `gobuster`
* **File Upload Bypass** using `.php5` extension
* **Reverse Shell** via uploaded webshell
* **SUID Privilege Escalation** exploiting `/usr/bin/python`

---

## 📓 Walkthrough

The full detailed process (including commands, output, and answers to all THM questions) is available here:
👉 [walkthrough.md](walkthrough.md)

---

## 🛠 Lessons Learned

* Always check for **alternative extensions** (`.php5`, `.phtml`) in file upload filters.
* Misconfigured **SUID binaries** can be leveraged for privilege escalation.
* THM rooms may sometimes expect *slightly incorrect versions* (e.g., Apache `2.4.29` vs actual `2.4.41`). Always record real findings separately.

---

## ⚖️ Disclaimer

This walkthrough is for **educational purposes only**.
Do not attempt these techniques on systems you do not own or have explicit permission to test.



