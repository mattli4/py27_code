# -*- coding:UTF-8 -*-
import sqlite3


class PriceDatabase:
    def __init__(self, watcher):
        self.watcher = watcher
        self.conn = sqlite3.connect('./db/' + self.watcher.name + '.db')

    def create_table(self):
        self.conn.execute('CREATE TABLE tbl_price('
                          'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'name VARCHAR(20), '
                          'price REAL, '
                          'time TIMESTAMP);')
        print '成功创建数据表！'

    def insert(self):
        params = (self.watcher.name, self.watcher.price)
        self.conn.execute('INSERT INTO tbl_price (name, price, time) '
                          'VALUES (?, ?, Datetime());', params)
        self.conn.commit()
        print '成功添加新条目！'

    def query(self):
        data_list = []
        data = self.conn.execute('SELECT name, price, time FROM tbl_price')
        for row in data:
            price_item = {'name': row[0], 'price': row[1], 'time': row[2]}
            data_list.append(price_item)
        print '查询成功！'
        return data_list

    def close_conn(self):
        self.conn.close()