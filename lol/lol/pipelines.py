import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from .settings import MYSQL_CONFIG as mysql


class LolMysqlPipeline:
    conn = None
    cursor = None

    # def open_spider(self, spider):
        # print("建立数据库连接")
        # self.conn = pymysql.Connection(host=mysql['host'], port=mysql['port'], user=mysql['username'],
        #                                password=mysql['password'], database=mysql['database'])

    def process_item(self, item, spider):
        # list_skin = item['skins']
        # print("list_skin", list_skin)
        # self.cursor = self.conn.cursor()
        # try:
        #     self.cursor.execute('insert into hero values("%s", "%s")' % (item['hero_id'], item['hero_name']))
        #     for skin in list_skin:
        #         self.cursor.execute('insert into skin (skin_name, skin_url, hero_id) values("%s", "%s", "%s")' %
        #                             (skin['skin_name'], skin['skin_url'], item['hero_id']))
        #     self.conn.commit()
        # except Exception as e:
        #     print("Exception:", e)
        #     self.conn.rollback()
        # print(item)
        return item

    # def close_spider(self, spider):
        # print("关闭数据库连接")
        # self.cursor.close()
        # self.conn.close()


# class LolImagePipeline(ImagesPipeline):
#
#     # 就是可以根据图片地址进行图片数据的请求
#     def get_media_requests(self, item, info):
#         skin_list = item['skins']
#         for skin in skin_list:
#             yield scrapy.Request(skin["skin_url"], meta={'item': item, 'skin_name': skin['skin_name']})
#
#     # 指定图片存储的路径
#     def file_path(self, request, response=None, info=None, *, item=None):
#         item = request.meta['item']
#         hero_name = item["hero_name"]
#         skin_name = request.meta['skin_name']
#         file_name = f'{hero_name}/{skin_name}.jpg'
#         return file_name
#
#     def item_completed(self, results, item, info):
#         for ok, x in results:
#             if ok:
#                 print(f'已完成下载: {x["path"]}')  # 添加调试信息
#             else:
#                 print(f'下载失败: {x["url"]}')  # 添加调试信息
#         return item  # 返回给下一个即将被执行的管道类
