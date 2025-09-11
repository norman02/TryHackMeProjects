# 🛡️ TryHackMe Walkthrough – OpenCTI

## 📘 Room Overview

**OpenCTI** (Open Cyber Threat Intelligence) is an open-source platform for managing, visualizing, and enriching cyber threat intelligence. This TryHackMe room introduces OpenCTI’s structure, core features, and practical workflows for security analysts.

- 🧠 Focus: CTI, MITRE ATT&CK, Malware & APT investigations
- 🔗 Room Link: [TryHackMe – OpenCTI](https://tryhackme.com/room/opencti)

---

## 🧭 Tasks & Answers

### ✅ Task 1 – Room Overview
> _No answer required._  
Introductory overview of OpenCTI and its purpose.

---

### ✅ Task 2 – Introduction to OpenCTI
- Developed by **ANSSI** (France)
- Supports STIX 2.0+ format
- Graph-based representation of threats
- Connects to external sources: MISP, TheHive, CVE feeds, etc.

---

### ✅ Task 3 – OpenCTI Data Model
- CTI modeled using **STIX 2.0**: entities + relationships + context
- Components: GraphQL API, Workers, and Connectors

---

### ✅ Task 4 – OpenCTI Dashboard 1
1. **Which group is known to have used the 4H RAT malware?**  
   → `Maverick Panda`

2. **What kill-chain phase is the Command-Line Interface attack pattern associated with?**  
   → `execution-ics`

3. **What category tab contains indicators under activities?**  
   → `Observations`

---

### ✅ Task 5 – OpenCTI Dashboard 2
1. **Which intrusion sets are linked to Cobalt Strike (Good confidence)?**  
   → `CopyKittens, FIN7`

2. **Who is listed as the author of this entity?**  
   → `The MITRE Corporation`

---

### ✅ Task 6 – Investigative Scenario

**Topic:** Investigate the CaddyWiper malware and APT37 threat group.

#### 📌 Questions & Answers

1. **Earliest date recorded related to CaddyWiper**  
   → `2022/03/15`  
   🧠 _Based on the ESET report inside OpenCTI's knowledge tab — not the entity metadata._

2. **Attack technique used by the malware for execution**  
   → `Native API`

3. **How many malware relations are linked to this attack technique?**  
   → `113`

4. **Which 3 tools were used by the Attack Technique in 2016?**  
   → `BloodHound, Empire, ShimRatReporter`

5. **What country is APT37 associated with?**  
   → `North Korea`

6. **Which attack techniques are used by the group for initial access?**  
   → `T1189, T1566`  
   _Drive-by Compromise and Phishing (respectively)._

---

## 🧠 Analyst Notes

### 💡 Takeaways from OpenCTI
- OpenCTI presents **CTI as an interactive graph**, not just static lists.
- Malware, attack techniques, observables, and reports are all linked.
- Best used in conjunction with **ATT&CK**, **report-based analysis**, and **external tools** (EDR, SIEM, MISP).

### ⚠️ THM Caveats
- Answer validation sometimes expects **exact report phrases**, not metadata fields.
- CTI success depends on reading **source documents**, not just relying on UI entries.
- Non-technical audiences may be confused by ATT&CK technique IDs (`T1189`, `T1566`); real-world reporting should prioritize readable summaries like:
  - “Initial access occurred via phishing and drive-by compromise.”

---

## 📂 Vault Captures (Reusables)

- **Arsenal Tab** in OpenCTI = pivot point for malware → TTP → CVE → detection logic.
- **Observations Tab** = hunting ground for indicators (IOCs) and real-world detections.
- **Confidence scoring** in OpenCTI = crucial to filter noise.
- **"Author" field** ≠ attacker; may refer to data source or intel provider.

---

## 🔗 References

- [MITRE ATT&CK](https://attack.mitre.org/)
- [OpenCTI GitHub](https://github.com/OpenCTI-Platform/opencti)
- [ESET CaddyWiper Report](https://www.welivesecurity.com/en/eset-research/caddywiper-data-wiper-ukraine/)
- [[Related Cheatsheets]](../cheatsheets)  
  - MITRE ATT&CK  
  - MISP  
  - TheHive  
  - Threat Intel Tools  

---

## 🏁 Completion

🎉 **Room completed successfully!**  
Part of my progress toward becoming a SOC Analyst.


