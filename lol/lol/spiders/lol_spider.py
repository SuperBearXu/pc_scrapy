from copy import deepcopy

import scrapy
from scrapy import Request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from ..items import LolItem


class LolSpiderSpider(scrapy.Spider):
    name = "lol_spider"
    # allowed_domains = ["101.qq.com"]
    start_urls = ["https://101.qq.com/#/hero"]
    # start_urls = ["https://101.qq.com/#/hero-detail?heroid=1"]

    base_url = "https://101.qq.com/"
    allow_urls = ["https://101.qq.com/#/hero"]

    def __init__(self):
        service = Service('D:\scrapy\project\pc_scrapy\lol\lol\chromedriver.exe')
        self.bro = webdriver.Chrome(service=service)

    def parse(self, response):
        li_list = response.xpath('//*[@id="app"]/div/div[3]/div/div[2]/ul/li')
        for li in li_list:
            name = li.xpath('./div/p/text()').extract_first()
            detail_url = li.xpath('./a/@href').extract_first()

            hero_id = get_hero_id(detail_url)
            item = LolItem()
            item['hero_name'] = name
            item['hero_id'] = hero_id

            new_url = self.base_url+detail_url
            # new_url = "https://101.qq.com/#/hero-detail?heroid=1"
            # self.allow_urls.append(new_url)
            # print(name, hero_id)
            yield Request(new_url, callback=self.parse_detail, meta={"item": item})
            print(new_url)

    def parse_detail(self, response):
        print(response.meta["item"])
        item = response.meta["item"]
        # skins_dic = {}
        # skins = []
        # div_list = response.xpath('//*[@class="swiper-wrapper"]/div')
        # for div in div_list:
        #     skin_name = div.xpath('./img/@alt').extract_first()
        #     skin_url = div.xpath('./img/@src').extract_first()
        #
        #     skins_dic["skin_name"] = skin_name
        #     skins_dic["skin_url"] = skin_url
        #     skins.append(deepcopy(skins_dic))
        #
        # item["skins"] = skins
        # # print(item)
        yield item

    # def close(self, spider):
    #     self.bro.close()


def get_hero_id(url):
    # 使用 split 方法，分割字符串
    list = url.split("=")
    # 取出第二部分
    hero_id = list[1].strip()  # strip 用来移除可能的额外空格
    return hero_id

# 遗留问题，yield Request(new_url, callback=self.parse_detail, meta={"item": item}) 只调用了一次就结束