# Task 8 — Reddit Web Scraper

## Description
This program builds a scraper using `requests` and `BeautifulSoup`.

It creates a Python pipeline that:

1. Searches Reddit posts using keywords and context.
2. Extracts:
   - Post text
   - Username
   - Post link
   - Video URL or media link
   - Timestamp
   - Engagement statistics (likes/comments if available)
3. Stores the collected data in:
   - CSV format
   - JSON format

---

## Example Search Contexts

- AI generated videos
- Robotics demos
- Self-driving cars
- Sports highlights

---

## Requirements

- Modular code structure
- Proper exception handling
- Retry mechanisms for failed requests
- Clean folder organization

---

## Technologies Used

- Python
- requests
- BeautifulSoup
- pandas

---

## Output

The scraper saves collected Reddit data into:

- `data/output.csv`
- `data/output.json`

---

## How to Run

```bash
python main.py
```
