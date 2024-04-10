import scrapy

from sspary.items import ForesightItem


class FundraisingSpider(scrapy.Spider):
    name = "fundraising"
    allowed_domains = ["foresightnews.pro"]
    start_urls = ["https://foresightnews.pro/wiki/fundraising"]

    def parse(self, response):
        # elements = response.xpath('//*[@class="invest InvestCord"]')
        # elements = response.xpath('//*[@id="layout-body"]')
        elements = response.css('.module')
        # print(response)
        # print(elements)
        # 打印抓取到的页面源码
        print(response.body)
        for element in elements:
            item = ForesightItem()
            item_name = element.xpath('./div/div/span[@class="name"]/text()').extract()
            item_amount = element.xpath('./div[1]/div[2]/div[1]/text()').extract()[0].strip()
            item_amount_unit = element.xpath('./div[1]/div[2]/div[1]/span/text()').extract()
            item_amount_round = element.xpath('./div[1]/div[2]/div[2]/text()').extract()
            item_date = element.xpath('./div[1]/div[3]/text()').extract()
            # print(f"名字：{item_name}, 融资金额： {item_amount},{item_amount_unit}融资轮次： {item_amount_round},日期： {item_date}")

            item['name'] = item_name
            item['amount'] = item_amount
            item['amount_unit'] = item_amount_unit
            item['amount_round'] = item_amount_round
            item['date'] = item_date

            # return or yield ？
            yield item
