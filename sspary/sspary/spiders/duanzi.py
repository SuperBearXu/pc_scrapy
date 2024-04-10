import scrapy

from sspary.items import DuanziproItem


class DuanziSpider(scrapy.Spider):
    name = "duanzi"
    allowed_domains = ["duanzixing.com"]
    start_urls = ["https://duanzixing.com"]

    # 写入管道 持久化存储
    def parse(self, response):
        article_list = response.xpath('/html/body/section/div/div/article')
        for article in article_list:
            title = article.xpath('./header/h2/a/text()').extract_first()
            con = article.xpath('./p[2]/text()').extract_first()
            item = DuanziproItem()
            item['title'] = title
            item['con'] = con
            yield item
