
# TryHackMe — Snort Walkthrough



---

## Task 1 – Introduction
No answer required.

---

## Task 2 – Interactive Material & VM
**Challenge:** Run the `./.easy.sh` script inside the `Task-Exercise` folder.  

✅ Output: `Too Easy!`

---

## Task 3 – IDS/IPS Basics

### IDS vs IPS Types

| Category        | IDS        | IPS        |
|-----------------|------------|------------|
| Passive         | Detects    | —          |
| Active          | —          | Blocks     |
| Host-based      | HIDS       | HIPS       |
| Network-based   | NIDS       | NIPS       |
| Behavior-based  | —          | NBA        |
| Wireless        | —          | WIPS       |

### Detection Techniques
- **Signature-based** → Match against known attack signatures  
- **Behavior-based (NBA)** → Detect anomalies based on baseline  
- **Policy-based** → Compare to defined security policies  

---

## Task 5 – Operation Mode 1: Sniffer Mode

**Goal:** Inspect live traffic in Sniffer mode.  

### Commands
```bash
sudo snort -v       # Basic sniffing
sudo snort -v -i eth0  # Specific interface
sudo snort -vd      # With payloads
sudo snort -vde     # Payload + Ethernet headers
sudo snort -X       # Full hex dump
````

**Notes:**

* Must generate active traffic
* `CTRL+C` stops sniffing and shows packet summary
* Warnings like `No preprocessors configured for policy 0` are expected

---

## Task 6 – Operation Mode 2: Packet Logger Mode

**Goal:** Record and analyze traffic in logs.

### Logging

```bash
sudo snort -dev -l .        # Binary logs
sudo snort -dev -K ASCII -l .  # ASCII logs
```

Run in parallel:

```bash
sudo ./traffic-generator.sh
```

### Reviewing Logs

```bash
sudo snort -r snort.log.<timestamp>
sudo snort -r snort.log.<timestamp> -n 10
sudo snort -r snort.log.<timestamp> 'udp and port 53'

# Using tcpdump
sudo tcpdump -r snort.log.<timestamp> -ntc 10
```

### Binary vs ASCII Output

| Format | Characteristics                                             |
| ------ | ----------------------------------------------------------- |
| Binary | Single `.log` file, must be read by Snort/tcpdump/Wireshark |
| ASCII  | Human-readable, split by IPs/protocols                      |

**ASCII directory example:**

```
./145.254.160.237/
├── ICMP_ECHO
├── UDP:36648-53
├── UDP:40757-53
├── TCP:12345-80
```

---

## Task 7 – Operation Mode 3: IDS/IPS

### Useful Parameters

| Param | Description                                               |
| ----- | --------------------------------------------------------- |
| `-c`  | Specify config file                                       |
| `-T`  | Test config file                                          |
| `-N`  | Disable logging                                           |
| `-D`  | Run in daemon mode                                        |
| `-A`  | Set alert mode (`full`, `fast`, `console`, `cmg`, `none`) |

---

## Task 8 – Operation Mode 4: PCAP Investigation

Snort can analyze PCAPs to generate traffic stats and alerts.

| Param                  | Description                      |
| ---------------------- | -------------------------------- |
| `-r` / `--pcap-single` | Read a single pcap               |
| `--pcap-list`          | Read multiple pcaps              |
| `--pcap-show`          | Show pcap name during processing |

---

## Task 9 – Snort Rule Structure

### Rule Components

* **Action** → `alert`, `log`, `drop`, `reject`
* **Protocol** → IP, TCP, UDP, ICMP
* **IP/Port** → Define source/destination + ports
* **Options** → Define conditions (payload/non-payload)

### Examples

**IP-based filters:**

```snort
alert icmp 192.168.1.56 any <> any any (msg:"ICMP from host"; sid:100001; rev:1;)
alert icmp 192.168.1.0/24 any <> any any (msg:"ICMP from subnet"; sid:100002; rev:1;)
alert icmp !192.168.1.0/24 any <> any any (msg:"ICMP not from subnet"; sid:100003; rev:1;)
```

**Port-based filters:**

```snort
alert tcp any any <> any 21 (msg:"FTP detected"; sid:100010; rev:1;)
alert tcp any any <> any 1:1024 (msg:"System ports activity"; sid:100011; rev:1;)
alert tcp any any <> any !21 (msg:"Non-FTP traffic"; sid:100012; rev:1;)
```

---

### Rule Options

**Metadata:**

* `msg` → Rule description
* `sid` → Snort Rule ID (`>=1,000,000` for user rules)
* `rev` → Revision number
* `reference` → CVE or external doc link

```snort
alert icmp any any <> any any (msg:"ICMP Packet"; sid:1001000; reference:cve,CVE-XXXX; rev:1;)
```

**Payload detection:**

```snort
alert tcp any any <> any 80 (msg:"HTTP GET"; content:"GET"; sid:1001001; rev:1;)
alert tcp any any <> any 80 (msg:"HTTP GET nocase"; content:"GET"; nocase; sid:1001002; rev:1;)
alert tcp any any <> any 80 (msg:"HTTP GET with www"; content:"GET"; fast_pattern; content:"www"; sid:1001003; rev:1;)
```

**Non-payload detection:**

```snort
alert tcp any any <> any any (msg:"SYN Packet"; flags:S; sid:1002000; rev:1;)
alert ip any any <> any any (msg:"Payload size 100-300"; dsize:100<>300; sid:1002001; rev:1;)
alert ip any any <> any any (msg:"SameIP Test"; sameip; sid:1002002; rev:1;)
```

---

## 📖 Key Takeaways

* Snort operates in **four modes**: Sniffer, Logger, IDS/IPS, PCAP analysis.
* Binary logs are efficient but need Snort/tcpdump; ASCII logs are human-readable.
* Rule creation is the backbone of Snort: actions, protocol, IPs/ports, and conditions.
* Useful for both blue team defense and red team evasion training.

---


