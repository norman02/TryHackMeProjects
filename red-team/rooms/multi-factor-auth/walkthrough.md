

# 🔐 Multi-Factor Authentication (MFA) – Full Walkthrough

**Room**: Premium
**Difficulty**: Easy
**Target Machine**: `mfa.thm`

---

## 🗝️ 1 – Introduction

**Multi-Factor Authentication (MFA)** adds extra layers of security by requiring more than one verification method to prove a user’s identity.

### **Why MFA Matters**

* Passwords alone are vulnerable to theft, guessing, and reuse.
* MFA dramatically reduces the success rate of phishing and credential stuffing.
* Even if a password is compromised, additional factors protect the account.

**Core Security Principle**: *Never rely on one single factor — attackers only need to bypass one defense if you do.*

---

## 🔍 2 – Types of Authentication Factors

| Factor Type            | Description      | Examples                                             |
| ---------------------- | ---------------- | ---------------------------------------------------- |
| **Something you know** | Knowledge-based  | Passwords, PINs, security questions                  |
| **Something you have** | Possession-based | Phone, smart card, hardware token, authenticator app |
| **Something you are**  | Biometric        | Fingerprint, face scan, iris                         |
| **Somewhere you are**  | Location-based   | IP address, GPS geolocation                          |
| **Something you do**   | Behavioral       | Typing rhythm, mouse movement                        |

---

## ⏱️ 3 – Common 2FA/MFA Implementations

| Type                                    | Description                        | Example                      |
| --------------------------------------- | ---------------------------------- | ---------------------------- |
| **TOTP (Time-Based One-Time Password)** | 6–8 digit codes changing every 30s | Google Authenticator, Authy  |
| **HOTP (Counter-Based OTP)**            | Code increments each use           | RSA SecurID                  |
| **Push Notifications**                  | App prompt to approve login        | Duo, Microsoft Authenticator |
| **SMS OTP**                             | Text message with code             | Bank login                   |
| **Hardware Token**                      | Physical device generates code     | YubiKey, RSA token           |
| **Biometric MFA**                       | Physical trait as factor           | Face ID, fingerprint scanner |

**Conditional Access Rules** can further restrict MFA:

* **Location-based**: Only allow logins from certain countries/IP ranges.
* **Time-based**: Block logins during certain hours.
* **Behavioral**: Detect anomalies like typing speed or device posture.
* **Device-specific**: Limit access to registered devices.

---

## ⚠️ 4 – MFA Vulnerabilities

Even with MFA, **bad implementation** can introduce weaknesses:

* Weak OTP algorithms.
* OTP/token leakage in API responses.
* No rate-limiting → brute-force OTPs.
* Skippable MFA logic (direct dashboard access).
* **Reverse Proxy Attacks** (e.g., Evilginx) to steal post-MFA session cookies.

**Best Practices to Defend Against These**:

* Use phishing-resistant MFA (FIDO2/WebAuthn).
* Enforce strict server-side checks.
* Limit OTP attempts and lock accounts after repeated failures.
* Secure API responses — never send OTPs to the client.

---

## 💻 5 – Practical Room Exploits

### **Task 5 – OTP Leakage**

**Goal**: Exploit API leaking the OTP.

**Steps**:

1. Go to:

   ```
   http://mfa.thm/labs/first
   ```
2. Login:

   ```
   thm@mail.thm / test123
   ```
3. Open **DevTools → Network** tab.
4. Find the request to `/token`.
5. In **Response**, copy the `"token"` value.
6. Paste into OTP form → Verify.
7. Flag appears in dashboard.

**Answer**: `904c8ac84e44f0ba942e9e11ee7037b8`

---

### **Task 6 – Insecure Coding**

**Goal**: Bypass MFA check entirely.

**Steps**:

1. Go to:

   ```
   http://mfa.thm/labs/second
   ```
2. Login:

   ```
   thm@mail.thm / test123
   ```
3. Skip OTP form — directly visit:

   ```
   http://mfa.thm/labs/second/dashboard
   ```
4. Flag appears.

**Answer**: `87880e9d27001affdff90989f351c462`

---

### **Task 7 – Beating Auto-Logout**

**Goal**: Brute-force OTP outside of browser and reuse valid session cookie.

**Steps**:

1. Run `exploit.py` to brute force and retrieve PHPSESSID:

   ```
   Session token: vc05hpdmdof9b5dcvtjgcvdr47
   ```
2. In browser, login to:

   ```
   http://mfa.thm/labs/third
   ```
3. Open **DevTools → Application (Chrome)** or **Storage (Firefox)**.
4. Expand **Cookies** → select `mfa.thm`.
5. Find `PHPSESSID` → double-click value → paste new token.
6. Save, then visit:

   ```
   http://mfa.thm/labs/third/dashboard
   ```
7. Flag appears.

**Answer**: `20548e076dbb9ba30c9d94ae4aceb38e`

---

## 🛠️ 6 – Tools & Techniques Reference

### **Editing Cookies via DevTools**

* **Chrome**: `F12` → Application → Storage → Cookies → Edit value → Enter.
* **Firefox**: `F12` → Storage → Cookies → Edit value → Enter.

### **Evilginx Overview** (for real-world MFA bypass)

* Reverse proxy between victim & legitimate site.
* Captures credentials + MFA-validated session cookies.
* Use case in lab: Not required, but important in real-life scenarios.

---

## 📜 7 – Conclusion

**Key Takeaways**:

* MFA is powerful but **not invulnerable** — security depends on correct implementation.
* OTP leakage, missing checks, and cookie manipulation are common flaws.
* Manual cookie editing is a critical CTF skill.
* Reverse proxy phishing tools like Evilginx make session hijacking possible, but hardware-based MFA mitigates these attacks.

---

## 📌 Final Flags Recap

* Task 5: `904c8ac84e44f0ba942e9e11ee7037b8`
* Task 6: `87880e9d27001affdff90989f351c462`
* Task 7: `20548e076dbb9ba30c9d94ae4aceb38e`



