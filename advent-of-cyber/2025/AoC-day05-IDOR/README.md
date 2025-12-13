
# 🎄 Advent of Cyber 2025 – Day 5  
## IDOR – Santa’s Little IDOR

**Difficulty:** Medium  
**Focus:** Insecure Direct Object Reference (Authorization Bypass)  
**Perspective:** Web application security / AppSec / Pentesting  
**Target:** TrypresentMe web application

---

## 🧠 Objective

Learn how **Insecure Direct Object Reference (IDOR)** vulnerabilities occur, how they are exploited in practice, and why they represent a failure of **authorization**, not simply “guessable IDs”.

The goal is to identify and exploit multiple IDOR patterns while understanding how to properly remediate them.

---

## 🧭 Environment

- Target URL: `http://10.66.152.239`
- Credentials:
  - **Username:** `niels`
  - **Password:** `TryHackMe#2025`
- Tools:
  - Browser Developer Tools
  - (Optional) Burp Suite for bonus tasks

---

## 🧩 What Is IDOR?

**IDOR (Insecure Direct Object Reference)** occurs when a web application:
- accepts an object identifier from the client (e.g., user ID, record ID)
- retrieves data based on that identifier
- **fails to verify that the requester is authorized to access it**

IDOR is best understood as an **authorization bypass**, not a guessing flaw.

---

## 🔐 Authentication vs Authorization

- **Authentication:** Who are you?
- **Authorization:** What are you allowed to access?

IDOR happens when authentication succeeds but **authorization checks are missing or incomplete**.

Most IDORs are a form of **horizontal privilege escalation**:
- same role
- same features
- access to *other users’ data*

---

## 1️⃣ Initial Login

Log into the application using the provided credentials.

After login, you are presented with a dashboard showing account information and related data (children, vouchers, etc.).

This establishes a baseline:  
You are authenticated as a **normal user**.

---

## 2️⃣ Observing Object References (Network Analysis)

### Action
1. Open Developer Tools (`Inspect`)
2. Go to the **Network** tab
3. Refresh the page
4. Inspect the request for account information (e.g., `view_accountinfo`)

### Observation
The request contains a parameter such as:
```

user_id=10

```

### Why This Matters
This reveals:
- the application uses `user_id` as a direct object reference
- the client supplies this value
- the server trusts it

This is the foundation of the IDOR.

---

## 3️⃣ Client-Side Identity Storage

### Action
1. Open the **Application / Storage** tab
2. Navigate to **Local Storage**
3. Inspect stored values (e.g., `auth_user`)

You’ll find something like:
```

"user_id": 10

````

### Insight
The user’s identity reference is **stored and modifiable client-side**.

This means:
- changing the value changes how the server responds
- the server is not re-validating ownership

---

## 4️⃣ Exploiting the Basic IDOR

### Action
1. Change `user_id` from `10` to `11`
2. Save the change
3. Refresh the page

### Result
You now see **another user’s account data**.

### Why This Works
The server logic effectively does:
```sql
SELECT * FROM users WHERE user_id = <client value>;
````

There is no check to ensure:

> “Does this data belong to the authenticated user?”

This is classic IDOR.

---

## 5️⃣ Finding the Parent with 10 Children

### Goal

Identify the `user_id` of the parent who has **10 children**.

### Logic

* You already control `user_id`
* Iterate through user IDs
* Observe how many children each account has

### Action

1. Increment `user_id` values (e.g., 10 → 11 → 12 → …)
2. Refresh after each change
3. Count children displayed

The account showing **10 children** provides the answer.

---

## 6️⃣ IDOR Hidden by Encoding (Base64)

### Observation

Clicking the 👁️ icon next to a child triggers a request with a value like:

```
Mg==
```

### Analysis

`Mg==` is simply:

```
Base64("2")
```

### Key Lesson

Encoding is not security.

If the server:

* decodes the value
* uses it directly
* does not check ownership

→ IDOR still exists.

---

## 7️⃣ IDOR Hidden by Hashing (MD5)

### Observation

Clicking the ✏️ edit icon triggers a request containing what appears to be a hash.

### Insight

* The value resembles an MD5 hash
* Hashes are deterministic
* If the input and algorithm are known, hashes can be recreated

### Lesson

Hashing identifiers does **not** fix IDOR unless authorization is enforced server-side.

---

## 8️⃣ Algorithmic IDOR (UUID v1)

### Observation

Voucher codes appear random and UUID-like.

### Investigation

Decoding reveals **UUID version 1**, which includes:

* timestamp
* node information

### Risk

If the generation time window is known, valid UUIDs can be:

* predicted
* brute-forced

This is IDOR caused by **predictable identifier generation**, not weak randomness alone.

---

## 🛠️ Proper Remediation (Blue-Team Perspective)

### ❌ What Does NOT Fix IDOR

* Base64 encoding
* Hashing IDs
* UUIDs alone
* Obfuscation
* Hiding parameters in JavaScript

---

### ✅ What DOES Fix IDOR

Authorization checks on **every request**.

Example:

```sql
SELECT *
FROM children
WHERE child_id = ?
AND parent_id = <authenticated_user_id>;
```

Rules:

* Server determines access
* Client input is never trusted
* Ownership is verified per object

---

## 🧠 Key Takeaways

* IDOR is an authorization failure, not an ID format issue
* Most IDORs are horizontal privilege escalation
* Obfuscation ≠ access control
* Authorization must be enforced server-side, per request
* IDOR is one of the most common real-world web vulnerabilities

---

## 🧭 Skills Practiced

* Identifying object references in web apps
* Exploiting authorization bypasses
* Client-side vs server-side trust analysis
* Understanding IDOR variants (numeric, encoded, hashed, algorithmic)
* AppSec remediation strategies

---

## ⚠️ Ethical Note

All actions performed:

* occurred in a controlled lab
* targeted intentionally vulnerable systems
* were conducted for defensive learning purposes

Unauthorized exploitation of IDOR vulnerabilities in real applications is illegal and unethical.

---

## 🔗 Related Learning

* OWASP Top 10 – Broken Access Control
* TryHackMe: Complete IDOR Room
* Secure API Design Principles
