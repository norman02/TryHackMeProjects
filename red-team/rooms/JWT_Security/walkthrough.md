# 🛡️ TryHackMe: JWT Security Walkthrough

> Room: [JWT Security](https://tryhackme.com/room/jwtsecurity)  
> Machine: `JWT_API_Server_v5`  
> IP: `10.201.66.208`

---

## ✅ Task 1 – Introduction

JWTs (JSON Web Tokens) are widely used in modern API authentication systems. This room explores common JWT vulnerabilities and how attackers exploit them.

### 🧠 Learning Objectives

- Understand token-based auth flows
- Decode and forge JWTs
- Abuse common implementation flaws
- Recognize weak configurations and their risks

---

## ✅ Task 2 – Token-Based Authentication

### 🔑 Highlights

- Stateless token-based auth replaces cookies in APIs
- JWTs are sent in HTTP headers: `Authorization: Bearer <token>`
- They're stored client-side (e.g., `localStorage`)

---

## ✅ Task 3 – JWT Anatomy

```text
Header.Payload.Signature
````

* **Header:** Algorithm and type (e.g., `HS256`)
* **Payload:** Claims like username, role, admin status
* **Signature:** Ensures token integrity

JWTs are **not encrypted** — only encoded. Anyone can decode them.

---

## ✅ Task 4 – Sensitive Info Disclosure

### 🛠 Vulnerability

Developers mistakenly include secrets in the JWT payload.

### 🧪 Example

* JWT contains: `username`, `password`, and `flag`
* Decoding reveals sensitive data

```bash
echo '<payload>' | base64 -d
```

### ✅ Fix

Only include non-sensitive claims. Fetch secrets from the backend.

---

## ✅ Task 5 – Signature Validation Mistakes

### 🔥 Issue

The server accepts unsigned tokens.

### 🧪 Exploit

* Set `alg: none` in the JWT header
* Omit the signature entirely
* Create a payload with `admin: 1`

```bash
curl -H "Authorization: Bearer <header>.<payload>." http://.../example3
```

---

## ✅ Task 6 – Missing Expiration

JWT is valid forever due to no `exp` claim.

### 🛠 Fix

Include an expiration date when generating the token.

```python
"exp": datetime.utcnow() + timedelta(minutes=5)
```

---

## ✅ Task 7 – Cross-Service JWT Abuse

### 🔐 Scenario

* One app checks the `aud` claim, the other doesn’t.
* Auth token from `appB` reused on `appA` for privilege escalation.

### 🛠 Fix

All services must validate the `aud` claim:

```python
jwt.decode(token, secret, audience=["appA"])
```

---

## ✅ Task 8 – Conclusion

### 🚨 Common JWT Mistakes

| Mistake                 | Risk                                |
| ----------------------- | ----------------------------------- |
| No signature check      | Allows forged tokens                |
| `alg: none` allowed     | Signature bypass                    |
| Weak secret             | Easily brute-forced                 |
| RS256 accepted as HS256 | Public key used as HMAC secret      |
| No expiration (`exp`)   | Tokens never expire                 |
| Ignoring `aud` claim    | Enables token reuse across services |



