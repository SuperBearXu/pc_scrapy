
BOT_NAME = "douban"

SPIDER_MODULES = ["douban.spiders"]
NEWSPIDER_MODULE = "douban.spiders"

ROBOTSTXT_OBEY = False
LOG_LEVEL = "WARNING"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'douban.pipelines.DoubanPipeline': 300
}

IMAGES_STORE = './images'  # 图片保存路径
# 避免重复下载
IMAGES_EXPIRES = 90

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36'
}
