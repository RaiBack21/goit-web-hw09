import scrapy

from hw09.hw09.pipelines import AuthorsPipeLine

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = { 
        "ITEM_PIPELINES": {AuthorsPipeLine: 100}
        }

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            link = quote.xpath("span/a/@href").get()
            yield response.follow(link, self.parse_author)
            
            next_link = response.xpath("/html//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(url=self.start_urls[0]+next_link)

    def parse_author(self, response):
        yield {
            "fullname": response.xpath("//h3[@class='author-title']/text()").get(),
            "born_date": response.xpath("//span[@class='author-born-date']/text()").get(),
            "born_location": response.xpath("//span[@class='author-born-location']/text()").get(),
            "description": response.xpath("//div[@class='author-description']/text()").get().strip(),
        }