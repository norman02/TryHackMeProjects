# Mr Robot — Walkthrough (Spoiler‑Light)

## Target
robot.thm

## Plan
1) **Nmap quick**: `nmap -sC -sV -oN scans/initial.txt <IP>`
2) **Web enum**: `robots.txt`, Dirb/Gobuster
3) **Creds**: harvest site wordlist, prepare brute
4) **Foothold**: login + reverse shell
5) **Privesc**: standard checks (`sudo -l`, SUID, PATH abuse)

## Findings
- Services:
- Web dirs:
- Creds/wordlist:

## Commands
```bash
# paste key commands here for reproducibility

