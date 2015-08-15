import twitter
import requests

from spiders.config import api_credentials

requests.packages.urllib3.disable_warnings()

class SweepRequester:
    def __init__(self):
        self.api = twitter.Api(consumer_key=api_credentials['consumer_key'],
            consumer_secret=api_credentials['consumer_secret'],
            access_token_key=api_credentials['access_token_key'],
            access_token_secret=api_credentials['access_token_secret']
        )

    def request_sweepstake_statuses(self):
        keywords = {
            # 'main': ['#contest', '#giveaway', 'RT to win']
            'main': ['#contest RT', '#giveaway RT']
        }
        self.statuses = []

        # loop through keywords main and append to an array
        for word in keywords['main']:
            results = self.api.GetSearch(term=word, count=50)
            for result in results:
                if self.not_yet_included(result):
                    self.statuses.append(result)

        return self.statuses

    def not_yet_included(self, status):
        for s in self.statuses:
            if s.id == status.id:
                return False
        return True
