import requests
from retrying import retry


HEADERS = {
    "User-Agent": "python:reddit.scraper:v1.0 (by /u/demo)"
}


@retry(stop_max_attempt_number=3, wait_fixed=2000)
def scrape_reddit(keyword):

    url = "https://www.reddit.com/search.json"

    params = {
        "q": keyword,
        "limit": 10,
        "raw_json": 1
    }

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        timeout=15
    )

    # DO NOT use raise_for_status directly
    if response.status_code != 200:
        print(f"Failed with status code: {response.status_code}")
        return []

    data = response.json()

    posts = []

    children = data.get("data", {}).get("children", [])

    for child in children:

        post = child.get("data", {})

        media_link = "N/A"

        if post.get("url_overridden_by_dest"):
            media_link = post["url_overridden_by_dest"]

        posts.append({
            "tweet_text": post.get("title", "N/A"),
            "username": post.get("author", "N/A"),
            "tweet_link": f"https://reddit.com{post.get('permalink', '')}",
            "media_link": media_link,
            "timestamp": post.get("created_utc", "N/A"),
            "likes": post.get("ups", 0),
            "reposts/comments": post.get("num_comments", 0)
        })

    return posts