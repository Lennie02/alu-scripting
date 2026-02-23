#!/usr/bin/python3
"""Module to recursively count keywords in Reddit hot posts."""
import json
import urllib.request


def count_words(subreddit, word_list, counts={}, after=None):
    """Parse titles of hot posts and print sorted keyword counts."""
    if not counts:
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)

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
                title = post.get("data", {}).get("title", "").lower()
                words = title.split()
                for word in word_list:
                    word = word.lower()
                    counts[word] += words.count(word)
            after = data.get("data", {}).get("after")
            if after is None:
                sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    if count > 0:
                        print("{}: {}".format(word, count))
                return
            return count_words(subreddit, word_list, counts, after)
    except Exception:
        return
