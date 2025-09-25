# 🕵️ Trooper – TryHackMe Walkthrough

## 📌 Room Info
- **Path**: SOC Level 1 → Cyber Threat Intelligence
- **Room**: Trooper (Premium)
- **Difficulty**: Easy
- **Tools Used**: OpenCTI, MITRE ATT&CK Navigator
- **Target IPs**:
  - OpenCTI → `http://10.201.126.98:8080`
  - ATT&CK Navigator → `http://10.201.126.98:4200`
- **Login**:
  - Username: `info@tryhack.io`
  - Password: `TryHackMe1234`

---

## 🎯 Objective
Use threat intelligence platforms to identify an adversary (APT X), investigate their TTPs, and attribute known malware and techniques using OpenCTI and MITRE Navigator.

---

## ✅ Task Answers + How They Were Found

---

### Q1. **What kind of phishing campaign does APT X use as part of their TTPs?**

> **Answer**: `spear-phishing emails`

🔍 **How to find it**:
- Open the threat intelligence report on the target VM.
- The report states:  
  > "APT X was reportedly using spear-phishing emails with weaponized attachments to exploit known vulnerabilities."
- Even though this could map to MITRE ID `T1566.001`, THM only wants the literal phrase.

---

### Q2. **What is the name of the malware used by APT X?**

> **Answer**: `USBferry`

🔍 **How to find it**:
- From the report and OpenCTI, the malware used in the USB-based attacks is called **USBferry**.
- It’s a USB worm used for exfiltration from air-gapped systems.

---

### Q3. **What is the malware's STIX ID?**

> **Answer**: `malware--5d0ea014-1ce9-5d5c-bcc7-f625a07907d0`

🔍 **How to find it**:
- In OpenCTI, go to:
  `Knowledge` → `Threats` → `Malware` → `USBferry`
- Scroll down to find the STIX ID — it's a long UUID-format identifier.

---

### Q4. **With the use of a USB, what technique did APT X use for initial access?**

> **Answer**: `Replication Through Removable Media`

🔍 **How to find it**:
- The malware uses USBs to spread from one machine to another (air-gap jumping).
- This maps to MITRE technique `T1091` – but again, THM just wants the label.

---

### Q5. **What is the identity of APT X?**

> **Answer**: `Tropic Trooper`

🔍 **How to find it**:
- In OpenCTI, view the `Intrusion Sets` list and find the one with USBferry.
- Tropic Trooper is the only group associated with this malware and geography.

---

### Q6. **On OpenCTI, how many Attack Pattern techniques are associated with the APT?**

> **Answer**: `39`

🔍 **How to find it**:
- In OpenCTI:
  `Intrusion Sets` → `Tropic Trooper` → Related `Attack Patterns`
- Count (or scroll to the bottom). The total is **39** attack techniques.

---

### Q7. **What is the name of the tool linked to the APT?**

> **Answer**: `BITSAdmin`

🔍 **How to find it**:
- In the malware analysis, `USBferry` uses `BITSAdmin` (a Windows LOLBin) for downloading/staging payloads.
- Even though USBferry is the main tool, THM expects the **LOLBAS** utility name.

---

### Q8. **What is the sub-technique used by the APT under Valid Accounts?**

> **Answer**: `Local Accounts`

🔍 **How to find it**:
- In ATT&CK Navigator:
  - Filter to `Tropic Trooper` overlays
  - Under `Valid Accounts`, the sub-technique listed is: **Local Accounts** (`T1078.003`)
- THM wants only the sub-technique label.

---

### Q9. **Under what Tactics does the technique above fall?**

> **Answer**: `Initial Access, Persistence, Defense Evasion and Privilege Escalation`

🔍 **How to find it**:
- On [MITRE ATT&CK T1078.003 page](https://attack.mitre.org/techniques/T1078/003/), check “Tactic” section.
- This sub-technique appears under **multiple tactics**, and THM expects the full list in this exact order.

---

### Q10. **What technique is the group known for using under the tactic Collection?**

> **Answer**: `Automated Collection`

🔍 **How to find it**:
- In Navigator or OpenCTI, under Tactic `Collection`, **Automated Collection** is linked to Tropic Trooper.
- This fits the USBferry behavior of gathering data from removable media.

---

## 🧠 Key Takeaways

| Phase            | Technique                        | THM Label                    |
|------------------|----------------------------------|------------------------------|
| Initial Access   | Spear-phishing, USB worm         | `spear-phishing emails`, `Replication Through Removable Media` |
| Malware          | USB-based trojan                 | `USBferry`                   |
| Malware STIX ID  | Unique UUID                      | `malware--5d0ea014-...`      |
| Tool Used        | LOLBin                           | `BITSAdmin`                  |
| Persistence/Evasion | Valid Accounts: Local          | `Local Accounts`             |
| Collection       | Auto-gather from drives          | `Automated Collection`       |

---


