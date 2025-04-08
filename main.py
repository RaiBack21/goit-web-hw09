from scrapy.crawler import CrawlerProcess

from hw09.hw09.spiders.quotes import QuotesSpider
from hw09.hw09.spiders.authors import AuthorsSpider

procces = CrawlerProcess()
procces.crawl(AuthorsSpider)
procces.crawl(QuotesSpider)
procces.start()