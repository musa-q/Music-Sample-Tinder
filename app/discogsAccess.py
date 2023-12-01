import sys
sys.path.append('..')

import time
import discogs_client
from config import DISCOGS

class DiscogsAccess:
    def __init__(self):
        self.discogsClient = discogs_client.Client('ExampleApplication/0.1', user_token=DISCOGS.TOKEN)
        self.allTracks = []

    def getTracks(self, startPage=1, endPage=5, timeout=1):
        tracks = []
        for page in range(startPage, endPage):
            results = self.discogsClient.search(type='release', page=page)
            tracks.extend(results.page(1))
            print(f"[Page retrieved] Page : {page}")
            time.sleep(timeout)
        return tracks

    def searchTracks(self, searchItem, searchType='release'):
        results = self.discogsClient.search(searchItem, type=searchType)
        return results