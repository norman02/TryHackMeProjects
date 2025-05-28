# JWT Security - TryHackMe Challenge

## Overview
This repository documents my progress through the **JWT Security** room on TryHackMe. The room covers **common vulnerabilities in JSON Web Tokens (JWTs)** and how to exploit or mitigate them.

## Structure
```
📂 thm/JWT_Security  
 ├── 📜 README.md - This file  
 ├── 📜 Write_Up.md - Detailed challenge walkthrough  
 ├── 📂 supporting_docs  
 │   ├── 🛠 configs - Configuration files  
 │   ├── 🖼 images - Screenshots and references  
 │   ├── 📝 notes - General notes and findings  
 │   ├── 🔎 scans - Security scans and enumeration results  
 │   ├── 💻 scripts - Exploitation scripts  
```

## Challenge Topics
- JWT signature validation and common pitfalls
- Algorithm downgrade attacks
- Weak secret key exploitation
- Cross-service relay attacks
- Securing JWTs effectively

## Tools Used
- [jwt.io](https://jwt.io/) (for decoding tokens)
- [hashcat](https://hashcat.net/) (for cracking weak JWT secrets)
- Burp Suite (for manipulating JWT headers)
- TryHackMe's built-in attack environment

## Progress & Write-Up
All findings and methodology will be documented in `Write_Up.md`. Stay tuned for updates!



