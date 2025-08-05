## Task 1 – Ye Ol’ Search Engine

*No answer needed.*

This task provides an overview of how search engines index and crawl the web — laying the groundwork for understanding later tasks.

## Task 2 – Let’s Learn About Crawlers

**Question 1:** Name the key term of what a “Crawler” is used to do
**Answer:** `index`

**Question 2:** What is the name of the technique that “Search Engines” use to retrieve this information about websites?
**Answer:** `crawling`

**Question 3:** What is an example of the type of contents that could be gathered from a website?
**Answer:** `keywords`

**Explanation:** Web crawlers (also called spiders or bots) systematically browse the web to discover URLs and collect information. They **index** web pages, enabling search engines to respond to user queries. During crawling, crawlers gather **keywords**, URLs, and domain data to build a searchable index. :contentReference[oaicite:6]{index=6}

---

### 📎 Sidebar: Do Search Engines Still Work This Way?

Yes — despite all the modern AI enhancements, the foundation of search engines like **Google** is still based on:

1. **Crawling** – Bots (like `Googlebot`) explore web pages via links.
2. **Indexing** – Extracted content (text, metadata, images) is stored in a searchable index.
3. **Ranking** – When a user searches, Google ranks results from the index using hundreds of signals (like relevance, freshness, and mobile-friendliness).

#### 🧠 What’s Changed?

Modern search engines go beyond keywords:

| Traditional Search                | Modern Enhancements                            |
|----------------------------------|-------------------------------------------------|
| Keyword-based indexing           | NLP-based understanding (e.g., BERT, MUM)       |
| Manual crawl discovery           | Auto-discovery via sitemaps and schema.org      |
| Link-focused ranking (PageRank)  | Machine learning + user behavior                |
| Static HTML analysis             | Dynamic rendering with JavaScript execution     |

So while crawling and indexing are still critical, Google now **understands meaning and context**, executes JavaScript, and uses **AI models** to match intent.

#### 🔐 Relevance to Google Dorking

Google Dorking works *because* this index is so rich. You’re querying Google's already-collected data using advanced operators like:

- `filetype:`
- `site:`
- `inurl:`
- `intitle:`
- `cache:`

That’s why pages blocked by `robots.txt` or protected by `noindex` don’t show up in dork results — they’re never indexed in the first place.

---
## Task 3 – Search Engine Optimization (SEO)

*No answer required.*

This task introduces SEO (Search Engine Optimization) and explains how search engines use various signals to rank pages in their results.

### Key Takeaways:
- **SEO** is about making a site easier to crawl and rank.
- Factors include:
  - Site responsiveness across browsers and devices
  - The presence of a sitemap
  - Keyword relevance
- Sites are scored by complex, proprietary algorithms.
- Tools like Google’s SEO Analyzer can show how well a site ranks.

The task ends by introducing a limitation tool — `robots.txt` — which will be covered in the next task.

This sets the stage for Task 4, which introduces *robots.txt* and how web admins can control what gets indexed.

Absolutely — here’s the **complete Joplin-compatible walkthrough for Task 4 – Robots.txt**, including all questions, corrected answers, explanations, and your requested sidebar.

---

```markdown
## Task 4 – Robots.txt

This task explains how the `robots.txt` file controls web crawler behavior. It's located in the root directory of a site and defines what search engine crawlers (user-agents) are allowed or disallowed from indexing.

---

> **1. Where would `robots.txt` be located on the domain `ablog.com`?**
**Answer:** `ablog.com/robots.txt`

> **2. If a website was to have a sitemap, where would that be located?**
**Answer:** `/sitemap.xml`

> **3. How would we only allow "Bingbot" to index the website?**
**Answer:**

`User-agent: Bingbot
Allow: /`


> **4. How would we prevent a "Crawler" from indexing the directory `/dont-index-me/`?**
**Answer:** `Disallow: /dont-index-me/`

> **5. What is the extension of a Unix/Linux system configuration file that we might want to hide from "Crawlers"?**
**Answer:** `.conf`

---

### 🧠 Explanation

- `robots.txt` lives at the root of a domain (`example.com/robots.txt`).
- It provides indexing rules for crawlers, with instructions like:
  - `User-agent`: specifies which crawler the rule applies to.
  - `Allow`: explicitly allows access.
  - `Disallow`: blocks access to directories or files.
- You can even use patterns to block entire file types (e.g., `*.conf`).
- This file is **public** — attackers often read it for hints about sensitive directories.

---

### 📎 Sidebar: What if There Is No `robots.txt`?

If a website does **not** include a `robots.txt` file at its root, search engine crawlers will assume **full permission** to index everything they can reach.

#### 🔍 Default Behavior
- No file = no restrictions.
- Crawlers will index all accessible URLs, unless blocked by other means (like authentication or `noindex` tags).

#### 🔐 Security Implication
This can lead to sensitive directories (e.g., `/admin`, `/config`, `/backups`) being indexed and appearing in Google search results — a common Google Dorking target.

🛑 **Important:**
`robots.txt` is not a security control. Anyone (including attackers) can read it. Use it to avoid indexing, not to protect sensitive data.


