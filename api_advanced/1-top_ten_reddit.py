#!/usr/bin/python3
"""Print the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts, or None if invalid."""
    if not isinstance(subreddit, str) or not subreddit:
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api_advanced:v1.0 (by /u/rruzigana-hub)"
    }

    try:
        response = requests.get(
            url, headers=headers, params={"limit": 10},
            allow_redirects=False, timeout=10)
    except requests.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
