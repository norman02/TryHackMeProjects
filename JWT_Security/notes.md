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
✅ The common header used to transport JWTs in a request is:  
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


