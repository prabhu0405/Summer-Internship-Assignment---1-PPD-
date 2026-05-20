import requests
from retrying import retry

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


@retry(stop_max_attempt_number=3, wait_fixed=2000)
def fetch_page(url, params=None):
    """
    Fetch page with retry mechanism.
    """

    response = requests.get(
        url,
        headers=HEADERS,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.text