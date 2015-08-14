import twitter
import requests
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

from spiders.config import api_credentials, user_agents
from spiders.status import StatusSpider

requests.packages.urllib3.disable_warnings()

class SweepsFinder:
    def __init__(self):
        self.api = twitter.Api(consumer_key=api_credentials['consumer_key'],
            consumer_secret=api_credentials['consumer_secret'],
            access_token_key=api_credentials['access_token_key'],
            access_token_secret=api_credentials['access_token_secret']
        )

    def process_status(self, status):
        # TODO: Check if it is the original tweet
        if status.retweeted:
            return None

        # TODO: Filter tweet and find out if I should follow
        # tweet = status.text
        return {
            'tweet': status.text,
            'user': status.user.name,
            'id': status.id
        }

    def not_yet_included(self, status, statuses):
        for s in statuses:
            if s['id'] == status.id:
                return False
        return True

    def filter_out_sweepstakes(self):
        keywords = {
            # 'main': ['#contest', '#giveaway', 'RT to win']
            'main': ['#contest']
        }
        statuses = []

        # loop through keywords main and append to an array
        for word in keywords['main']:
            results = self.api.GetSearch(term=word)
            for result in results:
                if self.not_yet_included(result, statuses):
                    status = self.process_status(result)
                    if status: statuses.append(status)

        return statuses

    def get_sweepstakes_and_crawl(self):
        sweepstakes = self.filter_out_sweepstakes()
        status_spider = StatusSpider(statuses=sweepstakes)

        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(status_spider)
        crawler.start()
        log.start()
        reactor.run()



