# Summer Internship Assignment - 1

This repository contains solutions for all tasks given in the Summer Internship Assignment using Python 3.13.1

---

# Folder Structure

```bash
ASSIGNMENT/
│
├── tasks/
│   │
│   ├── task_1/
│   │   ├── input&output.txt
│   │   ├── ReadMe.md
│   │   └── task1.py
│   │
│   ├── task_2/
│   │   ├── input&output.txt
│   │   ├── log_summary.json
│   │   ├── ReadMe.md
│   │   ├── task2.py
│   │   └── text_file.txt
│   │
│   ├── task_3/
│   │   ├── input&output.txt
│   │   ├── ReadMe.md
│   │   └── task3.py
│   │
│   ├── task_4/
│   │   ├── ReadMe.md
│   │   └── task4.py
│   │
│   ├── task_5/
│   │   ├── ReadMe.md
│   │   ├── Screenshot of first 5 rows.png
│   │   └── task5.py
│   │
│   ├── task_6/
│   │   ├── 1_histogram_burnout.png
│   │   ├── 2_scatter_sleep_stress.png
│   │   ├── 3_heatmap.png
│   │   ├── 4_bar_chart.png
│   │   ├── 5_boxplot.png
│   │   ├── ReadMe.md
│   │   └── task6.py
│   │
│   ├── task_7/
│   │   ├── insights_report.txt
│   │   ├── ReadMe.md
│   │   └── task7.py
│   │
│   ├── task_8_reddit_scraper/
│   │   ├── data/
│   │   ├── scraper/
│   │   ├── main.py
│   │   ├── ReadMe.md
│   │   └── requirements.txt
│   │
│   ├── task_9_context_scraper/
│   │   ├── data/
│   │   ├── helpers/
│   │   ├── videos/
│   │   ├── keywords.txt
│   │   ├── main.py
│   │   └── ReadMe.md
│   │
│   └── task_10/
│       ├── charts/
│       ├── analysis.py
│       ├── ReadMe.md
│       ├── requirements.txt
│       └── summary_report.txt
│
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Tasks Overview

## Task 1 — List & Dictionary Operations

- Remove duplicates from a list
- Sort the list
- Find:
  - Maximum value
  - Minimum value
  - Average value
  - Frequency of elements

---

## Task 2 — File Handling

- Read log entries from a text file
- Count occurrences of log types
- Save summary into JSON format
- Display most frequent log type

---

## Task 3 — Functions & Error Handling

- Implemented `safe_divide(a, b)`
- Handles:
  - Division by zero
  - Invalid inputs
- Added proper docstrings and error messages

---

## Task 4 — Debugging

- Fixed buggy Python code
- Explained:
  - Why the bug occurs
  - Correct solution
  - Time complexity

---

## Task 5 — Data Cleaning

Dataset Used:  
Digital Burnout & Productivity Analytics Dataset

Operations Performed:
- Loaded dataset using pandas
- Handled missing values
- Removed duplicates
- Encoded categorical data
- Generated dataset statistics
- Saved cleaned dataset

---

## Task 6 — Data Visualization

Generated 5 visualizations:
- Histogram
- Scatter Plot
- Heatmap
- Bar Chart
- Boxplot

All graphs include:
- Titles
- Labels
- Proper formatting

---

## Task 7 — Insights Report

Created a report containing:
- Dataset observations
- Trends
- Problems in dataset
- Final conclusions

---

## Task 8 — Reddit Scraper

Built a Reddit scraping pipeline.

### Features
- Collects Reddit posts/videos
- Stores data in CSV/JSON
- Modular folder structure
- Exception handling
- Clean reusable code

---

## Task 9 — Context Based Scraper

Extended scraper pipeline to:
- Read multiple keywords from file
- Collect data from multiple searches
- Remove duplicates
- Categorize videos into folders

Example:

```bash
videos/
├── robotics/
├── ai/
├── sports/
└── semiconductor/
```

---

## Task 10 — Data Summary & Analysis

Generated:
- Total videos collected
- Unique creators count
- Most common keywords
- Average engagement statistics
- Top-performing posts

Also created visualizations and summary report.

---

# Requirements

Libraries used are listed in `requirements.txt`.

```txt
pandas
numpy
matplotlib
seaborn
requests
beautifulsoup4
lxml
tqdm
retrying
```

---
