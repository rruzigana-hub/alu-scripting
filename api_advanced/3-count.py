#!/usr/bin/python3
"""Recursively count keywords in the titles of hot posts of a subreddit."""
import requests


def get_page(subreddit, after=None):
    """Return the data of one page of hot posts, or None if it fails."""
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
        return None

    if response.status_code != 200:
        return None

    try:
        return response.json().get("data", {})
    except ValueError:
        return None


def print_counts(counts, multiples):
    """Print the keyword counts, sorted by count then by name."""
    totals = {}
    for word, number in counts.items():
        if number > 0:
            totals[word] = number * multiples[word]
    for word in sorted(totals, key=lambda name: (-totals[name], name)):
        print("{}: {}".format(word, totals[word]))


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the keywords found in hot post titles."""
    if not isinstance(subreddit, str) or not subreddit:
        return
    if counts is None:
        counts = {}

    multiples = {}
    for word in word_list:
        key = word.lower()
        multiples[key] = multiples.get(key, 0) + 1

    data = get_page(subreddit, after)
    if data is None:
        print_counts(counts, multiples)
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for word in title.lower().split():
            if word in multiples:
                counts[word] = counts.get(word, 0) + 1

    after = data.get("after")
    if after is None:
        print_counts(counts, multiples)
    else:
        count_words(subreddit, word_list, after, counts)
