#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers, or 0 if the subreddit is invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api_advanced:v1.0 (by /u/rruzigana-hub)"
    }

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
    except ValueError:
        return 0

    return data.get("subscribers") or 0
