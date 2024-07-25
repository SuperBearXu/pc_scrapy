import scrapy
from scrapy import Request

from ..items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    name = "douban_spider"
    allowed_domains = ["douban.com"]
    start_urls = ["https://www.douban.com/photos/album/1881849723"]

    # def url_next(self):
    #     urls = []
    #     for i in range(1, 3):
    #         page = i * 18
    #         url = f"https://www.douban.com/photos/album/1881849723/?m_start={page}"
    #         urls.append(url)
    #     return urls
    wangzhi = "https://www.douban.com/photos/album/1881849723/?m_start=%d"
    page_num = 1
    page_offset = 0

    def parse(self, response):

        lists = response.css('#content > div.grid-16-8.clearfix > div.article > div.photolst .photo_wrap > a')
        # print(lists)
        for li in lists:
            item = DoubanItem()
            item['img_url'] = li.css('a > img[src]::attr(src)').get()
            yield item

        # urls = self.url_next()
        # for url in urls:
        #     yield Request(url, callback=self.parse)

        if self.page_num < 2:
            self.page_offset = self.page_num * 18
            new_url = format(self.wangzhi % self.page_offset)
            self.page_num += 1
            yield Request(new_url, callback=self.parse)

