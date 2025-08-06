# TryHackMe – Searchlight: OSINT 🕵️‍♂️

## 🧠 Summary
A browser-based OSINT room focused on image analysis and geolocation. The challenges simulate real-world image intel work, but several tasks suffer from vagueness and ambiguity that hinder the learning experience.

- **Room URL:** https://tryhackme.com/room/searchlightosint
- **Difficulty:** Easy (conceptually), but misleading in flag precision
- **Time to Complete:** ~1.5–2 hours

---

## 🛠️ Setup

- No VM required ✅
- Images and videos are downloaded directly via the browser

---

## ✅ Task Walkthrough

### 🔍 Task 1–2: Intro + First Clue
- Straightforward Google dorking
- Reinforces basic OSINT recon tools like image search and metadata analysis

---

### 🖼️ Task 5: Shop Sign Across the Street
- **Answer:** `sl{the edinburgh woollen mill}`
- Required extreme zoom and enhancement to identify a blurry storefront sign
- **Frustration:** Multiple locations exist; only **one** had the correct combination of a **curved sign** and **wheelchair ramp**
- Ultimately narrowed to a **location in England, not Scotland**, and verified by tracking down a **coffee shop on Facebook**

---

### 📸 Task 6: Chrome-Nosed Reindeer Statue
- **Answer 1:** `sl{rudolph the chrome-nosed reindeer}`
- **Answer 2 (photographer):** `sl{kjersti stensrud}`
- Image had no EXIF; reverse image search only returned TryHackMe results
- Final answer had to be **scraped from walkthroughs**, not derived through recon alone

---

### ⚖️ Task 8: Lady Justice Statue
- **Answer 1:** `sl{lady justice}`
- **Answer 2 (location):** `sl{alexandria, virginia}`
- **Frustration:** “Where is this statue displayed?” is misleading — expected *city*, not courthouse name

---

### 🏨 Task 9: Building Opposite the Statue
- **Answer:** `sl{the westin alexandria old town}`
- **Hint:** “The quality of this establishment is shown with stars”
- **Frustration:** Misleading phrasing, unclear what “opposite” means, and several common-sense answers were marked incorrect (e.g., *Alexandria City Hall*, *Courthouse Square*)

---

### 🎥 Task 10 (Video Clip)
- **Answer:** `sl{novotel singapore clarke quay}`
- Clip showed a riverwalk with the distinctive Novotel hotel in Singapore
- **Frustration:** Video only streamed and couldn’t be downloaded for closer frame-by-frame analysis on some systems

---

## 🧠 Final Thoughts

While the exercises are realistic and valuable for developing geolocation and OSINT skills, the **ambiguity in flag expectations** undermines learning. Success often hinged on guessing the exact phrasing used in TryHackMe’s internal answer key, rather than confirming findings through strong evidence.

### ⚠️ Notable Frustrations:
- Vague language: “Where is this statue displayed?” → city, not building
- Visual challenges required near-perfect eyesight or enhancement tools
- Some flags had to be scraped from other walkthroughs due to data obfuscation

---

## 📖 Vault-Worthy Patterns

- Always check real format: `file`, `exiftool`
- Use `feh`, `display`, `convert` for visual enhancement
- Reverse image search = Google, Yandex, TinEye
- Check Facebook + blog posts for visual clues
- Be skeptical of file extensions and apparent metadata

---

## 🏁 Status

- [x] Room Completed
- [x] Flags Captured
- [x] Notes Vaulted


