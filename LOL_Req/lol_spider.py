import gzip
import json

import requests

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2865511"
    res = requests.get(url, headers)
    # print(res.text)
    # print(gzip.decompress(bytes(res.text, 'utf-8')).decode('utf-8'))
    # str = "\u5b89\u59ae"
    # print(str)
    json_data = json.loads(res.text)
    print(json_data)
    fp = open("./lol.json", "w", encoding="utf-8")
    json.dump(json_data, fp, ensure_ascii=False)
