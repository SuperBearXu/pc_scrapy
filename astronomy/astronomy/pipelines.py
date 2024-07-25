# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AstronomyPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        print("open...")
        self.conn = pymysql.Connection(host="127.0.0.1", port=3306, user="root", password="123456", database="spider")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into astronomy values("%s","%s","%s","%s")'%(item["title"],item["author"],item["desc_cn"],item["desc_en"]))
            self.conn.commit()
        except Exception as e:
            print("Exception:", e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        print("close...")
        self.cursor.close()
        self.conn.close()
