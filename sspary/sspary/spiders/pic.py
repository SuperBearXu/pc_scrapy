from urllib.parse import urljoin

import scrapy

from ..items import SsparyItem


class PicSpider(scrapy.Spider):
    name = "pic"
    allowed_domains = ["pic.netbian.com"]
    start_urls = ["https://pic.netbian.com/4kfengjing/index.html"]

    def parse(self, response):
        try:
            items = SsparyItem()
            lists = response.css('.slist .clearfix li')
            for li in lists:
                url = li.css('a img::attr(src)').extract_first()
                name = li.css('a img::attr(alt)').extract_first()

                items['image_urls'] = [urljoin(self.start_urls[0], url)]
                items['name'] = [name]
                yield items
        except Exception as e:
            print(f"报错{e}")

        # if self.page < 10:
        #       self.page += 1
        # url = f'https://pic.netbian.com/4kfengjing/index_{str(self.page)}.html'

        # url = urljoin('https://pic.netbian.com/4kfengjing/index.html', items['image_urls'])
        # print(url)
        # print(items['image_urls'])
        # yield scrapy.Request(url=url, callback=self.parse)
