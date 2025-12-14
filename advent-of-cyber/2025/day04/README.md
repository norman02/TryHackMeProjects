
# 🎄 Advent of Cyber 2025 – Day 4  
## AI in Security – *old sAInt nick*

**Difficulty:** Easy  
**Focus:** Practical uses and limitations of AI in cyber security  
**Perspective:** Human-in-the-loop security workflows  
**Tools:** AI assistant (Van SolveIT), Python, HTTP exploitation

---

## 🧠 Objective

Explore how AI can be used in cyber security workflows across:
- **Offensive security** (exploit generation)
- **Defensive security** (log analysis)
- **Secure software development** (code review)

The goal is not to “let AI do security,” but to understand **where AI helps, where it fails, and why human judgment is mandatory**.

---

## 🧭 Environment

- Target Machine IP: `10.65.135.4`
- Vulnerable Web App: `http://10.65.135.4:5000`
- AI Showcase UI: `http://10.65.135.4`
- Execution Environment: TryHackMe AttackBox

---

## 1️⃣ AI Showcase Overview (Van SolveIT)

The room uses an interactive AI assistant, **Van SolveIT**, to demonstrate three use cases:

| Stage | Security Domain | Purpose |
|-----|-----------------|---------|
| Red | Offensive Security | Generate and use an exploit |
| Blue | Defensive Security | Analyse attack logs |
| Software | AppSec | Identify code vulnerabilities |

Each stage unlocks sequentially. Completing all stages presents the **showcase completion flag**.

---

## 2️⃣ Red Team Stage – AI-Generated Exploit

### What the AI Provides
- A Python exploit script targeting a vulnerable login endpoint
- Intended to demonstrate how AI can accelerate exploit development

### Analyst Logic
AI can draft exploit code quickly, but:
- output must be reviewed
- target configuration must be verified
- execution errors are the human’s responsibility

---

### Save the Exploit Script
```bash
mkdir -p ~/aoc/day04
cd ~/aoc/day04
vi exploit.py
````

Paste the script provided by the AI.

---

### Critical Fix: Target Formatting

The script contains a placeholder for the target IP/URL.
It **must** be set correctly:

```text
http://10.65.135.4:5000
```

A common failure mode (observed here) was an invalid IP format using commas instead of dots, which caused DNS resolution errors.

---

### Execute the Exploit

```bash
python3 exploit.py
```

If required:

```bash
python3 -m pip install --user requests
```

---

### Result

* HTTP 200 response
* Successful authentication bypass via SQL injection
* Flag returned in the HTTP response body

This answers the room’s second question regarding exploit execution output.

---

## 3️⃣ Blue Team Stage – Log Analysis (Conceptual)

In the Blue stage, the AI explains how defenders can use AI to:

* process large volumes of logs
* detect abnormal behaviour
* add context to alerts

### Key Takeaway

AI excels at **speed and scale**, but:

* does not understand business impact
* cannot reliably judge intent
* must be supervised to avoid false positives or missed incidents

This mirrors real SOC tooling (AI-assisted SIEM, EDR, IDS).

---

## 4️⃣ Software Stage – Code Analysis

The Software stage demonstrates AI-assisted secure development:

* identifying vulnerabilities in source code
* acting as a SAST/DAST-style assistant
* providing suggestions and explanations

### Important Limitation

AI is often **better at finding vulnerabilities than writing secure code**.

Generated code:

* may compile
* may “work”
* but often lacks secure defaults or proper validation

Human review remains essential.

---

## 5️⃣ AI Showcase Completion

After completing:

* Red stage
* Blue stage
* Software stage

Van SolveIT presents the **showcase completion flag**, which answers the room’s first question.

---

## 🧠 Core Lessons Learned

### AI Is an Accelerator, Not an Authority

AI can:

* generate code
* summarize logs
* suggest next steps

AI cannot:

* validate scope
* ensure safety
* reason about unintended consequences

---

### Human-in-the-Loop Is Mandatory

Correct security workflow:

1. AI suggests
2. Human reviews
3. Human executes
4. Human validates
5. Human decides

Removing the human from this loop introduces unacceptable risk.

---

### Real-World Relevance

The failures observed in this room mirror real issues:

* subtle AI-generated bugs
* confident but incorrect output
* brittle behaviour outside expected paths

These are not theoretical problems — they already exist in production environments.

---

## 🧭 Skills Practiced

* Safe execution of AI-generated exploit code
* Debugging Python and HTTP errors
* Understanding AI’s role in SOC workflows
* Critical evaluation of AI output
* Ethical handling of offensive tooling

---

## ⚠️ Ethical Note

All actions in this room:

* occur in a controlled lab
* target intentionally vulnerable systems
* are performed for defensive learning

Unsupervised or unauthorized use of AI-generated exploits in real environments is unethical and illegal.

---

## 🔗 Related Learning

* Defending Adversarial Attacks (TryHackMe)
* Secure AI governance
* SOC automation best practices
