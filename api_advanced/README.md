# api_advanced

Python scripts that use the Reddit API with the `requests` module.

## Files

| File | What it does |
| ---- | ------------ |
| `0-subs.py` | `number_of_subscribers(subreddit)` returns the number of subscribers, or 0 if the subreddit is invalid |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts, or None if invalid |
| `2-recurse.py` | `recurse(subreddit, hot_list=None, after=None)` returns the titles of all hot posts, using recursion and pagination |
| `3-count.py` | `count_words(subreddit, word_list)` prints a sorted count of keywords in the hot post titles, using recursion |

## Notes

- A custom User-Agent is set in every request.
- Redirects are not followed, because an invalid subreddit redirects to a search page.

## Author

Ruzigana Irakiza Junior Raul (rruzigana-hub), African Leadership University
