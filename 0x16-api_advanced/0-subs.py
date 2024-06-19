#!/usr/bin/python3
'''a function that queries the Reddit API and returns the number of subscribers for a given subreddit.'''
import requests

def number_of_subscribers(subreddit):
    '''Returns total number of subscribers on a given subreddit.'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
           return 0

        data = response.json().get("data", {})
        return data.get("subscribers", {})
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
