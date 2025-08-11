
# OAuth Vulnerabilities – Walkthrough  
**Room Type:** Premium  
**Difficulty:** Medium  
**Platform:** TryHackMe  

---

## 📌 Overview
In this room, we’ll learn how **OAuth 2.0** works, explore different grant types, identify implementations, and exploit common vulnerabilities — including token theft, CSRF attacks, and flaws in the implicit grant flow.

By the end, you’ll understand:
- What each OAuth 2.0 role and grant type is
- How the OAuth 2.0 authorization process flows
- How to spot OAuth in the wild
- How to exploit real misconfigurations in OAuth implementations
- Security changes introduced in OAuth 2.1

---

## 🗂 Task 1 – Introduction
**Learning objectives:**
- Understand core OAuth concepts  
- Learn grant types and flows  
- Identify OAuth services in apps  
- Exploit common OAuth weaknesses  
- See how OAuth 2.1 improves security  

_No answers needed for this task._

---

## 🗂 Task 2 – Key Concepts

**Key Terms:**
- **Resource Owner** – The person or system who owns the data.  
- **Client** – The application requesting access to resources on behalf of the owner.  
- **Authorization Server** – Issues access tokens after verifying the owner’s permission.  
- **Resource Server** – Hosts the protected resource and validates tokens.  
- **Authorization Grant** – A credential (e.g., code) used to get an access token.  
- **Access Token** – Credential used by the client to access resources.  
- **Refresh Token** – Used to get a new access token without re-authentication.  
- **Redirect URI** – Where the authorization server sends the user after login.  
- **Scope** – Defines the level of access requested.  
- **State** – Used to maintain request state and prevent CSRF attacks.  
- **Token Endpoint** – Where the client exchanges grants for tokens.

**Questions:**
1. Which parameter prevents CSRF attacks?  
   **Answer:** `state`
2. What credential lets the client act for the user?  
   **Answer:** `Access Token`

---

## 🗂 Task 3 – OAuth Grant Types

**1. Authorization Code Grant** (Most Secure)  
- For: Server-side apps  
- Process: Redirect → login → get `code` → exchange for token (server-to-server)  
- Pro: Token not exposed in browser  

**2. Implicit Grant** (Less Secure)  
- For: Client-side apps (SPAs)  
- Process: Redirect → login → token returned directly in URL fragment  
- Con: Token visible in browser, no refresh tokens  

**3. Resource Owner Password Credentials (ROPC)**  
- For: Trusted apps only  
- Process: User gives username/password directly to client  
- Con: Insecure — client sees password  

**4. Client Credentials Grant**  
- For: Server-to-server communication  
- Process: Client authenticates itself → gets token  

**Question:** Which grant type is often used for server-to-server communication?  
**Answer:** Client Credentials  

---

## 🗂 Task 4 – How OAuth Flow Works

**Example Flow:**  
- **Provider:** `coffee.thm`  
- **Client App:** `bistro.thm`

**Step-by-step:**
1. **Authorization Request**  
```
[http://coffee.thm:8000/accounts/login/?next=/o/authorize/?client\_id=...\&response\_type=code](http://coffee.thm:8000/accounts/login/?next=/o/authorize/?client_id=...&response_type=code)...

```
Parameters:  
- `response_type=code`  
- `client_id`  
- `redirect_uri`  
- `scope`  
- `state`  

2. **Login & Consent** – User logs in and approves access.

3. **Authorization Response**  
```

[http://bistro.thm:8000/oauthdemo/callback?code=AuthCode123456\&state=xyzSecure123](http://bistro.thm:8000/oauthdemo/callback?code=AuthCode123456&state=xyzSecure123)

```

4. **Token Request** – POST to `/o/token/` with:  
```

grant\_type=authorization\_code
code=\<auth\_code\_here>
redirect\_uri=\<redirect\_uri\_here>
client\_id=\<client\_id\_here>
client\_secret=\<client\_secret\_here>

```
Auth header: Basic Auth (`base64(client_id:client_secret)`)

5. **Token Response** – Returns:  
- `access_token`
- `token_type` (usually `Bearer`)
- `expires_in`
- `refresh_token` (optional)

**Questions:**
1. Client ID value after initiating workflow?  
**Answer:** `zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt`
2. Parameter for token validity time?  
**Answer:** `expires_in`

---

## 🗂 Task 5 – Identifying OAuth Services

**How to spot OAuth in an app:**
- “Login with Google/Facebook/GitHub” buttons
- Redirects with parameters like `client_id`, `redirect_uri`, `scope`, `response_type`
- Source code imports (e.g., `django-oauth-toolkit`)
- Unique endpoints like `/o/authorize/` or `/o/token/`
- Error messages revealing OAuth libraries

**Question:** Toolkit used for implementing OAuth at `coffee.thm:8000`?  
**Answer:** `django-oauth-toolkit`

---

## 🗂 Task 6 – Exploiting OAuth: Stealing Token

**Vulnerability:** Attacker can control the `redirect_uri` to capture authorization codes.

**Attack Flow:**
1. Attacker hosts malicious redirect pages:
- `redirect_uri.html` → Sends form to OAuth login with hidden malicious redirect
- `malicious_redirect.html` → Captures `code` from URL

2. Victim logs in at attacker’s link:
```

[http://dev.bistro.thm:8002/redirect\_uri.html](http://dev.bistro.thm:8002/redirect_uri.html)

```

3. Authorization server sends code to `malicious_redirect.html`.

4. Attacker visits:
```

[http://bistro.thm:8000/oauthdemo/callbackforflag/?code=](http://bistro.thm:8000/oauthdemo/callbackforflag/?code=)\<stolen\_code>

```
5. Token + flag returned.  

**Flag:**  
```

THM{GOT\_THE\_TOKEN007}

```

---

## 🗂 Task 7 – CSRF in OAuth

**Vulnerability:** Missing `state` parameter → attacker can link their OAuth account to victim’s session.

**Attack Flow:**
1. Attacker logs in and gets OAuth code:
```

[http://coffee.thm:8000/o/authorize/?response\_type=code\&client\_id=kwoy5pKgHOn0bJPNYuPdUL2du8aboMX1n9h9C0PN\&redirect\_uri=http://coffee.thm:8000/oauthdemo/callbackforcsrf/](http://coffee.thm:8000/o/authorize/?response_type=code&client_id=kwoy5pKgHOn0bJPNYuPdUL2du8aboMX1n9h9C0PN&redirect_uri=http://coffee.thm:8000/oauthdemo/callbackforcsrf/)

````
Example JSON response:
```json
{
  "code": "abcdef123456",
  "Payload": "http://bistro.thm:8080/csrf/callbackcsrf.php?code=abcdef123456"
}
````

2. Victim visits attacker’s crafted URL:

   ```
   http://bistro.thm:8080/csrf/callbackcsrf.php?code=abcdef123456
   ```

3. Victim’s session linked to attacker’s account.

**Flag:**

```
THM{CONTACTS_SYNCED}
```

**Mitigation:** Always include and verify the `state` parameter.

---

## 🗂 Task 8 – Implicit Grant Flow Exploit

**Vulnerability:** Token returned directly in URL fragment → exposed to JavaScript/XSS.

**Flow:**

```javascript
var client_id = 'npmL7WDiRoOvjZoGSDiJhU2ViodTdygjW8rdabt7';
var redirect_uri = 'http://factbook.thm:8080/callback.php';
var auth_url = "http://coffee.thm:8000/o/authorize/";
var url = auth_url + "?response_type=token&client_id=" + client_id + "&redirect_uri=" + encodeURIComponent(redirect_uri);
window.location.href = url;
```

**Key Point:** Access token appears in URL after `#` (hash).

**Flag Retrieval:**

1. Get token from URL fragment.
2. Visit:

   ```
   http://coffee.thm:8080/flagvalidator/
   ```

   and submit token.

**Flag:**

```
THM{TOKEN_HACKED}
```

---

## 🗂 Task 9 – Other Vulnerabilities & OAuth 2.1 Changes

**Common Issues:**

* Long-lived tokens
* Token replay attacks
* Insecure token storage

**OAuth 2.1 Updates:**

* Implicit Grant deprecated
* `state` parameter required
* Stronger redirect URI validation
* PKCE encouraged for all clients

**Question:** Which grant is omitted in OAuth 2.1?
**Answer:** Implicit Grant
