from django.conf import settings

from urllib.parse import urlparse, parse_qs
import requests


def extract_video_id(yt_url):
    url = urlparse(yt_url)
    qs = parse_qs(url.query)
    return qs['v'][0]

def get_video_metadata(yt_id):
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {
        'id': yt_id,
        'part': 'contentDetails,snippet',
        'key': settings.YOUTUBE_API_KEY,
    }

    req = requests.get(url=url, params=params)
    json = req.json()['items']
    if not json:
        return None

    meta = {
        'title': json[0]['snippet']['title'],
        'author': json[0]['snippet']['channelTitle'],
        'duration': json[0]['contentDetails']['duration'],
    }
    return meta
