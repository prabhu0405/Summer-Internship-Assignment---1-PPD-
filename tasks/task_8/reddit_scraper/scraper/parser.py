from bs4 import BeautifulSoup


def parse_reddit_posts(html):
    """
    Parse Reddit search page and extract post data.
    """

    soup = BeautifulSoup(html, "lxml")

    posts = []

    # Reddit shreddit posts
    post_blocks = soup.find_all("shreddit-post")

    for post in post_blocks:

        title = post.get("post-title", "N/A")

        username = post.get("author", "N/A")

        post_link = post.get("permalink", "")

        timestamp = post.get("created-timestamp", "N/A")

        score = post.get("score", "N/A")

        comments = post.get("comment-count", "N/A")

        media_link = "N/A"

        # Check for video/image
        if post.get("content-href"):
            media_link = post.get("content-href")

        posts.append({
            "tweet_text": title,   # keeping field name same as assignment
            "username": username,
            "tweet_link": f"https://www.reddit.com{post_link}",
            "media_link": media_link,
            "timestamp": timestamp,
            "likes": score,
            "reposts/comments": comments
        })

    return posts