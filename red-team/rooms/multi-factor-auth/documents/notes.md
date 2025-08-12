# Multi-Factor Authentication
room: premium
difficulty: easy
target machin: mfa.thm

## Task 1 - Introduction

### Objectives
- Undersand the operational principles of MFA
- Explore different types of authentication facors used
- explore practical scenarious of MFA

### Questions
No answer needed
## Task 2 - How MFA Works

### Types of Authentication Factors

* Something you Know: Password, PIN
* Something you have: Authentication app, secrity token, smart card
* Something you are: Biometrics
* Somewhere you are: IP address, geolocation
* Something you do: captcha

### Kinds of 2FA

* Time-Based-One-Time Passords (TOTP)
* Push Notifications
* SMS
* Hardware tokens

### Conditional access
* Location-Based
* Time-Based
* Behaviroral Analysis
* Device Specific

### Questions
Q: When Logging in to the application, you recive an SMS on yu phone contianing the OTP, What authentication factor is this?
Answer: something you have

## Implementations and Applications

### MFA in Banking
* protect user's personal information from cyber thef, fraud, and other threats.

### MFA in Helthcare
Due to regulations like HIPAA, MFA makes sure that patient records and personal health information are only accessible by authorizaed persons

### MFA in Corporate IT
IT departments in the corporate world are under intense pressure to protect sensitive business data and maintain system integrity. MFA helps mitigate the risk of unauthorized access that could lead to data theft, espionage, or sabotage.

### Questions
Q: Is MFA an important factor in keeping our online and offline activities safe from threat actors?
Answer: yea

## Task 4 - Common Vulnerabilities in MFA
* Weak OTP Generation Algorithms
* Application leaking the 2FA Token
* Brute Forcing the OTP
* Usage of EVilginx

### Questions
Q: What can be implemented to help prevent brute forcing OTPs?
A: rate limiting

## Task 5 - Practical - OTP Leakage
### OTP Leakage
* Server-Side Validation and Return of Sensitive Data
* Lack of Proper Security Practices
* Debugging Inforrmation Left In Production


### Exploitation

* Go to http://mfa.thm/labs/first
* Login with the credentials `thm@mail.thm` `test123`
* You will see an XHR request sent to the /token endpoint
* the application returns a response with a size of 16 bytes. Click this request and navigate to the response tab
* Copy the value of the token parameter and past it into the OTP form, then click verify account
* Retrieve the flag


### Questions
Q: What is the flag in the dashboard?
A:  904c8ac84e44f0ba942e9e11ee7037b8

## Task 6 - Practical - Insecure Coding

### Exploitation
* Login to http://mfa.thm/labs/second using the same credentials as befor
* Bypass the OTP step by directly accessing the dashboard http://mfa.thm/labs/second/dashboard


### Questions
Q: What is the flag in the dashboard?
A: 87880e9d27001affdff90989f351c462

## Task 7 - Practical - Beathing the Auto-Logout Feature

* Create exploit.py script to brute force the pin
* Using the new PHPSESSID, go to http://mfa.thm/labs/third, in dev tools go to storage > cookies
* Replace the PHPSESSID value with the PHPSESSID from your terminal
* Go to http://mfa.thm/labs/third/dashboard and retrieve the flag

Session token: vc05hpdmdof9b5dcvtjgcvdr47

### Questions
Q: What is the flag in the terminal?
A:  20548e076dbb9ba30c9d94ae4aceb38e 

## Task 8 - Conclusion
* Understanding MFA
* Addressing vulnerabilities
* Best Practices

### Questions
no answer needed
