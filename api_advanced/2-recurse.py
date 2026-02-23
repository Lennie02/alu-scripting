#!/usr/bin/python3
"""Module to recursively query Reddit API for all hot posts."""
import json
import urllib.request


def recurse(subreddit, hot_list=[], after=None):
    """Return list of titles of all hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "linux:myredditapp:v1.0 (by /u/myusername)"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                hot_list.append(post.get("data", {}).get("title"))
            after = data.get("data", {}).get("after")
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after)
    except Exception:
        return None
