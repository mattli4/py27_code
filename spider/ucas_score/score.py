# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup


class Score:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_page = 'http://sep.ucas.ac.cn'
        self.login_url = self.login_page + '/slogin'
        self.course_system = self.login_page + '/portal/site/226/821'
        self.course_base = 'http://jwxk.ucas.ac.cn'
        self.course_identify = self.course_base + '/login?Identity='
        self.score_page_all = self.course_base + '/score/yjs/all'  #all
        self.score_page_autumn = self.course_base + '/score/yjs/49344'
        self.score_page_spring = self.course_base + '/score/yjs/49345'
        self.score_page_summer = self.course_base + '/score/yjs/49346'
        self.headers = {
            'Host': 'sep.ucas.ac.cn',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/47.0.2526.80 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        self.session = requests.Session()

    def login(self):
        formdata = {'userName': self.username, 'pwd': self.password, 'sb': 'sb'}
        print 'loging in...'
        post_response = self.session.post(self.login_url, data=formdata, headers=self.headers)
        if post_response.status_code == 200:
            print 'login success.'

    def query(self):
        while True:
            try:
                choose = input('please choose term:\n1. all\t2. autumn\t3. spring\t 4. summer\n')
                if choose == 1:
                    score2query = self.score_page_all
                    break
                elif choose == 2:
                    score2query = self.score_page_autumn
                    break
                elif choose == 3:
                    score2query = self.score_page_spring
                    break
                elif choose == 4:
                    score2query = self.score_page_summer
                    break
            except Exception as e:
                print 'input invalid.'
                continue
        print 'querying now...'
        get_response = self.session.get(self.course_system, headers=self.headers)
        soup = BeautifulSoup(get_response.text, 'html.parser')
        try:
            identity = str(soup).split('Identity=')[1].split('"'[0])[0]
            course_page = self.course_identify + identity
            reponse = self.session.get(course_page)
            score_response = self.session.get(score2query)
            print 'querying ok. showing result...'
            score_soup = BeautifulSoup(score_response.text, 'html.parser')
            score_table = score_soup.find_all('table')[1]
            score_body = score_table.tbody
            subject = score_body.find_all('tr')
            if subject is not []:
                print '*' * 35
                for item in subject:
                    all = item.find_all('td')
                    name = all[0].string
                    score = all[2].string
                    print name, score
                print '*' * 35
            else:
                print 'no score.'
            print 'end.'
        except Exception as e:
            print e.message

    def query_score(self):
        self.login()
        self.query()

if __name__ == '__main__':
    score = Score('xixixi', 'hahaha')
    score.query_score()
