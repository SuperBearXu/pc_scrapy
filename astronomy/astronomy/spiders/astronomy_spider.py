import scrapy
from scrapy import Request

from ..items import AstronomyItem


class AstronomySpiderSpider(scrapy.Spider):
    name = "astronomy_spider"
    allowed_domains = ["www.twxb.org"]
    start_urls = ["http://www.twxb.org/twxb/home"]

    url = "http://www.twxb.org/twxb/article/abstract/202403"
    index = 1

    def parse_detail(self, response):
        item = response.meta["item"]
        desc_en = response.xpath('//*[@id="EnAbstractValue"]/text()').extract_first()
        item["desc_en"] = desc_en
        yield item

    def parse(self, response):
        div_list = response.xpath('//div[@class="bd check_ww"]/ul[1]/div[@class="slideTxtBox_list"]')
        for div in div_list:
            title = div.xpath('./div/div[1]/a/text()').extract_first()
            author = div.xpath('./div/div[2]/span/a/text()').extract_first()
            desc_cn = div.xpath('./div/div[5]/span/text()').extract_first()

            item = AstronomyItem()
            item["title"] = title
            item["author"] = author
            item["desc_cn"] = desc_cn

            param = f"0{self.index}"
            if self.index >= 10:
                param = str(self.index)
            detail_url = format(self.url + param)
            self.index += 1
            # 请求传参
            yield Request(detail_url, callback=self.parse_detail, meta={"item": item})
