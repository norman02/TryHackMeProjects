### **Task 1 - Introduction**  
_No Answer needed_

### **Task 2 - Token-Based Authentication**  
**Objective:** Understand how JWTs are used for authentication in APIs.  

#### **Challenge Goal**  
Obtain an **admin-level JWT** to retrieve the task flag.  

#### **Key Takeaways**  
- APIs use **token-based authentication** instead of traditional cookies for session management.  
- JWTs are sent in requests using the `Authorization: Bearer <token>` header.  
- The API accepts **POST** requests for authentication and **GET** requests for user verification.  
- **Why tokens over cookies?** Cookies are web-browser specific, whereas tokens allow a more flexible authentication method across mobile apps, web apps, and other interfaces.  

#### **Answer for Task 2**  
✅ **The common header used to transport JWTs in a request is:**  
**Authorization: Bearer**

#### **Host File Update for Easier Access**  
We added the target IP `10.10.104.9` to the **hosts file** for easier reference:
```
10.10.104.9    jwt-security.thm
```
Now, API requests can be made using `jwt-security.thm` instead of the raw IP.

#### **Commands Used**  
```bash
# Authenticate to the API and receive JWT
curl -H 'Content-Type: application/json' -X POST -d '{ "username": "user", "password": "password2" }' http://jwt-security.thm/api/v1.0/example2

# Use JWT to verify user details
curl -H 'Authorization: Bearer [JWT token]' http://jwt-security.thm/api/v1.0/example2?username=Y
```

#### **Observations**  
- The API grants access based on the JWT provided.  
- To escalate privileges, we need a **JWT where `admin: 1`**.  
- Using the `Authorization: Bearer` header correctly is crucial for authentication.

#### **Next Steps**  
- Investigate possible JWT attacks (signature bypass, weak secret cracking).  
- Try modifying the token to escalate privileges.  
- Extract the flag and document the exploitation process.  

---

### **Task 3 - JWT Structure**  
**Objective:** Understand the structure and different signing algorithms used in JSON Web Tokens (JWTs).  

#### **JWT Overview**  
JWTs are **self-contained tokens** used to securely transmit session information. They follow an **open standard**, making them accessible for developers to implement across various applications.

#### **JWT Structure**  
A JWT consists of **three Base64Url-encoded components**, separated by dots (`.`):  
1. **Header** – Specifies the token type (`JWT`) and the signing algorithm (e.g., `HS256`, `RS256`).  
2. **Payload** – Contains **claims**, which store user details and attributes (e.g., `{ "username": "user", "admin": 0 }`).  
3. **Signature** – Validates the authenticity of the token and ensures it hasn't been tampered with.

#### **Signing Algorithms**  
Three main algorithms used in JWT security:
- **None** – No signature validation, making the token insecure.  
- **Symmetric Signing** (e.g., **HS256**) – Uses a **shared secret key** for both signing and verification.  
- **Asymmetric Signing** (e.g., **RS256**) – Uses a **private key** for signing and a **public key** for verification.

#### **Security in JWT Signatures**  
JWTs can be **encrypted** (known as **JWEs**) for extra security, but their core strength comes from **signatures**. A properly signed JWT allows multiple applications to verify it **without needing direct access** to the issuing server.

#### **Answers for Task 3**  
✅ **HS256 is an example of what type of signing algorithm?** **Symmetric**  
✅ **RS256 is an example of what type of signing algorithm?** **Asymmetric**  
✅ **What is the name used for encrypted JWTs?** **JWE**

---

### **Task 4 - Sensitive Information Disclosure**  
**Objective:** Identify potential JWT security flaws that expose sensitive data.  

#### **Key Takeaways**  
- JWTs should **never** store sensitive information, like passwords, in plaintext.  
- Storing tokens in **LocalStorage** or exposing them in URLs increases the risk of theft.  
- Using weak signing secrets allows attackers to forge valid JWTs.

#### **Commands Used**  
```bash
# Authenticate and receive JWT
curl -H 'Content-Type: application/json' -X POST -d '{ "username": "user", "password": "password1" }' http://jwt-security.thm/api/v1.0/example2

# Decode JWT payload to extract sensitive data
echo "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJwYXNzd29yZCI6InBhc3N3b3JkMSIsImFkbWluIjowLCJmbGFnIjoiVEhNezljYzAzOWNjLWQ4NWYtNDVkMS1hYzNiLTgxOGM4MzgzYTU2MH0ifQ.TkIH_A1zu1mu-zu6_9w_R4FUlYadkyjmXWyD5sqWd5U" | cut -d '.' -f2 | base64 -d
```

#### **Extracted Data**  
```json
{
  "username": "user",
  "password": "password1",
  "admin": 0,
  "flag": "THM{9cc039cc-d85f-45d1-ac3b-818c8383a560}"
}
```

#### **Observations**  
- The JWT **contains the password in plaintext**, which is a huge security flaw.  
- The **flag** is stored directly in the payload, meaning anyone with the token can access it.  
- Since `admin: 0`, privilege escalation is required for admin access.

#### **Next Steps**  
- Investigate ways to **modify or forge JWTs** to escalate privileges.  
- Check if weak JWT secrets allow forging new tokens.  
- Securely document findings and commit to GitHub.


