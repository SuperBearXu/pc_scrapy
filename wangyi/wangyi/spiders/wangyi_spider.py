import scrapy
from scrapy import Request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from ..items import WangyiItem


class WangyiSpiderSpider(scrapy.Spider):
    name = "wangyi_spider"
    # allowed_domains = ["news.163.com"]
    start_urls = ["https://news.163.com/"]

    model_urls = []

    def __init__(self):
        service = Service('D:\scrapy\project\pc_scrapy\wangyi\wangyi\chromedriver.exe')
        self.bro = webdriver.Chrome(service=service)

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[3]/div[2]/div[2]/div[2]/div/ul/li')
        i_list = [1, 2, 4, 5, 9]
        for index in i_list:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)

        # 依次对每个模块的url进行解析
        for url in self.model_urls:
            # print("请求前的url：", url)
            yield Request(url, callback=self.parse_model)

    # 解析动态加载的内容
    def parse_model(self, response):
        div_list = response.xpath('//*[@class="newsdata_wrap"]/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            content_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyiItem()
            item['title'] = title
            # print(content_url)
            # print(type(content_url))
            if content_url is None:
                continue
            yield Request(content_url, callback=self.parse_detail, meta={"item": item})

    def parse_detail(self, response):
        print(response.meta["item"])
        item = response.meta["item"]
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item['content'] = content
        print(item)
        # yield item

    def close(self, spider):
        self.bro.close()
