
# 🎄 Advent of Cyber 2025 – Day 2  
## Phishing – Merry Clickmas

**Difficulty:** Easy  
**Focus:** Social engineering fundamentals, phishing delivery, credential harvesting  
**Tools:** Social-Engineer Toolkit (SET), Python phishing server  
**Perspective:** Red-team simulation for awareness and defense

---

## 🧠 Objective

Simulate a phishing attack to demonstrate how social engineering can be used to harvest user credentials.  
The goal is to understand **how phishing campaigns are built**, delivered, and why they succeed — not to exploit real users.

---

## 🧍 Social Engineering Background

Social engineering targets **humans rather than systems**.  
Successful attacks often rely on psychological triggers such as:

- urgency
- authority
- curiosity
- familiarity

Phishing is one of the most common social-engineering techniques and can be delivered via:
- email
- SMS (smishing)
- voice (vishing)
- QR codes (quishing)
- social media messages

---

## 🪤 Attack Scenario Overview

- Target: TBFC (Toy Factory) staff
- Goal: Capture login credentials
- Method:
  - Host a fake login page
  - Deliver the link via a realistic phishing email
- Tooling:
  - Custom Python phishing server
  - Social-Engineer Toolkit (SET) for email delivery

All activity occurs **inside the TryHackMe lab environment**.

---

## 1️⃣ Prepare the Phishing Web Server

The provided phishing server hosts a fake TBFC login page and captures submitted credentials.

### Navigate to the task directory
```bash
cd ~/Rooms/AoC2025/Day02
````

### Start the phishing server

```bash
./server.py
```

Expected output:

```text
Starting server on http://0.0.0.0:8000
```

### Why this matters

* `0.0.0.0` means the server listens on all interfaces
* Port `8000` hosts the fake login page
* Any submitted credentials are printed directly to the terminal

You can preview the page by visiting:

* `http://127.0.0.1:8000`
* or `http://<CONNECTION_IP>:8000`

---

## 2️⃣ Deliver the Phishing Email with SET

Sending phishing emails from a personal account is unrealistic and ineffective.
Instead, we use **SET (Social-Engineer Toolkit)** to craft a believable message.

### Launch SET

```bash
setoolkit
```

---

## 3️⃣ Navigate SET Menus

### Select Social Engineering Attacks

```text
1) Social-Engineering Attacks
```

### Select Mass Mailer Attack

```text
5) Mass Mailer Attack
```

### Choose Single Target Email

```text
1) E-Mail Attack Single Email Address
```

---

## 4️⃣ Configure Email Delivery

Key inputs (example values shown):

* **Send email to:** `factory@wareville.thm`
* **Delivery method:** Use your own server or open relay
* **From address:** `updates@flyingdeer.thm`
* **From name:** `Flying Deer`
* **SMTP server:** `<MACHINE_IP>`
* **Port:** `25`
* **High priority:** No
* **Attachments:** None

### Why these choices work

* The sender matches a trusted shipping partner
* No attachments reduces suspicion
* Direct SMTP delivery increases realism
* The email context fits normal business operations

---

## 5️⃣ Craft the Phishing Message

### Subject example

```
Shipping Schedule Changes
```

### Body example

```
Dear elves,

Kindly note that there have been significant changes to the shipping schedules
due to increased shipping orders.

Please confirm the new schedule by visiting:
http://<CONNECTION_IP>:8000

Best regards,
Flying Deer
END
```

Type `END` on a new line to send the message.

SET confirms successful delivery.

---

## 6️⃣ Capture Credentials

Return to the terminal running `server.py`.

Within a short time, submitted credentials appear in plaintext, confirming:

* the phishing email was convincing
* the target user interacted with the fake login page

This demonstrates how easily credentials can be lost without awareness training.

---

## 7️⃣ Post-Phish Validation

Using the harvested credentials:

* Access the TBFC portal
* Check whether password reuse occurs on other services (e.g., email portal)

This highlights a common real-world issue:

> **Credential reuse significantly amplifies phishing impact.**

---

## 🧠 Key Takeaways

### Red-Team Perspective

* Phishing success depends more on psychology than technology
* Realistic context and trusted senders dramatically increase success rates
* Tooling like SET lowers the barrier to entry for attackers

### Blue-Team / Defensive Perspective

* User awareness training is critical
* Password reuse greatly increases blast radius
* Email filtering alone is insufficient
* MFA would significantly reduce impact

---

## 🧭 Skills Practiced

* Ethical social engineering simulation
* Phishing infrastructure setup
* Email delivery using SET
* Credential harvesting mechanics
* Understanding attacker mindset

---

## ⚠️ Ethical Reminder

All activities in this room are performed:

* in a controlled lab
* against simulated targets
* for defensive learning purposes

Unauthorized phishing in real environments is illegal and unethical.

---

## 🔗 Related Learning

* Phishing Prevention (TryHackMe)
* Security Awareness Training
* Credential Hygiene & MFA
