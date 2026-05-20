# Task 9 — Context Based Scraping

Extend the Reddit scraping pipeline from Task 8 to support multiple search contexts, merged results, duplicate removal, and categorized media storage.

---

# Features Implemented

1. Accept multiple keywords/topics from a text file.
2. Perform multiple Reddit searches automatically.
3. Merge all collected search results.
4. Remove duplicate posts/videos.
5. Download and save media into categorized folders based on context.

---

# Project Structure

```text
tasks/
│
├── task_8/
│   └── reddit_scraper/
│       ├── scraper/
│       │   ├── reddit_scraper.py
│       │   ├── saver.py
│       │   └── utils.py
│
├── task_9/
│   └── context_scraper/
│       ├── main.py
│       ├── keywords.txt
│       │
│       ├── videos/
│       │   ├── ai/
│       │   ├── robotics/
│       │   ├── sports/
│       │   └── semiconductor/
│       │
│       └── helpers/
│           ├── downloader.py
│           └── deduplicate.py
```

---

# Workflow

1. Read keywords from `keywords.txt`
2. Reuse Task 8 Reddit scraper
3. Perform multiple searches
4. Merge all collected results
5. Remove duplicate posts/videos
6. Download media files
7. Categorize media based on context
8. Save final merged data into CSV and JSON formats

---

# Output

Data files generated inside:

```text
data/
```

Files:

- `merged_results.csv`
- `merged_results.json`

---

# Categorized Media Storage

Downloaded media is stored inside:

```text
videos/
```

Example:

```text
videos/
│
├── ai/
├── robotics/
├── sports/
└── semiconductor/
```
