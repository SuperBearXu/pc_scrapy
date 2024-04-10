import hashlib
import json
import os

# import pymysql
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes

# from sspary import settings
# from sspary.settings import MYSQL_CONFIG as mysql


class SsparyPipeline(ImagesPipeline):
    def open_spider(self, spider):
        print('爬虫开始时调用一次')

    def process_item(self, item, spider):
        print(item)
        return item

    # # 1. 发送请求(下载图片, 文件, 视频,xxx)
    # def get_media_requests(self, item, info):
    #     # 获取到图片的url
    #     url = item['image_urls']
    #     meta_data = {'key': 'value'}
    #
    #     for i in url:
    #         # 进行请求
    #         # print(item['name'][0])
    #         yield scrapy.Request(url=i, callback=self.test, meta=meta_data)  # 直接返回一个请求对象即可

    def close_spider(self, spider):
        print('爬虫结束时被调用')


class ITSpiderPipeline:
    f = None

    def open_spider(self, spider):
        print('爬虫开始时被调用一次')
        self.f = open('./duanzi.txt', 'w', encoding='utf-8')

    # 爬虫文件中提取数据的方法每yield一次item，就会运行一次
    # 该方法为固定名称函数
    def process_item(self, item, spider):
        print(item)
        # self.f.write(item['title'] + item['con'] + '\n')
        return item

    def close_spider(self, spider):
        print('爬虫结束时被调用')
        self.f.close()


class SpiderPipeline:

    def __init__(self):
        # self.conn = None
        self.f = None

    def open_spider(self, spider):
        # 写入到文件中
        # self.f = open('../shuyou.csv', 'w', encoding='utf-8')
        self.f = open('../shuyou.txt', 'a', encoding='utf-8')
        print('爬虫开始时被调用一次')
        # self.conn = pymysql.connect(host=mysql["host"], port=mysql["port"], user=mysql["user"], password=mysql["password"], database=mysql["database"])

    # 爬虫文件中提取数据的方法每yield一次item，就会运行一次
    # 该方法为固定名称函数
    def process_item(self, item, spider):
        # print(item)
        # self.f.write(item['title'] + item['text'] + '\n')
        # 写入文件
        # self.f.write(f"{item['title']},{item['text']}\n")

        # try:
        #     cursor = self.conn.cursor()
        #     sql = "insert into juejin(title, text) values(%s, %s)"
        #     cursor.execute(sql, (item['title'], item['text']))
        #     self.conn.commit()
        #     spider.logger.info(f"保存数据{item}")
        # except Exception as e:
        #     self.conn.rollback()
        #     spider.logger.error(f"保存数据库失败!", e, f"数据是: {item}")  # 记录错误日志

        item = dict(item)
        # 爬虫文件中提取数据的方法每yield一次，就会运行一次
        # 该方法为固定名称函数
        # 默认使用完管道，需要将数据返回给引擎
        # 1.将字典数据序列化
        '''ensure_ascii=False 将unicode类型转化为str类型，默认为True'''
        json_data = json.dumps(item, ensure_ascii=False, indent=2) + ',\n'
        # print(json_data)
        self.f.write(json_data)
        return item

    def close_spider(self, spider):
        print('爬虫结束时被调用')
        self.f.close()
        # self.conn.close()
