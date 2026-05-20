def remove_duplicates(posts):

    unique_links = set()

    unique_posts = []

    for post in posts:

        link = post["tweet_link"]

        if link not in unique_links:

            unique_links.add(link)

            unique_posts.append(post)

    return unique_posts