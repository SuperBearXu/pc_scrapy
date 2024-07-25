# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LolItem(scrapy.Item):
    hero_name = scrapy.Field()
    hero_id = scrapy.Field()
    # skin_names = scrapy.Field()
    # skin_urls = scrapy.Field()
    skins = scrapy.Field()

