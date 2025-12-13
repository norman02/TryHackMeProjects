
# 🎄 Advent of Cyber 2025 – Day 3  
## Splunk Basics: *Did you SIEM?*

**Difficulty:** Medium  
**Focus:** SIEM fundamentals, log analysis, attack chain reconstruction  
**Tools:** Splunk (Search & Reporting)

---

## 🧠 Objective

Investigate a suspected web-based intrusion using pre-ingested Splunk logs.  
Identify the attacker, reconstruct the kill chain, and quantify impact using **web traffic** and **firewall logs**.

---

## 🗂️ Data Sources

| Sourcetype | Description |
|-----------|-------------|
| `web_traffic` | HTTP requests to the web server |
| `firewall_logs` | Allowed/blocked network connections |

The compromised web server has an internal IP of `10.10.1.5`.

---

## 1️⃣ Initial Data Validation

Start broad to confirm data ingestion:

```spl
index=main
````

This confirms:

* logs are present
* available sourcetypes
* field extraction is working

---

## 2️⃣ Focus on Web Traffic

Web logs are the primary source for:

* reconnaissance
* exploitation
* payload delivery

```spl
index=main sourcetype=web_traffic
```

Key fields observed:

* `client_ip`
* `user_agent`
* `path`
* `status`

---

## 3️⃣ Identify the Attack Window

Count events per day to locate abnormal spikes:

```spl
index=main sourcetype=web_traffic
| timechart span=1d count
```

Sorting by volume highlights a clear **peak traffic day**, indicating the main attack phase.

---

## 4️⃣ Reduce Noise (Filter Normal Users)

Attackers typically do not use full browser user agents.
Exclude common browsers to isolate automated tooling:

```spl
sourcetype=web_traffic
user_agent!=*Mozilla*
user_agent!=*Chrome*
user_agent!=*Safari*
user_agent!=*Firefox*
```

---

## 5️⃣ Identify the Primary Attacker IP

Group suspicious traffic by source IP:

```spl
sourcetype=web_traffic
user_agent!=*Mozilla*
user_agent!=*Chrome*
user_agent!=*Safari*
user_agent!=*Firefox*
| stats count by client_ip
| sort -count
| head 5
```

One IP clearly dominates malicious activity and becomes the focus of the investigation.

---

## 6️⃣ Reconnaissance Activity

Check for probing of exposed or sensitive configuration files:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND path IN ("/.env", "/*phpinfo*", "/.git*")
| table _time path user_agent status
```

These requests indicate early-stage reconnaissance.

---

## 7️⃣ Enumeration & Path Traversal Attempts

Attackers often test for directory traversal and redirect flaws:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND (path="*../*" OR path="*redirect*")
| table _time path user_agent status
```

This confirms automated vulnerability testing.

---

## ⚠️ Important Distinction: Sensitive vs Generic Traversal

Not all traversal attempts represent equal risk.

### ❌ Overbroad (incorrect for this question)

Counting *all* `../` requests inflates results with noise.

### ✅ Correct Interpretation

Count **only traversal attempts targeting sensitive system files**, such as:

* `/etc/passwd`
* `/etc/shadow`
* `/proc/self/environ`
* `/etc/hosts`

To identify these, enumerate traversal targets:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND path="*../*"
| stats count by path
| sort -count
```

Then count only traversal events aimed at sensitive files:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND (
  path="*../*etc/passwd*" OR
  path="*../*etc/shadow*" OR
  path="*../*proc/self/environ*" OR
  path="*../*etc/hosts*"
)
| stats count
```

This produces the correct value for
**“path traversal attempts to access sensitive files.”**

---

## 8️⃣ SQL Injection Detection

Identify automated SQL injection tooling:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND (user_agent="*sqlmap*" OR user_agent="*Havij*")
| table _time path user_agent status
```

Tool-specific user agents and time-based payloads confirm exploitation.

---

## 9️⃣ Post-Exploitation & RCE

Look for webshell usage and payload execution:

```spl
sourcetype="web_traffic" client_ip="<ATTACKER_IP>"
AND (path="*shell.php?cmd=*" OR path="*bunnylock.bin*")
| table _time path user_agent status
```

This confirms **remote code execution** on the web server.

---

## 🔟 Command & Control (C2) Correlation

Pivot to firewall logs to confirm outbound attacker communication:

```spl
sourcetype=firewall_logs
src_ip="10.10.1.5"
AND dest_ip="<ATTACKER_IP>"
AND action="ALLOWED"
| table _time protocol src_ip dest_ip dest_port reason
```

Correlation across log sources proves compromise.

---

## 1️⃣1️⃣ Data Exfiltration Volume

Quantify impact by summing outbound data:

```spl
sourcetype=firewall_logs
src_ip="10.10.1.5"
AND dest_ip="<ATTACKER_IP>"
AND action="ALLOWED"
| stats sum(bytes_transferred)
```

This represents confirmed data exfiltration.

---

## 🧠 Key Takeaways

* SIEM analysis is about **intent**, not just pattern matching
* Filtering noise is essential before counting events
* Correlating multiple log sources converts suspicion into proof
* Question wording matters — “sensitive files” ≠ “all traversal”

---

## 🧭 Skills Practiced

* Log scoping and noise reduction
* Behavioral attack analysis
* Web → firewall correlation
* Incident impact quantification
* Analyst-level interpretation of SIEM data

---

## 🔗 Related Learning

* Incident Handling with Splunk (TryHackMe)
* MITRE ATT&CK: Initial Access → Execution → C2
