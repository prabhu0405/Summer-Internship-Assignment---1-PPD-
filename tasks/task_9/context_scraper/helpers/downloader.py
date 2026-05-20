import os
import requests


def download_media(posts):

    for post in posts:

        media_url = post["media_link"]

        if media_url == "N/A":
            continue

        # category name
        context = post["context"].split()[0].lower()

        folder_path = f"videos/{context}"

        os.makedirs(folder_path, exist_ok=True)

        try:

            response = requests.get(media_url, timeout=10)

            if response.status_code == 200:

                filename = media_url.split("/")[-1]

                if "." not in filename:
                    filename += ".mp4"

                file_path = os.path.join(folder_path, filename)

                with open(file_path, "wb") as file:

                    file.write(response.content)

                print(f"Downloaded: {file_path}")

        except Exception as error:

            print("Download failed:", error)