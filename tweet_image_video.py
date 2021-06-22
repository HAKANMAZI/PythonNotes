import snscrape.modules.twitter as sntwitter
import snscrape
import requests
import urllib.request
import os
from urllib.parse import urlparse



def photo_save(photo_url):
    a = urlparse(photo_url)
    photo_name = os.path.basename(a.path)
    with open(photo_name+'.jpg', 'wb') as f:
        f.write(requests.get(photo_url).content)

def video_save(url_link):
    a = urlparse(url_link)
    video_name = os.path.basename(a.path)
    urllib.request.urlretrieve(url_link, video_name+'.mp4')
      
name ='_tekoazad_e___'
for tweet in snscrape.modules.twitter.TwitterUserScraper(username=name).get_items():
        if tweet.media:
            for medium in tweet.media:
                if medium.type == 'photo': photo_save(medium.fullUrl)
                elif medium.type == 'video':
                    for v in medium.variants:
                        if '.mp4' in v.url : video_save(v.url)
                        