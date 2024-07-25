import scrapy

from ..items import XhsItem


class XhsSpiderSpider(scrapy.Spider):
    name = "xhs_spider"
    allowed_domains = ["www.xiaohongshu.com"]
    start_urls = ["https://www.xiaohongshu.com/explore"]

    def parse(self, response):
        sec_list = response.xpath('//div[@id="exploreFeeds"]/section')
        for sec in sec_list:
            author = sec.xpath('./div/div/div/a/span/text()').extract_first()
            title = sec.xpath('./div/div/a/span/text()').extract_first()

            item = XhsItem()
            item['author'] = author
            item['title'] = title

            yield item
