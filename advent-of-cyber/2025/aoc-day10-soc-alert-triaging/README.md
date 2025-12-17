

# Advent of Cyber 2025 – Day 10

## SOC Alert Triaging – *Tinsel Triage* (Intentional Skip)

> **Status:** ⚠️ *Intentionally Skipped*
> **Reason:** Excessive tooling friction due to Microsoft Sentinel / Defender UI divergence
> **Outcome:** Conceptual objectives captured and documented in lieu of hands-on execution

---

## 📌 Why This Room Was Skipped

This room relies heavily on **Microsoft Sentinel’s UI and log schema**, which has **materially diverged** from the version assumed by the lab instructions:

* Sentinel incidents redirect into **Microsoft Defender XDR**
* Expected alerts and entities were **inconsistent or missing**
* KQL examples referenced **tables and fields no longer exposed**
* Navigation paths in the lab **no longer exist**
* Queries returned no results despite verified incidents

This created **tooling friction unrelated to SOC skill**, turning the exercise into a UI archaeology problem rather than a triage exercise.

**Decision:**
Rather than brute-forcing broken mechanics, this room was **skipped intentionally**, and its **intended learning outcomes were extracted, validated, and documented** below.

This mirrors real SOC practice:

> *When tools fail, analysts still reason correctly.*

---

## 🎯 What This Room Was Intended to Teach

### Core Objective

Learn how a **SOC analyst triages alerts under pressure**, prioritises threats, correlates detections, and decides on escalation — **independent of tooling quirks**.

This is a **thinking skill**, not a click-path exercise.

---

## 🧠 SOC Alert Triage Framework (Key Takeaway)

When alerts flood in, analysts evaluate them across **four dimensions**:

### 1. Severity — *How bad could this be?*

* Informational ≠ urgent
* Privilege escalation, credential access, and persistence alerts are **high priority**
* Severity guides *review order*, not verdict

### 2. Time — *Is this ongoing?*

* Recent alerts matter more than historical ones
* Repeated alerts across short windows suggest automation or persistence
* Time clustering helps identify attack phases

### 3. Context — *Where in the attack lifecycle?*

Alerts map to attacker stages:

| Stage                | Example Alert              |
| -------------------- | -------------------------- |
| Initial Access       | External SSH login         |
| Discovery            | SUID enumeration           |
| Privilege Escalation | Polkit exploit, sudo abuse |
| Persistence          | Kernel module insertion    |
| Lateral Movement     | New logins across hosts    |

Multiple stages on the **same asset** = likely compromise.

### 4. Impact — *What asset is affected?*

* Production > dev
* Internet-facing > internal
* Root/admin access > user access

---

## 🔗 Correlation Over Isolation (Critical Insight)

The room’s most important lesson:

> **Single alerts are noise.
> Correlated alerts tell the story.**

Example chain the room intended to demonstrate:

1. Root SSH login from external IP
2. SUID discovery on the same host
3. User added to sudoers
4. Kernel module installed

Individually debatable.
Together unmistakably malicious.

---

## 🔎 What “Diving Into Logs” Was Supposed to Teach

Not specific KQL syntax — but **how to reason from evidence**:

* Identify commands that don’t match normal admin behavior
* Detect privilege changes and persistence mechanisms
* Build timelines from partial data
* Validate alerts instead of trusting severity labels blindly

Examples of suspicious behaviors:

* Copying `/etc/shadow`
* Silent kernel module loads
* Root logins from unfamiliar IPs
* Users added to sudoers without ticket context

---

## 🚨 SOC Decision-Making Outcomes

After triage and correlation, analysts choose one path:

* **Escalate** → confirmed malicious activity
* **Investigate further** → insufficient evidence
* **Close/Suppress** → false positive or expected behavior

This room focused on **defensible decision-making**, not flag hunting.

---

## 🧠 Meta-Lesson (Unintended but Valuable)

This room accidentally taught a real SOC truth:

> **Tools change. Interfaces break.
> Analyst reasoning must not.**

* Azure portals evolve
* Sentinel merges into Defender
* Queries and schemas drift

But:

* Attack logic
* Kill-chain reasoning
* Correlation skills

…remain stable and transferable.

---

## ✅ Final Outcome

Although the lab execution was skipped:

* The **SOC triage mental model** was fully captured
* The **attack-chain reasoning** was understood
* The **analyst decision process** was documented
* The skip was **intentional, justified, and transparent**

This preserves learning value **without pretending broken tooling worked**.

---

## 📝 Note for Reviewers / Employers

This entry reflects **real-world SOC maturity**:

* Recognising when tools obstruct learning
* Extracting conceptual value regardless
* Documenting decisions clearly
* Avoiding performative checkbox completion

That is a stronger signal than forcing a broken lab.

