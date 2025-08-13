
# 🧨 TryHackMe – Flag Vault (PWN)

> **Status:** Abandoned (Remote Exploit Fails Despite Valid Conditions)

---

## 🗂️ Overview

- **Room:** Flag Vault (PWN)  
- **Platform:** TryHackMe  
- **Category:** Binary Exploitation  
- **Difficulty:** Easy  
- **Date Started:** 2025-08-13  
- **Date Abandoned:** 2025-08-13  
- **Status:** Incomplete due to suspected remote misconfiguration

---

## 🔍 Objective

Exploit a simple stack buffer overflow to redirect execution to a function called `print_flag()` and retrieve the flag. The vulnerability lies in an unsafe use of `gets()` on a buffer declared in the main login function.

---

## 🔧 Setup Summary

```c
char username[100];
char password[100] = "";
gets(username);
````

* **Vulnerability:** Unbounded `gets()` input into `username` allows stack smashing.
* **Goal:** Overflow buffer and overwrite RIP to jump to `print_flag()`.

---

## 🧪 Compilation Notes

To compile the provided `pwn1.c` source locally for testing:

```bash
gcc pwn1.c -o vault -fno-stack-protector -no-pie
```

**Required fixes:**

* Remove invalid trailing characters and semicolons
* Declare `gets()` manually to suppress warnings

---

## ✅ Local Exploitation

* **RIP Offset Discovered:** 230 bytes
* Used `pwntools` and GDB to verify stack overflow
* Extracted address of `print_flag()` using `nm` and `objdump`
* Constructed payload: `A * 230 + print_flag address`
* **Local execution succeeds** and triggers flag print

---

## ❌ Remote Exploitation Failure

Despite the exploit working perfectly locally:

* All remote payloads result in the **exact same response**:

  ```
  Username: Wrong password! No flag for you.
  ```
* Remote server behavior does not change, even when:

  * RIP is overwritten with a valid address
  * `cat flag.txt` or other commands are sent post-exploit
  * Payload is sent via `pwntools`, raw socket, or manual `nc`
* Even interactive shells from `pwntools` receive an EOF after output

---

## 📎 Evidence of Broken Challenge

* The vulnerability and payload logic have been verified locally in GDB.
* Multiple walkthroughs from prior years describe the same exploit path, but none seem recent.
* No successful 2025 reports could be found.
* Behavior is identical across multiple delivery methods and recompiled binaries.

---

## 📌 Final Notes

Due to repeated failures with **validated payloads**, a consistent "Wrong password" response, and lack of any shell interaction or flag output, we have concluded that the **remote instance of this room is broken or misconfigured**.

---

## 🧠 Lessons Learned

* Reinforced buffer overflow fundamentals
* Practiced using GDB, `cyclic()` patterns, and RIP offset detection
* Learned to validate stack layout and protections (`checksec`)
* Gained insight into debugging remote exploitation failures
* Reaffirmed the importance of verifying room stability

---

## 🛑 Recommendation

Unless TryHackMe updates or fixes the room backend, this room should be avoided. Consider alternatives such as:

* [TryHackMe – Buffer Overflow Prep](https://tryhackme.com/room/bufferoverflowprep)
* [TryHackMe – Stack Based Buffer Overflow](https://tryhackme.com/room/stackbasedbufferoverflow)


