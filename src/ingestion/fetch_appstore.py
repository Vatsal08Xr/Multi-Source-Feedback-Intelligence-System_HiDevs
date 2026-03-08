import requests
import feedparser
import pandas as pd

def fetch_appstore_reviews(app_id):

    url = f"https://itunes.apple.com/rss/customerreviews/id={app_id}/sortby=mostrecent/json"

    feed = feedparser.parse(url)

    data = []

    for entry in feed.entries:

        data.append({
            "source": "appstore",
            "review": entry.title,
            "rating": 3,
            "date": entry.updated
        })

    return pd.DataFrame(data)