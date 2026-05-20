import pandas as pd
import matplotlib.pyplot as plt
import os


# Read Task 9 merged data
DATA_PATH = "../task_9/context_scraper/data/merged_results.csv"

df = pd.read_csv(DATA_PATH)

# Create charts folder
os.makedirs("charts", exist_ok=True)

# -----------------------------------
# Basic Analysis
# -----------------------------------

total_videos = len(df)

unique_creators = df["username"].nunique()

most_common_keywords = df["context"].value_counts()

average_likes = df["likes"].mean()

average_comments = df["reposts/comments"].mean()

top_posts = df.sort_values(
    by="likes",
    ascending=False
).head(5)

# -----------------------------------
# Visualization 1
# Keyword Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

most_common_keywords.plot(kind="bar")

plt.title("Most Common Keywords")

plt.xlabel("Keyword")

plt.ylabel("Number of Posts")

plt.tight_layout()

plt.savefig("charts/keyword_distribution.png")

plt.close()

# -----------------------------------
# Visualization 2
# Top Creators
# -----------------------------------

top_creators = df["username"].value_counts().head(10)

plt.figure(figsize=(8, 5))

top_creators.plot(kind="bar")

plt.title("Top Creators")

plt.xlabel("Username")

plt.ylabel("Number of Posts")

plt.tight_layout()

plt.savefig("charts/top_creators.png")

plt.close()

# -----------------------------------
# Generate Summary Report
# -----------------------------------

with open("summary_report.txt", "w", encoding="utf-8") as file:

    file.write("TASK 10 — DATA SUMMARY & ANALYSIS\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Videos Collected: {total_videos}\n")

    file.write(f"Total Unique Creators: {unique_creators}\n\n")

    file.write("Most Common Keywords:\n")

    file.write(str(most_common_keywords))

    file.write("\n\n")

    file.write(f"Average Likes: {average_likes:.2f}\n")

    file.write(f"Average Comments: {average_comments:.2f}\n\n")

    file.write("Top Performing Posts:\n\n")

    for index, row in top_posts.iterrows():

        file.write(f"Title: {row['tweet_text']}\n")

        file.write(f"Username: {row['username']}\n")

        file.write(f"Likes: {row['likes']}\n")

        file.write(f"Comments: {row['reposts/comments']}\n")

        file.write(f"Link: {row['tweet_link']}\n")

        file.write("-" * 50 + "\n")

print("Analysis completed successfully.")
print("Summary saved to summary_report.txt")
print("Charts saved inside charts/")