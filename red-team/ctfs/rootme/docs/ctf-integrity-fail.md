
## ⚠️ CTF Integrity Note – RootMe Apache Version Discrepancy

### 🧩 Context
During the "RootMe" room on TryHackMe, we encountered a mismatch between the **live scan results** and the **expected answer** to the following question:

> ❓ *What version of Apache is running?*  
> 💬 Format required: `*.*.**`

### 🧪 Our Findings

- Nmap and curl enumeration confirmed:
```

Apache/2.4.41 (Ubuntu)

```
- However, the room **only accepted**:
```

2.4.29

```

### 🧠 Root Cause
This discrepancy likely stems from:
- The RootMe VM image being originally built on **Ubuntu 18.04**, where Apache 2.4.29 is the default.
- The TryHackMe answer validator being **hardcoded** to the original answer.
- Recent deployments possibly using **updated base images (Ubuntu 20.04)** where Apache 2.4.41 is the default.

### 🧼 Implications

| Observation                        | Why It’s a Problem |
|-----------------------------------|--------------------|
| Live scan returned 2.4.41         | Accurate, real data from the box |
| THM only accepted 2.4.29          | Based on outdated image assumptions |
| Rewarded walkthrough copying      | Not tool-driven investigation |
| Penalized correct enumeration     | Breaks professional workflow habits |

### ✅ Resolution
We submitted `2.4.29` to proceed, but this highlights a **CTF integrity issue**:

- Always validate the environment yourself.
- Be cautious with walkthroughs and static answer keys.
- THM rooms may require working around **dated expectations** instead of trusting your tools.

---

**#TryHackMe #RootMe #CTF-Integrity-Fail #ReconLessons**

