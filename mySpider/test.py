import hashlib


# 下载的图片默认会以url的sha1值进行命名
def sha256_generator(str):
    m = hashlib.sha1()
    m.update(str.encode())
    return m.hexdigest()


if __name__ == "__main__":
    print(sha256_generator("https://img3.doubanio.com/view/photo/m/public/p2887770127.webp"))
