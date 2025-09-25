
# 🛡️ TryHackMe Walkthrough – MISP

## 📌 Context

- **Platform:** TryHackMe  
- **Room:** [MISP – Malware Information Sharing Platform](https://tryhackme.com/room/misp)  
- **Path:** SOC Level 1  
- **Difficulty:** Medium  
- **Status:** ✅ Completed  
- **Author(s):** tryhackme, SecurityNomad, TactfulTurtle  
- **Tags:** `threat-intel` `misp` `soc-analyst` `cti` `walkthrough`  

---

## 🧠 Learning Objectives

- Understand what MISP is and why it matters in SOC workflows  
- Learn core concepts: Events, Attributes, Tags, Taxonomies, Galaxies  
- Navigate and use the MISP dashboard  
- Explore feed ingestion and tagging  
- Apply your skills in a real-world scenario (PupyRAT)  

---

## 🧩 Task Overview

| Task | Title                       | Summary                                         |
|------|-----------------------------|-------------------------------------------------|
| 1    | Room Overview               | Orientation and goals                           |
| 2    | MISP Introduction           | What MISP is and its key use cases              |
| 3    | Using the System            | Dashboard, event creation, attribute management |
| 4    | Feeds & Taxonomies          | Importing intel, classification via tags        |
| 5    | Scenario – PupyRAT Event    | Real-world IOC extraction task                  |
| 6    | Conclusion                  | Recap and external resources                    |

---

## ✅ Task 1 – Room Overview

MISP is a **structured threat intelligence sharing platform** for analysts, researchers, and incident responders. The TryHackMe room provides:

- A conceptual foundation for understanding MISP  
- A lab walkthrough via web access (no VM login needed)  
- A scenario-based exercise simulating SOC usage  

---

## ✅ Task 2 – MISP Introduction

**MISP** allows trusted groups to:

- Share Indicators of Compromise (IOCs)  
- Track malware, threat actors, and campaigns  
- Enrich SIEM and NIDS/HIDS with external threat data  

### Key Features

- IOC correlation  
- API access and automation  
- Event graph visualization  
- Taxonomy-based classification  
- Community-based intelligence sharing  

### Key Terminology

| Term        | Description                         |
|-------------|-------------------------------------|
| Event       | Logical grouping of threat intel    |
| Attribute   | Individual indicator (IP, hash, etc.) |
| Object      | Grouped attributes (e.g., file + hash) |
| Galaxy      | Knowledge base (APT, malware)       |
| Taxonomy    | Structured tag schema               |
| Tag         | Metadata label for filtering/search |
| Sighting    | Time-based observation of indicator |

---

## ✅ Task 3 – Using the System

### Dashboard Overview

After logging in, analysts can:

- View or create events  
- Tag, share, and publish indicators  
- Navigate taxonomies and galaxies  

### Event Lifecycle

1. **Create Event** – title, threat level, org scope  
2. **Add Attributes** – IPs, hashes, domains, uploads  
3. **Publish** – shared by admin with proper distribution scope  

### Key Q&A

- **Q: How many distribution options exist?**  
  **A:** 4  
- **Q: Who publishes the event?**  
  **A:** Organisation Admin  

---

## ✅ Task 4 – Feeds & Taxonomies

### Feeds

- External intel sources (e.g. CIRCL, abuse.ch)  
- Admins configure; analysts can **preview/import**

### Tags & Taxonomies

- Machine-readable tagging format:  
  `namespace:predicate="value"`  
  Example: `tlp:color="amber"`

- Used for classification, interoperability, and filtering

### Tagging Best Practices

- Use event-level tags by default  
- Attribute-level tags only for overrides  
- Keep taxonomy sets lean and meaningful  

---

## ✅ Task 5 – Scenario: PupyRAT Investigation

> Investigate a real-world MISP event from CIRCL on **PupyRAT**, a known RAT used by APT groups.

| Item                                | Value                           |
|-------------------------------------|----------------------------------|
| Event ID                            | `1145`                          |
| Threat Vector                       | `remote access`                 |
| C2 IP Address                       | `89.107.62.39`                  |
| Threat Actor (Galaxy)              | `Magic Hound`                   |
| Taxonomy Tag (Certainty)           | `osint:certainty="50"`         |

---

## ✅ Task 6 – Conclusion

This room provided hands-on practice with:

- Creating and managing events  
- Ingesting structured intelligence via feeds  
- Tagging and classifying data  
- Real-world threat correlation with Galaxy mapping  

### Recommended Resources

- 📘 [MISP Book](https://www.misp-project.org/book/)  
- 💾 [MISP GitHub](https://github.com/MISP/MISP)  
- 🎓 [CIRCL Training Modules](https://www.circl.lu/services/misp-training/)  


