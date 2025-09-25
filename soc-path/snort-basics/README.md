# 🛡️ TryHackMe — Snort Challenge: The Basics

**Room URL:** [https://tryhackme.com/room/snort-challenge-the-basics](https://tryhackme.com/room/snort-challenge-the-basics)  
**Difficulty:** Medium  
**Estimated Time:** 90 minutes  
**Tags:** `network-security` `snort` `ids` `rules` `detection-engineering` `blue-team`  
**Status:** In Progress  
**Repo Path:** `~/TryHackMeProjects/soc-path/snort-challenge-basics/`

---

## 🧠 Overview

This room challenges you to write and test Snort intrusion detection rules against a series of PCAP files. Each task explores a different attack vector or file signature, such as:

- Suspicious HTTP commands and headers  
- FTP login attempts and file uploads  
- File signature detection (e.g., PNG, torrent files)  
- Real-world CVEs like **MS17-010** and **Log4Shell (CVE-2021-44228)**

The goal is to deepen your practical detection engineering skills with custom and external rules in Snort.

---

## 🧪 Tasks Covered

| Task | Topic                            | Skill Learned                                      |
|------|----------------------------------|----------------------------------------------------|
| 1    | Introduction                     | Room setup and challenge overview                  |
| 2    | HTTP Rule Writing                | URI pattern, headers, and client-body detection    |
| 3    | FTP Rule Writing                 | Keyword matching in FTP commands                   |
| 4    | PNG File Detection               | File signature matching via hex patterns           |
| 5    | Torrent Metafile Detection       | Bencoded string detection                          |
| 6    | Rule Syntax Troubleshooting      | Fixing syntax errors in Snort rules                |
| 7    | External Rules: MS17-010         | Using community rules for known exploits           |
| 8    | External Rules: Log4j            | Detecting Log4Shell via JNDI injection patterns    |
| 9    | Conclusion                       | Summary and real-world detection advice            |

---

## 🛠️ Usage

This repo contains:

- ✅ `local.rules` – All Snort rules created for this lab  
- ✅ `walkthrough.md` – Full step-by-step explanation  
- ✅ `secrets/notes.md` – Private note for flags, raw logs, credentials (not published)  
- ✅ `README.md` – You’re reading it!  

---

## 🧰 Sample Commands

```bash
# Syntax check
sudo snort -T -c /etc/snort/snort.conf

# Test a rule against a PCAP
sudo snort -c /etc/snort/snort.conf -r ~/Desktop/task2.pcap -A console -q
````

---

## 📁 File Tree

```plaintext
snort-challenge-basics/
├── README.md
├── walkthrough.md
├── local.rules
└── secrets/
    └── notes.md  # ⚠️ Do NOT publish
```

---

## 🔒 MITRE ATT&CK Mapping

* **Initial Access** – Exploiting vulnerable services (MS17-010, Log4j)
* **Execution** – Commands via HTTP/FTP payloads
* **Lateral Movement** – SMB (EternalBlue)
* **Exfiltration / C2** – Torrent use or web-based exfil

---

## 📌 Notes

* Snort version used: `Snort 2.9.x` on THM-hosted VM
* Config path: `/etc/snort/snort.conf`
* Rules added to: `/etc/snort/rules/local.rules`
* PCAPs stored in: `~/Desktop/` on THM desktop

---

## 🔗 Related

* [Official Snort Docs](https://docs.snort.org/)
* [Emerging Threats Rules](https://rules.emergingthreats.net/)
* [MITRE ATT&CK Framework](https://attack.mitre.org/)

