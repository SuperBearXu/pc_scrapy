# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class WangyiDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 该方法拦截五大板块对应的响应对象，进行篡改
    def process_response(self, request, response, spider):
        # print("中间件接收到的请求:", request.url)
        bro = spider.bro
        # 挑选出指定的响应对象进行篡改
        if request.url in spider.model_urls:
            # response #五大板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            # 获取动态加载内容（使用selenium操作）
            bro.get(request.url)
            # print("符合条件的请求：", request.url)
            time.sleep(2)
            page_txt = bro.page_source
            new_response = HtmlResponse(url=request.url,body=page_txt,encoding='utf-8',request=request)
            return new_response
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
