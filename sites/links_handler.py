import json
from urllib import response
import requests
import time


class LinksProcessor:
    def dailymotion(self, links):
        processed_links = []
        for link in links:
            # Process the links using the dailymotion logic
            savethevideo = "https://api.w03.savethevideo.com/tasks"
            obj = {"type": "info", "url": link}
            response = requests.post(savethevideo, json=obj)
            response = json.loads(response.text)['href']
            g1 = "https://api.w03.savethevideo.com//" + response
            time.sleep(5)
            r2 = requests.get(g1)
            download_link = json.loads(r2.text)
            download_link = download_link['result']['url']
            processed_links.append(download_link)
        return processed_links

    def fembed(self, links):
        processed_links = []
        # Process the links using the fembed logic
        # ...
        return processed_links

    def netu(self, links):
        processed_links = []
        # Process the links using the netu logic
        # ...
        return processed_links

    def fastvideo(self, links):
        processed_links = []
        # Process the links using the fastvideo logic
        # ...
        return processed_links
