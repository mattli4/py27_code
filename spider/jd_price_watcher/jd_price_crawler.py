# -*- coding:UTF-8 -*-
import requests
from xml.dom import minidom
import json


class Watcher:
    def __init__(self):
        doc = minidom.parse('./config.xml')
        root = doc.documentElement
        self.url = root.getElementsByTagName('url')[0].childNodes[0].nodeValue
        item_id = self.url.split('/')[-1].split('.')[0]
        self.price_utl = 'https://p.3.cn/prices/mgets?skuIds=J_' + item_id
        self.item = root.getElementsByTagName('name')[0].childNodes[0].nodeValue
        self.first_read = root.getElementsByTagName('firstread')[0].childNodes[0].nodeValue
        self.headers = {
                        'Accept': 'text / html, application / xhtml + xml, application / xml; '
                                  'q = 0.9, image / webp, image / apng, * / *;q = 0.8',
                        'Accept - Encoding': 'gzip, deflate',
                        'Accept - Language': 'zh - CN, zh;q = 0.8',
                        'Connection': 'keep - alive',
                        'Cache - Control': 'max - age = 0',
                        'Host': 'p.3.cn',
                        'Upgrade - Insecure - Requests': '1',
                        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) '
                                        'AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 59.0.3071.115 Safari / 537.36'
        }
        self.session = requests.Session()

    def get_price(self):
        print '正在查询，请稍后...'
        price_get = self.session.get(self.price_utl, headers=self.headers, allow_redirects=True)
        price_json = price_get.text
        price_json = json.loads(price_json)
        price = price_json[0]['p']
        print self.item, price

if __name__ == '__main__':
    w = Watcher()
    w.get_price()
