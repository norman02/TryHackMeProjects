
# Mr Robot CTF

**Target:** `robot.thm`  
**Goal:** Find all 3 keys

---

## 🔍 Nmap
Initial scan shows:

| Port | Service          | Version        |
|------|------------------|----------------|
| 22   | OpenSSH          | 8.2p1          |
| 80   | Apache httpd     | (no version)   |
| 443  | Apache httpd SSL | (no version)   |

---

## 🧭 Gobuster Findings

- `/robots.txt` → Revealed:
  - `fsocity.dic`
  - `key-1-of-3.txt`
- `/fsocity.dic` → Wordlist (used for brute-force; deduped)
- `/intro` → WebM video; cosmetic only
- `/login` → WordPress login page
- `/wp-admin/` → WP admin panel
- `/wp-content/` → Potential shell upload location
- `/wp-config` → Executed server-side, not exposed
- `/readme`, `/license` → Likely WP version info

---

## 🗝️ Key Progress

| Key        | Status | Notes                                 |
|------------|--------|----------------------------------------|
| Key 1 of 3 | ✅      | `073403c8a58a1f80d943455fb30724b9`    |
| Key 2 of 3 | ⬜      | —                                     |
| Key 3 of 3 | ⬜      | —                                     |

---

## 🔓 Credentials Discovered

| User    | Password   | Source              |
|---------|------------|---------------------|
| elliot  | ER28-0652  | Hydra (`fsocity.dic`) |

- Login confirmed at `/wp-login.php`
- Detection string used in Hydra:  
  `F=The password you entered for the username`
- Output logged to: `scans/hydra-login.txt`

---

## 📦 Next Steps

- [ ] Log in to WordPress admin with `elliot / ER28-0652`
- [ ] Explore dashboard: themes, plugin uploads, editor access
- [ ] Prepare PHP reverse shell payload
- [ ] Set up listener:
  ```bash
  nc -lvnp 4444


* [ ] Trigger shell → stabilize terminal → begin local enumeration
* [ ] Search for next key and post-exploitation targets

---

## 🧠 Notes & Observations

* WordPress is functioning as expected — clean password enumeration
* Login failure patterns were consistent and clearly detectable
* Realistic web app path with proper defenses (e.g., config not exposed, no RCE without login)


