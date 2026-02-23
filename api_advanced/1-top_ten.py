#!/usr/bin/python3
"""Module to query Reddit API for top 10 hot posts."""
import json
import urllib.request


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MyBot/1.0"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
