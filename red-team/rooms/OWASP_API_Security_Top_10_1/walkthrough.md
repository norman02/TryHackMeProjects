
## ✅ OWASP API Security Top 10 - 1 — Quick Walkthrough Template

Here’s a `walkthrough.md` template you can drop into your repo now:

```markdown
# TryHackMe Room: OWASP API Security Top 10 - 1

- [Room Link](https://tryhackme.com/room/owaspapi10)
- Status: ✅ Completed
- Path: Web Hacking Fundamentals

---

## 🧠 Room Overview

This room introduces the **OWASP API Security Top 10** list and focuses on:

- Broken Object Level Authorization (BOLA)
- Broken User Authentication
- Excessive Data Exposure

---

## 📘 Task Notes

### Task 1: Introduction

- APIs are a major attack surface — OWASP released a separate Top 10 list for them.
- Covers threats specific to REST/GraphQL APIs.

---

### Task 2: BOLA - Broken Object Level Authorization

- Attackers can access **unauthorized objects** by modifying object IDs.
- Classic example: 
```

GET /api/users/12345 → works
GET /api/users/12346 → also works? 🔥

````
- **Key Fix:** Server must enforce access control per object **on the backend**.

---

### Task 3: Broken User Authentication

- Weak or missing authentication (tokens, passwords, sessions).
- Vulnerabilities:
- No account lockout
- Predictable tokens
- No expiration
- Use `jwt.io` to decode/inspect JWTs

---

### Task 4: Excessive Data Exposure

- API leaks **more info than needed**, trusting the client to filter it.
- Example: API returns `passwordHash`, `isAdmin`, `SSN`, etc. in JSON payload

**Fix:** Backend should **filter response data** before sending to client.

---

## 🧪 Hands-On Challenges

> ⚠️ These may have changed — adapt as needed.

### Challenge 1: Decode JWT and modify it

```bash
# Step 1: Decode the JWT using jwt.io or a Python script
# Step 2: Modify payload to escalate privileges
# Step 3: Re-sign with same key if vulnerable
````

**Flag:** `THM{REDACTED}`

---

## ✅ Summary

* Object IDs in URLs must have **backend access checks**
* APIs must enforce **strict authentication**
* Never send more data than absolutely required

---

## 🏁 Flags

* [x] Challenge Flag 1: `THM{REDACTED}`


