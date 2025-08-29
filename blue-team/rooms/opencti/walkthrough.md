# 🛡️ TryHackMe Walkthrough – OpenCTI  
**Path:** SOC Analyst 1  
**Difficulty:** Medium  
**Status:** In Progress  
**VM IP:** `10.201.73.176`  
**Start Date:** 2025-08-29

---

## 📘 Room Summary

OpenCTI (Open Cyber Threat Intelligence) is an open-source platform for managing, visualizing, and enriching cyber threat intelligence. This room introduces OpenCTI's structure, features, and practical workflows for security analysts, mapped closely to MITRE ATT&CK concepts.

---

## ✅ Task 1 – Room Overview

> **Q:** _Read the above._  
> **A:** _No answer required._

This room introduces:
- What OpenCTI is and how it’s used
- How to navigate the platform
- Functionalities relevant to SOC workflows

**Suggested Prerequisite Rooms**:
- MITRE ATT&CK Framework  
- MISP  
- TheHive  
- Threat Intelligence Tools

---

## ✅ Task 2 – Introduction to OpenCTI

OpenCTI is an open-source platform developed by **ANSSI** (France’s national cybersecurity agency) to manage **Cyber Threat Intelligence (CTI)** in a structured, relational format.

### 🔍 Key Objectives
- Centralize threat data — collect, analyze, and visualize campaigns, malware, indicators (IOCs), TTPs
- Link entities together — e.g., Threat Actor → Campaign → Malware → Victim
- Visual analysis — graph-based dashboards with rich context
- Framework support — integrates **MITRE ATT&CK**, MISP, and TheHive
- Handles both technical and strategic data — connects tactical observables with high-level intel

> 💡 _OpenCTI isn’t just a database — it’s a **living graph** of threats and their ecosystem._

---

## ✅ Task 3 – OpenCTI Data Model

OpenCTI uses the **STIX 2.0+ standard** as its core data modeling framework.

### 🧠 What is STIX?
> **Structured Threat Information Expression (STIX)** is a standardized language for cyber threat intelligence (CTI) sharing.  
> It enables consistent expression of indicators, threat actors, attack patterns, malware, and their **relationships**.

> Think of it as:  
> `Entities` + `Relationships` + `Source/Context` = **A full intelligence graph**

---

### 🏗️ OpenCTI Architecture (Highlights)

| Component        | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| **GraphQL API**  | Interfaces with clients (frontend/backend) to query threat data      |
| **Write Workers**| Python workers that write queries asynchronously via RabbitMQ        |
| **Connectors**   | Plugin-like modules to ingest, enrich, import, or export data        |

---

### 🔌 Connector Types

| Class                       | Description                                         | Examples                      |
|----------------------------|-----------------------------------------------------|-------------------------------|
| External Input Connector   | Ingests data from external sources                  | MISP, MITRE, TheHive, CVE     |
| Stream Connector           | Consumes the platform’s data stream                 | Tanium, History               |
| Internal Enrichment        | Adds context to entities (from user action)         | Observable enrichment         |
| Internal Import File       | Extracts intel from user-uploaded files             | STIX2 files, PDFs             |
| Internal Export File       | Exports entities/data into different formats        | STIX2 export, CSV, PDF        |

> 🔍 These connectors are how OpenCTI **talks to other tools**, enriching and transforming raw data into a usable graph of knowledge.

---

## 🔄 Task 4 – OpenCTI Dashboard 1

🖥️ **Access Dashboard:** `http://10.201.73.176:8080`  
🔐 **Credentials:**  
- **Username:** `info@tryhack.io`  
- **Password:** `TryHackMe1234`

Give the machine a few minutes to initialize. Log in via AttackBox in fullscreen.

### Key Panels:
- **Activities**: Ingested incidents (reports, investigations)  
- **Knowledge**: Linked entities (Tools, Victims, Threat Actors)  
- **Analysis**: Imported reports (e.g., MITRE Triton), notes, references  
- **Events**: Incidents & response timelines  
- **Observations**: Indicators & detections (IP, hash, etc.)  
- **Threats**: Actors, Intrusion Sets, Campaigns  
- **Arsenal**: Malware, TTPs, CoAs, Vulnerabilities  
- **Entities**: Geopolitical and organizational targets

---

### ✅ Questions
> **Q1:** What is the name of the group that uses the 4H RAT malware?  
> **A:** _[To be confirmed in-lab]_  

> **Q2:** What kill-chain phase is linked with the Command-Line Interface Attack Pattern?  
> **A:** `Execution`  

> **Q3:** Within the Activities category, which tab would house the Indicators?  
> **A:** `Observations`

---

## 🧠 Vault Captures (so far)
- OpenCTI = Visual knowledge graph for cyber threat intel  
- Arsenal tab = useful for detection rule context (malware, TTPs, CVEs)  
- Courses of Action = direct countermeasures to mapped techniques  
- STIX model enables traceability, enrichment, and standardized sharing of TI  

---

## 🔗 Related Tools
- [OpenCTI Documentation](https://www.opencti.io/)  
- [STIX 2.1 Standard](https://oasis-open.github.io/cti-documentation/stix/intro.html)  
- [MITRE ATT&CK Navigator](https://attack.mitre.org/)  
- [TheHive Project](https://thehive-project.org/)  
- [MISP Threat Sharing](https://www.misp-project.org/)

---

## 📅 Timeline
- Started: 2025-08-29  
- In Progress: ✅ Tasks 1–3 complete, 🔄 Task 4 in progress

