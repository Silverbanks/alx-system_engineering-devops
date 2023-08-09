#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    '''A function that gets the total number of subscribers from reddit api'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    u_agent = 'mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return 0
    return response.json().get('data').get('subscribers')
