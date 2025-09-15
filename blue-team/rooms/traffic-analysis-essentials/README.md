# 🛡️ TryHackMe – Traffic Analysis Essentials

> **Room:** [Traffic Analysis Essentials](https://tryhackme.com/room/trafficanalysisessentials)  
> **Path:** SOC Level 1  
> **Status:** ✅ *Complete*  
> **Tags:** `#tryhackme` `#soc-path` `#traffic-analysis` `#pcap` `#wireshark` `#zeek` `#snort` `#vault-worthy`

---

## 🧠 Overview

This room introduces the fundamentals of **network traffic analysis** using packet captures (PCAP files), intrusion detection systems (IDS), and common protocols (TCP, HTTP, DNS, ARP).  
It simulates real-world SOC workflows, where analysts identify threats and suspicious activity using traffic patterns.

---

## 🧰 Tools Used

| Tool       | Purpose                              |
|------------|--------------------------------------|
| Wireshark  | PCAP inspection and packet filtering |
| Zeek       | Flow-based traffic visibility        |
| tcpdump    | Command-line packet capture          |
| Snort      | Signature-based IDS analysis         |

---

## 🎯 Learning Objectives

- Understand TCP/IP fundamentals and protocol behavior
- Detect threats using packet and flow analysis
- Analyze Snort IDS alerts and Zeek logs
- Apply SOC triage strategies in hands-on simulations

---

## 📝 Walkthrough

➡️ See [`walkthrough.md`](./walkthrough.md) for full task breakdown, flag answers, and key takeaways.

---

## 🧠 Vault-Worthy Captures

- Efficient **Wireshark filters** for SOC triage
- Snort rule breakdowns and behavioral signatures
- Zeek logs as a pivot tool for flow-to-packet mapping
- Indicators of C2 behavior (e.g., ports `4444`, `7777`)
- IDS + packet correlation to find true attacker IPs

---

## ✅ Status Tracker

| Task | Title                            | Status      |
|------|----------------------------------|-------------|
| 1    | Introduction                     | ✅ Complete |
| 2    | Network Security and Network Data| ✅ Complete |
| 3    | Traffic Analysis                 | ✅ Complete |
| 4    | Conclusion                       | ✅ Complete |

---

## 📌 Notes

This repo is part of an ongoing **SOC Analyst Learning Path**.  
Feel free to fork the layout or adapt the markdown templates for your own TryHackMe journey.

---

## ⚖️ Legal & Ethical Disclaimer

This repository is intended solely for **educational purposes** as part of a structured cybersecurity learning path (e.g., TryHackMe SOC Analyst Path).  
All labs and exercises were conducted in **controlled, authorized environments** provided by the TryHackMe platform or locally simulated systems.

I do **not condone** or support any unauthorized access, intrusion, or use of tools against systems without explicit permission.  
All activities comply with the [Computer Fraud and Abuse Act (CFAA)](https://www.justice.gov/criminal-ccips/computer-fraud-and-abuse-act) and related laws.

> Always hack **ethically**. Get **consent**. Stay **legal**.

