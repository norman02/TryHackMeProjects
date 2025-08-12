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
