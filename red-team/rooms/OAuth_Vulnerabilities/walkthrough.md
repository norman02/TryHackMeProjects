# OAuth Vulnerabilities
Learn how the OAuth protocol works and master techniques to exploit it
Roomtype: Premium
Difficulty: Medium

## Task 1 Introduction

### Learning Objectives
- Essential concepts for OAuth 2.0 (Grant Types
- OAuth 2.0 flow
- Idnetify OAuth services
- Exploitation techniques
- Evolution of OAuth 2.1

### Questions
No answer needed
***
## Task 2 - Key Concepts

- Resource Owner: The perosnor system that conrols data and can authorize an application to access that data.
- Client: An application that acts as an intermediar, requesting access to resources and performing actions as permitted bny the resource owner
- Authorization Server: Server resposible for issuing access tokens to the client.
- Resource Sever - The sever hoisting the protected resource can accept and respond to protected resource requests using access tokens.
- Authorization Grant: The client uses a credential representing the resource owner's authorization to obtain an access tokent. The primary grant types are Authorization Code, Implicit, Resou4rce Owner Password Credentials, and Client Credentials
- Access Token: A credential with limited lifespan and scope that the client can use to optain acccess protected resources on bahalf of the resource owner.
- Refresh Token: A credential that the client can use to obtain a new access token withouth requiring the resource owner to re-authenticate.
- Redirect URI: The URI to which the authorization sever will redirect the resource owner's user-agent after grant or denial of the authorization.
- Scope: A mechanism for limiting an application's access to a user's account, using the principle of least privilege.
- Sate Paramater: an optional parameter maintains the state between the client and the authorization server.
- Token & Authorization Endpoint: where the client exchanges the authorization grant (or refresh token) for an access token

### Questions
Which parmeter cna be used to prevent CSRF attackes?
Answer: State

What credentials can the client use to access protected resources on behalf of the resource owner?
Answer: Access Token
***
## Task 3 - OAuth Grant Types




OAuth 2.0 defines several **grant types**, which specify how a client obtains an **access token** to access protected resources on behalf of a user. Each type is tailored for different client capabilities and trust levels.

###  1. Authorization Code Grant

* **Use Case**: Server-side apps (e.g., PHP, Java, .NET)
* **Flow**:

  1. User is redirected to the authorization server.
  2. Upon approval, a code is sent to the client.
  3. The client exchanges the code (server-to-server) for an access token.
* **Pros**: Secure — tokens not exposed to the browser; supports refresh tokens.

###  2. Implicit Grant

* **Use Case**: Client-side apps (e.g., SPAs, mobile)
* **Flow**:

  1. User is redirected and approves access.
  2. Access token is returned in the URL fragment.
* **Pros**: Simpler, faster.
* **Cons**: Less secure — token visible in browser; no refresh tokens.

###  3. Resource Owner Password Credentials (ROPC) Grant

* **Use Case**: First-party/trusted apps.
* **Flow**:

  1. User provides credentials directly to the client.
  2. Client sends credentials to authorization server.
  3. Access token is issued.
* **Pros**: Fewer steps.
* **Cons**: Insecure — credentials shared directly.

###  4. Client Credentials Grant

* **Use Case**: Machine-to-machine / backend services.
* **Flow**:

  1. Client authenticates with client ID/secret.
  2. Receives access token directly.
* **Pros**: No user data involved — ideal for server-server communication.

---
### Questions
What is the grant type often used for server-server interaction?
Answer: Client Credentials

***


## Task 4 – How OAuth Flow Works (TryHackMe: OAuth Vulnerabilities)

### Overview

This task walks through a full OAuth 2.0 **Authorization Code Grant** flow using a practical example:

* **OAuth Provider**: `http://coffee.thm:8000`
* **Client App**: `http://bistro.thm:8000`
* **User Accounts**:

  * Victim: `victim:victim123`
  * Attacker: `attacker:tesla@123`

---

### OAuth Flow Breakdown

#### 1. **Authorization Request**

* The client (`bistro.thm`) redirects the user to the **OAuth provider** (`coffee.thm`) with:

  * `response_type=code`
  * `client_id`
  * `redirect_uri`
  * `state` (CSRF token)
  * `scope`
* URL Example:

  ```
  http://coffee.thm:8000/accounts/login/?next=/o/authorize/?client_id=...&response_type=code...
  ```

#### 2. **Authentication & Authorization**

* User (Tom) logs into the **authorization server**.
* Presented with a **consent screen** to approve scopes (e.g., view coffee orders).

#### 3. **Authorization Response**

* If Tom consents:

  * Redirected to `bistro.thm` with:

    * `code` = Authorization Code
    * `state` = CSRF token
* Example:

  ```
  http://bistro.thm:8000/oauthdemo/callback?code=AuthCode123456&state=xyzSecure123
  ```

#### 4. **Token Request**

* The client exchanges the code for an access token via POST to `/o/token/`.
* Parameters:

  * `grant_type=authorization_code`
  * `code`
  * `redirect_uri`
  * `client_id`
  * `client_secret`
* Auth header: Basic Auth (base64 of client\_id\:client\_secret)

#### 5. **Token Response**

* The server returns:

  * `access_token`
  * `token_type` (usually "Bearer")
  * `expires_in` **Validity period**
  * `refresh_token` (optional)

---
#### Questions:
Q1: What is the cliend_id value after initiating the OAuth 2.0 Workflow?
Answer: zlurq9lseKqvHabNqOc2DkjChC000QJPQ0JvNoBt
Q2: What parameter name determines the time validity of a token in the token response?
Anser: Expires_in
***
## Task 5 - Identifying OAuth Services
### Identifying OAuth Usage in an Application
Look for options allowing users to log in using external services providers, Google, Facebook, Github, etc.

### Detcting OAuth Implementation
OAuth implementations will generally redirect the browser to an authorization server's URL. This URL often contains specific query parameters, such as response_type, client_id, redirect_uri, scope, and state.

### Identifying the OAuth Framework

- HTTP Headers and Responses Unique identifiers or comments referencing OAuth libraries or frameworks
- Source Code Analysis: Keywords and import statments that reveal the frameworks in use
- Authorization and Token endpoints: OAuth implementations might have unique enpoint patterns or structures
- Error Messages: Error messages and debug output can reveal the underlying stack
---
### Questions
Q1 What is the name of the toolkit used for implementing OAuth in the URL http://cofee.thm:8000/
Answer - django-oauth-toolkit
***
## Task 6 - Exploiting OAuth: Stealing Token

### Vulnerability:

If an attacker controls a registered redirect URI, the can:

1. Initiate login with a fake redirect_uri
2. Victum logs in and consents
3. Authorization code is sent to attackers machine

### In this room:

* Attacker controls http://dev.bistro.thm:8002
* hosts:
* * redirect_uri.html -> sends form to ouath_login/ with hidden redirect_uri
* * malicious_redirect.html -> JavaScript captures code form URL
### Victim flow:
1. Clicks Login via Oauth on attacker's page
2. Logs in as victim:victim123
3. code is sent to malicious_redirect.html and displayed

### Attacker Flow

1. Copies the intercepted coude
2. Visits:
```
http://bistro.thm:8000/oauthdemo/callbackforflag/?code=xxxx
```
3. Receivs token + flag
token: ZhbMZE10koS84l7BTYqY2tezt9RRf6

Q: What is the flag after getting the access tokent?

flag: "THM{GOT_THE_TOKEN007}"
***
## Task 7 - CSRF in OAuth
---
### Goal
Exploit a missing state parameter in the OAuth flow to perform a CSRF attack that links the attackers OAuth account to the victim's session, exfiltrating contact data.
---
### Why the state Parameter Matters
* The state parameter is used to:
 * Prevent CSRF attacks in Oauth.
 * Ensure that the authorization response matches the request
* If the parameter is missing or static, a threat actor can reuse the authorization codes across user sessions

## Explit Steps

### Step 1 - Attacker's Perspective

#### Login as attacker
* URL: http://mycountacts.thm:8080/csrf/index.php
* Credentials attacker:attacker

#### Get Attacker's OAuth Code

```
http://coffee.thm:8000/o/authorize/?response_type=code&client_id=kwoy5pKgHOn0bJPNYuPdUL2du8aboMX1n9h9C0PN&redirect_uri=http://coffee.thm:8000/oauthdemo/callbackforcsrf/
```

You’ll see a response like:

```json
{
  "code": "abcdef123456",
  "Payload": "http://bistro.thm:8080/csrf/callbackcsrf.php?code=abcdef123456"
}
```

* Copy the full **Payload** URL.


### Step 2 - Victim's Perspective

#### Login as victim:

* URL: http://bistro.thm:8080/csrf
* Credentials: victim:victim


#### Simulate CSRF attack:

in the same browser pastee the attacker's paylod URL
```
http://bistro.thm:8080/csrf/callbackcsrf.php?code=XXXXX
```
Since there is no state parameter, the system can't tell that the authorization code belogns to someone else so it accepts it and links the attacker's account to the victims session

### Flag & Answers
token:"HVzfPZqG7qRd5C01elgF670J46MBYb"
Q1: What is the flag value after attaching the attacker's account with the victims account?
THM{CONTACTS_SYNCED}
Q2: What parameter name does the client application include in the authorization request to avoid CSRF attacks?
Answer: state
