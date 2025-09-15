# 🕵️ TryHackMe Walkthrough – Traffic Analysis Essentials

## 📌 Context
- **Room:** [Traffic Analysis Essentials](https://tryhackme.com/room/trafficanalysisessentials)
- **Path:** SOC Level 1
- **Status:** ✅ Complete
- **Tags:** `#tryhackme` `#soc-path` `#traffic-analysis` `#blue-team` `#network-security`
- **Repo Path:** `~/TryHackMeProjects/soc-path/traffic-analysis-essentials/walkthrough.md`

---

## 🗂️ Task Breakdown

### ✅ Task 1 – Introduction
No flag. Room spun up successfully.

---

### ✅ Task 2 – Network Security and Network Data

#### 🔍 Key Concepts

##### 🧱 Base Control Levels

| Level          | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Physical       | Prevents unauthorized physical access to network infrastructure             |
| Technical      | Controls access to data (e.g., VPNs, tunnels, NAC)                          |
| Administrative | Defines policies and authentication procedures                              |

##### 🛡️ Security Approaches

- **Access Control**: Authentication and authorization of users/devices  
- **Threat Control**: Detecting and preventing malicious activity

##### 🔐 Access Control Elements

- **Firewall** – Blocks unauthorized traffic based on rules  
- **NAC** – Validates device compliance before granting access  
- **IAM** – Manages user identities and access  
- **Load Balancer** – Distributes data based on traffic metrics  
- **Network Segmentation** – Isolates devices for granular control  
- **VPN** – Secures communications via encryption  
- **Zero Trust** – "Never trust, always verify" principle

##### ⚠️ Threat Control Elements

- **IDS/IPS** – Detects and/or blocks malicious traffic  
- **DLP** – Prevents exfiltration of sensitive data  
- **Endpoint Protection** – Combines AV, DLP, and more  
- **SIEM** – Centralizes and correlates logs/events  
- **SOAR** – Automates incident response across tools  
- **NTA/NDR** – Analyzes traffic for unusual behavior

##### 🛠 Managed Security Services (MSS)

MSSPs offer outsourced services like:
- Vulnerability assessment
- Pen testing
- Behavioral analysis
- Incident response

#### 🧠 Vault Highlights

- **Zero Trust** is a mindset, not a feature toggle  
- **SOAR** is essential for high-volume alert environments  
- Distinction between **Access** and **Threat** control is useful in incident triage  
- **SIEM** = the analyst’s radar system for modern SOCs

#### ✅ Answers

> Q1: Which Security Control Level covers creating security policies?  
**Answer:** `Administrative`

> Q2: Which Access Control element works with data metrics to manage data flow?  
**Answer:** `Load Balancing`

> Q3: Which technology helps correlate different tool outputs and data sources?  
**Answer:** `SOAR`

---

### ✅ Task 3 – Traffic Analysis

#### 🧠 Summary

Traffic Analysis involves observing network data (flows or packets) to detect anomalies or suspicious patterns. It supports core blue-team tasks including:

| Subdiscipline         | Covered In        |
|------------------------|------------------|
| Packet Sniffing        | Wireshark room   |
| Flow Monitoring        | Zeek room        |
| IDS/IPS                | Snort room       |
| Network Forensics      | NetworkMiner     |
| Threat Hunting         | Brim room        |

#### 🔍 Techniques

| Method          | Pros                                           | Cons                              |
|------------------|--------------------------------------------------|------------------------------------|
| **Flow Analysis**  | Lightweight, fast, good for baselining          | Lacks payloads or fine-grain data  |
| **Packet Analysis**| Deep inspection, reveals root causes            | Slower, requires expertise         |

#### ✅ Benefits

- Reveals threats even in **encrypted** traffic (via patterns/timings)
- Enables **baselining** for anomaly detection
- Critical for real-world SOC triage and investigation

---

### 🧪 Simulation Results

#### 🔐 Level 1 – Malicious IPs Only

- Identified attackers:
  - `10.10.99.99` → Metasploit traffic
  - `10.10.99.62` → “Bad Traffic”
- ✅ **Flag:** `THM{PACKET_MASTER}`

#### 🔐 Level 2 – IP + Port Filtering

- Suspicious Ports:
  - `4444` (Metasploit reverse shell)
  - `7777`, `2222` (often seen in C2 frameworks)
- ✅ **Flag:** `THM{DETECTION_MASTER}`

#### 🧠 Vault Highlights

- Attacker traffic often hides in plain sight via **weird port usage**
- **Correlate** IDS alerts with actual flow direction: source vs. destination
- Even without payloads, timing, ports, and metadata can reveal compromise

---

## ✅ Room Complete!

🔖 This room solidified key Tier 1 SOC analyst skills:
- Differentiating between flow and packet inspection
- Recognizing common attack patterns
- Applying traffic filtering logic in real-world scenarios


