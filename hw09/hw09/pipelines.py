# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class Hw09Pipeline:
    def process_item(self, item, spider):
        return item

class QuotesPipeLine:
    quotes = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.quotes.append(dict(adapter))

    def close_spider(self, spider):
        with open("quotes.json", "w", encoding="utf-8") as f:
            json.dump(self.quotes, f, ensure_ascii=False, indent=2)

class AuthorsPipeLine:
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.authors.append(dict(adapter))

    def close_spider(self, spider):
        with open("authors.json", "w", encoding="utf-8") as f:
            json.dump(self.authors, f, ensure_ascii=False, indent=2)