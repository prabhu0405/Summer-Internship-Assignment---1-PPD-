import sys
import os

# add task_8 reddit_scraper path
sys.path.append(
    os.path.abspath("../../task_8/reddit_scraper")
)

# IMPORT OLD TASK 8 FUNCTIONS
from scraper.reddit_scraper import scrape_reddit
from scraper.saver import save_csv, save_json

# IMPORT TASK 9 HELPERS
from helpers.deduplicate import remove_duplicates
from helpers.downloader import download_media


def read_keywords(filename):

    with open(filename, "r", encoding="utf-8") as file:

        return [line.strip() for line in file]


def main():

    keywords = read_keywords("keywords.txt")

    all_posts = []

    # multiple searches
    for keyword in keywords:

        print(f"\nSearching: {keyword}")

        posts = scrape_reddit(keyword)

        # add context
        for post in posts:

            post["context"] = keyword

        print(f"Collected: {len(posts)} posts")

        all_posts.extend(posts)

    # remove duplicates
    unique_posts = remove_duplicates(all_posts)

    print(f"\nUnique posts: {len(unique_posts)}")

    # download videos/media
    download_media(unique_posts)

    # create data folder
    os.makedirs("data", exist_ok=True)

    # save merged results
    save_csv(unique_posts, "data/merged_results.csv")

    save_json(unique_posts, "data/merged_results.json")


if __name__ == "__main__":

    main()