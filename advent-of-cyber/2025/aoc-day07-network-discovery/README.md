
# 🎄 Advent of Cyber 2025 – Day 7  
## Network Discovery – Scan-ta Clause

**Difficulty:** Easy  
**Focus:** Network discovery, port scanning, service enumeration  
**Perspective:** SOC / Blue Team / Junior Pentest  
**Tools:** Nmap, FTP, Netcat, Dig  
**Environment:** TryHackMe AttackBox (important)

---

## 🧠 Objective

Discover exposed services on a QA server, enumerate hidden network services across TCP and UDP, extract three key fragments, and pivot to internal service discovery to recover a final flag from a database.

This room teaches **how attackers and defenders map attack surfaces**, not just how to run scans.

---

## ⚠️ Environment Assumption (Important)

This walkthrough **assumes usage of the TryHackMe AttackBox**.

When using an external Kali VM via VPN, TCP ports may appear filtered and break the intended flow of the lab. The AttackBox has the correct network vantage point.

---

## 🎯 Target Information

- **Hostname:** tbfc-devqa01
- **IP Address:** `10.64.175.13`

---

## Phase 1 – Basic TCP Discovery

### Command
```bash
nmap 10.64.175.13
````

### Why this works

* Scans the top 1000 most common TCP ports
* Quickly identifies obvious services

### Expected Result

You should see:

```
22/tcp open ssh
80/tcp open http
```

---

## Phase 2 – Web Enumeration

Open the website from the AttackBox browser:

```
http://10.64.175.13
```

📌 **Answer:**
Note the **evil message** displayed at the top of the defaced page.

---

## Phase 3 – Full TCP Scan + Banner Grabbing

### Command

```bash
nmap -p- --script=banner 10.64.175.13
```

### Why this matters

* `-p-` scans all 65,535 TCP ports
* `--script=banner` identifies services running on non-standard ports

### Expected New Findings

* **21212/tcp** → FTP (vsFTPd)
* **25251/tcp** → Custom TBFC application

---

## Phase 4 – FTP Enumeration (Key #1)

### Connect to FTP

```bash
ftp 10.64.175.13 21212
```

Login as:

```
anonymous
```

List files:

```text
ls
```

Download the key:

```text
get tbfc_qa_key1 -
```

📌 **Answer:**
First key fragment (`KEYNAME:KEY`)

Exit FTP:

```text
bye
```

---

## Phase 5 – Custom Service Enumeration (Key #2)

### Connect with Netcat

```bash
nc -v 10.64.175.13 25251
```

Interact with the service:

```text
HELP
GET KEY
```

📌 **Answer:**
Second key fragment

Exit with:

```text
CTRL+C
```

---

## Phase 6 – UDP Discovery (Key #3)

So far, only TCP has been scanned. Now pivot to UDP.

### UDP Scan

```bash
nmap -sU 10.64.175.13
```

You should see:

```
53/udp open domain
```

---

## Phase 7 – DNS Enumeration

Query the DNS server directly for TXT records:

```bash
dig @10.64.175.13 TXT key3.tbfc.local +short
```

📌 **Answer:**
Third key fragment

---

## Phase 8 – Admin Console Access

Return to the website:

```
http://10.64.175.13
```

Submit **all three key fragments combined** to access the secret admin console.

You will receive shell access as the application user.

---

## Phase 9 – On-Host Service Enumeration

Once inside the host, list listening services:

```bash
ss -tunlp
```

### Key Observation

You will find:

```
127.0.0.1:3306
```

This is a **MySQL database bound to localhost only**, invisible to external scans.

📌 **Answer:**
MySQL is running on **port 3306**

---

## Phase 10 – Database Enumeration (Final Flag)

List database tables:

```bash
mysql -D tbfcqa01 -e "show tables;"
```

Query the flags table:

```bash
mysql -D tbfcqa01 -e "select * from flags;"
```

📌 **Answer:**
Final flag from the database

---

## 🧠 Key Lessons Learned

* Network discovery is iterative, not one-shot
* Services often run on non-standard ports
* TCP filtering does not mean services don’t exist
* UDP (especially DNS) is frequently overlooked
* Localhost-only services trust internal access
* Perimeter defenses ≠ internal security

---

## 🛡️ Defensive Takeaways

From a blue-team perspective:

* Monitor DNS traffic, including TXT records
* Don’t rely on firewalls alone for protection
* Restrict localhost services with authentication
* Regularly audit listening services internally

---

## ⚠️ Ethical Note

All actions were performed:

* in a controlled TryHackMe lab
* for defensive learning purposes
* without impacting real systems

Unauthorized scanning or exploitation outside approved environments is unethical and illegal.

---

## 🔗 Further Learning

* TryHackMe: Nmap – The Basics
* TryHackMe: Network Services
* OWASP: Attack Surface Analysis

