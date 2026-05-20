# Task 10 — Data Summary & Analysis

Analyze the collected Reddit scraping data from Task 9 and generate useful insights and visualizations.

---

# What This Task Does

- Reads merged Reddit data from Task 9
- Calculates:
  - Total videos/posts collected
  - Total unique creators
  - Most common keywords
  - Average likes and comments
  - Top-performing posts
- Generates visualizations using Matplotlib
- Saves analysis into a text report

---

# Workflow

1. Load merged CSV data from Task 9
2. Perform statistical analysis
3. Create charts for:
   - Keyword distribution
   - Top creators
4. Generate summary report
5. Save charts and report files

---

# Output Files

## Report

summary_report.txt

Contains:
- Total posts collected
- Unique creators
- Average engagement
- Top-performing posts

---

# Charts

Saved inside:

charts/

Generated charts:
- keyword_distribution.png
- top_creators.png


---

# Folder Structure

```text
task_10/
├── analysis.py
├── summary_report.txt
├── requirements.txt
│
└── charts/
    ├── keyword_distribution.png
    └── top_creators.png
```
