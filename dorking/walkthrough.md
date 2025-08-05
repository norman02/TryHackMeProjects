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

