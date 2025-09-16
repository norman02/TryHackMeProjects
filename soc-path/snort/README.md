# 🛡️ TryHackMe – Snort

## 📌 Overview
This repository contains notes, walkthroughs, and artifacts from the **TryHackMe Snort room** (SOC Level 1 → Network Security and Traffic Analysis).  
The room covers the basics of using **Snort** as an Intrusion Detection/Prevention System (IDS/IPS), including:  

- Running Snort in multiple modes (Sniffer, Packet Logger, IDS/IPS, PCAP Analysis).  
- Investigating live and captured network traffic.  
- Writing and applying Snort rules.  
- Understanding Snort’s packet processing and detection logic.  

---

## 📂 Repo Structure
```plaintext
snort/
├── notes/
│   └── walkthrough.md      # Detailed step-by-step room notes
└── README.md               # This file
````

---

## 🚀 Key Commands

Common Snort usage patterns learned in this room:

```bash
# Check version / help
snort -V
snort -h

# Sniffer mode
snort -v       # TCP/IP headers only
snort -vd      # Headers + packet data
snort -vde     # Headers + packet data + application data

# Packet logger mode
snort -dev -l ./log

# IDS/IPS mode
snort -c /etc/snort/snort.conf -i eth0

# PCAP investigation
snort -r capture.pcap
```

---

## 📝 Rule Structure

General syntax:

```
action proto src_ip src_port -> dst_ip dst_port (options)
```

**Example:**

```
alert tcp any any -> 192.168.1.0/24 80 (msg:"WEB traffic detected"; sid:1000001;)
```

---

## 🔗 Related

* [Snort Official Site](https://www.snort.org/)
* [Cisco Talos Blog](https://blog.talosintelligence.com/)
* TryHackMe Room: [Snort](https://tryhackme.com/room/snort)

---

## 🧠 Reflections

* Snort provides a practical bridge between **network traffic analysis** and **detection engineering**.
* Writing Snort rules builds intuition for **IDS logic**, which maps well to **Sigma** and **YARA** rule creation.
* Useful for both **SOC analyst workflows** (monitoring, alert triage) and **red team simulation** (understanding what defenders see).

