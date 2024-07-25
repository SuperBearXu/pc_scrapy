1、创建scrapy项目
scrapy startproject 项目名
如：scrapy startproject xhs

2、创建爬虫
cd 项目名
scrapy genspider 爬虫名 目标网址
如：scrapy genspider xhs_spider https://www.xiaohongshu.com/explore

3、 运行爬虫
scrapy crawl 爬虫名
如：scrapy crawl xhs_spider

流程：
    1.数据解析
    2.在item类中定义相关的属性
    3.将解析的数据封装存储到item类型的对象
    4.将item类型的对象提交给管道进行持久化存储的操作
    5.在管道类的process_item中要将其接受到的item对象中存储的数据进行持久化存储操作
    6.在配置文件中开启管道

动态加载数据的爬取：
    利用selenium和scrapy的结合，通过下载中间件DownloaderMiddleware 拦截到所有响应response
并对指定的url进行拦截， 在中间件中使用selenium来加载需要动态加载的页面，并爬取到页面内容page_source，
将爬取到 的内容添加至新的响应new_response中，并返回给spider，由它对新的响应进行数据解析。

4、全站数据爬取--创建爬虫 (https://www.bilibili.com/video/BV1ha4y1H7sx?p=77&vd_source=20a77dd11c570bbda9c55b7e870bb959)
scrapy genspider -t crawl 爬虫名 目标网址
如：scrapy genspider -t crawl xhs_pro https://www.xiaohongshu.com/explore

5、图片爬取
    --- 数据解析（图片的地址）
    --- 将存储图片地址的item提交到制定的管道类
    --- 在管道文件中自定制一个基于ImagesPipeline的一个管道类
        - get_media_request
        - file_path
        - item_completed
    --- 在配置文件中：
        - 指定图片存储的目录：IMAGES_STORE = './images'
        - 指定开启的管道：自定制的管道类