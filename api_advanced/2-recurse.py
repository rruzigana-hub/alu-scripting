#!/usr/bin/python3
"""Recursively query the Reddit API for the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return the titles of all hot posts of a subreddit.

    Return None if the subreddit is invalid or has no posts.
    """
    if hot_list is None:
        hot_list = []
    if not isinstance(subreddit, str) or not subreddit:
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api_advanced:v1.0 (by /u/rruzigana-hub)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10)
    except requests.RequestException:
        return hot_list or None

    if response.status_code != 200:
        return hot_list or None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return hot_list or None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list or None
    return recurse(subreddit, hot_list, after)
