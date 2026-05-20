from scraper.reddit_scraper import scrape_reddit
from scraper.saver import save_csv, save_json


def main():

    keywords = [
        "AI generated videos",
        "Robotics demos",
        "Self-driving cars",
        "Sports highlights"
    ]

    all_posts = []

    for keyword in keywords:

        print(f"\nSearching for: {keyword}")

        try:
            posts = scrape_reddit(keyword)

            print(f"Collected {len(posts)} posts")

            all_posts.extend(posts)

        except Exception as error:

            print(f"Error while scraping {keyword}")

            print(error)

    # Save outputs
    save_csv(all_posts, "data/reddit_posts.csv")

    save_json(all_posts, "data/reddit_posts.json")


if __name__ == "__main__":
    main()