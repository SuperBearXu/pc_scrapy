# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SsparyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image_urls = scrapy.Field()


class ForesightItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    amount = scrapy.Field()
    amount_unit = scrapy.Field()
    amount_round = scrapy.Field()
    date = scrapy.Field()
    pass


class DuanziproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    con = scrapy.Field()


class SpiderItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
