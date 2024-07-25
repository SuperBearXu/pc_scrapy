import hashlib

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.python import to_bytes


class DoubanPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        file_name = f'{media_guid}.jpg'
        print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        # print("results", results)
        for ok, result in results:
            if ok:
                path = result['path']
                # print(f'Downloaded image saved in {path}')
        return item

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])
