# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class XhsPipeline:
    fp = None

    def open_spider(self, spider):
        print("开始调用爬虫...")
        self.fp = open("./xhs.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        author = item['author']
        title = item['title']
        self.fp.write(author + ":" + title + "\n")
        return item

    def close_spider(self, spider):
        print("结束调用爬虫...")
        self.fp.close()


class XhsMysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print("开始爬虫...")
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database="spider")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into xhs values("%s","%s")'%(item["author"],item["title"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self, spider):
        print("结束爬虫...")
        self.cursor.close()
        self.conn.close()
