import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     print(item)
    #     return item

    def file_path(self, request, response=None, info=None, *, item=None):
        name = item['name']
        type = item['type']
        file_name = f'{type}/{name}.jpg'
        return file_name

    def item_completed(self, results, item, info):
        # image_paths = [x['path'] for ok, x in results if ok]
        # if image_paths:
        #     item['image_paths'] = image_paths
        for ok, result in results:
            if ok:
                path = result['path']
                print(f'Downloaded image saved in {path}')
        return item

    def get_media_requests(self, item, info):
        if item['image'] is not None:
            image_paths = "https:" + item['image']
            yield scrapy.Request(image_paths)
