from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

from sweep_requester import SweepRequester
from sweep_processor import SweepProcessor
from spiders.status import StatusSpider
from spiders.config import user_agents

requester = SweepRequester()
processor = SweepProcessor()

sweepstakes = requester.request_sweepstake_statuses()
sweepstakes = map(processor.process_status, sweepstakes)

status_spider = StatusSpider(statuses=sweepstakes)

settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(status_spider)
crawler.start()
log.start()
reactor.run()

