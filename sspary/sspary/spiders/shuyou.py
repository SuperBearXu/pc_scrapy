import scrapy

from sspary.items import SpiderItem


class ShuyouSpider(scrapy.Spider):
    name = "shuyou"
    allowed_domains = ["juejin.cn/"]
    start_urls = ["https://juejin.cn/post/7298635806474502180?searchId=202402211647594D222B048945F22E300F"]

    def parse(self, response):
        # print(response.text)
        # element = response.xpath('//*[@id="app"]/section/section/main/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div['
        #                          '1]/div/table/tbody/tr[1]')
        elements = response.xpath('//*[@id="article-root"]/ul[1]/li')

        for element in elements:
            title = element.xpath('./strong/text()').extract_first().strip()
            text = element.xpath('./text()').extract_first().replace('：', '').replace(':', '').replace(',', '，').strip()
            item = SpiderItem()
            item['title'] = title
            item['text'] = text
            yield item
