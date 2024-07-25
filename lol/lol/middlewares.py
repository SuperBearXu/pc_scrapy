# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class LolDownloaderMiddleware:

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

    def process_response(self, request, response, spider):
        bro = spider.bro
        # 此处做限制是防止后面单独请求图片时使用浏览器访问，这样无法下载图片
        bro.get(request.url)
        time.sleep(3)
        page_txt = bro.page_source
        new_response = HtmlResponse(url=request.url, body=page_txt, encoding='utf-8', request=request)
        return new_response
        # if request.url in spider.allow_urls:
        #     bro.get(request.url)
        #     time.sleep(3)
        #     page_txt = bro.page_source
        #     new_response = HtmlResponse(url=request.url, body=page_txt, encoding='utf-8', request=request)
        #     return new_response
        # else:
        #     return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
