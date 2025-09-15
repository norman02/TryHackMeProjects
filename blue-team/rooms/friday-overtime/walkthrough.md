
# 🧠 TryHackMe Walkthrough – Friday Overtime 



---

## 🖥️ Room Overview

You play as a Cyber Threat Intelligence Analyst at **PandaProbe Intelligence**.  
A late-Friday ticket from SwiftSpend Finance reports malware artifacts affecting over 9000 machines.  
Your tasks: extract and analyze samples, identify threat actor infrastructure, and correlate against MITRE ATT&CK.

---

## ✅ Task Answers

| # | Question | Answer |
|---|----------|--------|
| 1 | Who shared the malware samples? | `Oliver Bennett` |
| 2 | SHA1 hash of `pRsm.dll`? | `9d1ecbbe8637fed0d89fca1af35ea821277ad2e8` |
| 3 | Malware framework using these DLLs? | `MgBot` |
| 4 | MITRE ATT&CK Technique for `pRsm.dll`? | `T1123` |
| 5 | Defanged URL first seen 2020-11-02? | `hxxp[://]update[.]browser[.]qq[.]com/qmbs/QQ/QQUrlMgr_QQ88_4296[.]exe` |
| 6 | Defanged C2 IP first seen 2020-09-14? | `122[.]10[.]90[.]12` |
| 7 | MD5 of SpyAgent Android sample (June 2025)? | `951f41930489a8bfe963fced5d8dfd79` |

---

## 🔍 Key Artifacts

### 🎯 `samples.zip`
- Extracted with password: `Panda321!`
- File: `pRsm.dll`
- SHA1: `9d1ecbbe8637fed0d89fca1af35ea821277ad2e8`

### 🧪 Malware Framework
- **Identified:** MgBot  
- Modular plugins for: keylogging, audio capture, C2 comms

### 🧠 MITRE Technique
- **T1123 – Audio Capture**  
- Captures microphone input via DLL modules

### 🌐 Threat Infrastructure
- Malicious download:  
  `hxxp[://]update[.]browser[.]qq[.]com/qmbs/QQ/QQUrlMgr_QQ88_4296[.]exe`  
- C2 server (first seen 2020-09-14):  
  `122[.]10[.]90[.]12`

### 📱 Mobile Payload
- SpyAgent spyware for Android (June 2025)  
- MD5: `951f41930489a8bfe963fced5d8dfd79`

---

## 🛠️ Tools Used
- **DocIntel** (THM CTI platform)  
- **CyberChef** – URL/IP defanging  
- **MITRE ATT&CK Navigator**  
- `sha1sum`, `unzip` – static file analysis  

---

## 🧠 Reflections

This room simulates a real CTI workflow:
- Ingesting suspicious artefacts  
- Correlating hashes/domains with external intel  
- Mapping to MITRE ATT&CK  

⚠️ **Accessibility barrier**: THM’s VM lacks dark mode and is difficult for low-vision users. Core skills, however, were excellent practice in structured reporting and malware attribution.

---


---

## ✅ Room Complete

**Skills demonstrated:**

* Static malware analysis
* MITRE mapping
* Threat infrastructure correlation
* CyberChef & intel tool workflows

---

## 🔗 References

* [MITRE ATT\&CK T1123 – Audio Capture](https://attack.mitre.org/techniques/T1123/)
* ESET MgBot report (via DocIntel)
* [CyberChef – GCHQ](https://gchq.github.io/CyberChef/)


