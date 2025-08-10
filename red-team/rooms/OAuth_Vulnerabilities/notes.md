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

### 🔐 1. Authorization Code Grant

* **Use Case**: Server-side apps (e.g., PHP, Java, .NET)
* **Flow**:

  1. User is redirected to the authorization server.
  2. Upon approval, a code is sent to the client.
  3. The client exchanges the code (server-to-server) for an access token.
* **Pros**: Secure — tokens not exposed to the browser; supports refresh tokens.

### ⚠️ 2. Implicit Grant

* **Use Case**: Client-side apps (e.g., SPAs, mobile)
* **Flow**:

  1. User is redirected and approves access.
  2. Access token is returned in the URL fragment.
* **Pros**: Simpler, faster.
* **Cons**: Less secure — token visible in browser; no refresh tokens.

### 👤 3. Resource Owner Password Credentials (ROPC) Grant

* **Use Case**: First-party/trusted apps.
* **Flow**:

  1. User provides credentials directly to the client.
  2. Client sends credentials to authorization server.
  3. Access token is issued.
* **Pros**: Fewer steps.
* **Cons**: Insecure — credentials shared directly.

### 🤖 4. Client Credentials Grant

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
