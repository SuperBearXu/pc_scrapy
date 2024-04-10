import scrapy
from scrapy import Request

from ..items import MyspiderItem


class GameSpider(scrapy.Spider):
    name = "game"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com/flash"]

    def url_next(self):
        urls = []
        for i in range(2, 11):
            url = f"https://www.4399.com/flash/new_{i}.htm"
            urls.append(url)
        return urls

    def parse(self, response):
        txts = response.xpath('//*[@id="skinbody"]/div[@class="bre oh"]/ul/li')
        for _ in txts:
            item = MyspiderItem()
            item["name"] = _.xpath('a/b/text()').get()
            item["type"] = _.xpath('em[1]/a/text()').get()
            item["time"] = _.xpath('em/text()').get()
            item["image"] = _.xpath('a/img/@lz_src').get()
            yield item
        urls = self.url_next()
        for url in urls:
            yield Request(url, callback=self.parse)
