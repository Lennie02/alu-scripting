#!/usr/bin/python3
"""Module to query Reddit API for subscriber count."""
import json
import urllib.request


def number_of_subscribers(subreddit):
    """Return number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MyBot/1.0"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
