# -*- coding:UTF-8 -*-
import requests
from xml.dom import minidom
import json
import string


class Watcher:
    def __init__(self):
        self.doc = minidom.parse('./config.xml')
        self.root = self.doc.documentElement
        self.url = self.root.getElementsByTagName('url')[0].childNodes[0].nodeValue
        item_id = self.url.split('/')[-1].split('.')[0]
        self.price_url = 'https://p.3.cn/prices/mgets?skuIds=J_' + item_id
        self.name = self.root.getElementsByTagName('name')[0].childNodes[0].nodeValue
        self.first_read = self.root.getElementsByTagName('firstread')[0].childNodes[0].nodeValue
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
        self.price = 0

    def get_price(self):
        print '正在查询，请稍后...'
        price_get = self.session.get(self.price_url, headers=self.headers, allow_redirects=True)
        price_json = price_get.text
        price_json = json.loads(price_json)
        price = string.atof(price_json[0]['p'])
        print self.name, price
        self.price = price

    def modifiy_xml_firstread(self):
        self.root.getElementsByTagName('firstread')[0].childNodes[0].nodeValue = 'False'
        with open('./config.xml', 'w') as f:
            self.doc.writexml(f, addindent=' ', newl='\n', encoding='utf-8')
        f.close()
