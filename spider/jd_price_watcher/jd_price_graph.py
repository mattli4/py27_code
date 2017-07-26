# -*- coding:UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import time


class PlotGraph:
    def __init__(self, price_dict, name):
        self.price_dict = price_dict
        self.name = name

    def gen_xy_lable(self):
        X = []
        Y = []
        x_lable = []
        price_dict = self.price_dict
        base_item = price_dict[0]
        Y.append(base_item['price'])
        cur_time = base_item['time']
        x_lable.append(cur_time.replace(' ', '\n'))
        time_array = time.strptime(cur_time, "%Y-%m-%d %H:%M:%S")
        base_time_stamp = int(time.mktime(time_array))
        X.append(0)
        del price_dict[0]
        for item in price_dict:
            Y.append(item['price'])
            cur_time = item['time']
            x_lable.append(cur_time.replace(' ', '\n'))
            time_array = time.strptime(cur_time, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_array))
            diff = time_stamp - base_time_stamp
            diff /= 10000
            X.append(diff)
        return X, x_lable, Y

    def plot_graph(self, X, x_lable, Y):
        plt.figure(figsize=(8, 4))
        plt.plot(X, Y, 'b', linewidth=1)
        plt.xticks(X, x_lable, rotation=0)
        plt.xlabel('Time(D)')
        plt.ylabel('Price(RMB)')
        plt.title(self.name + ' Price Chart')
        plt.savefig('./image/price.png')

    def gen_graph(self):
        x, x_lable, y = self.gen_xy_lable()
        print '正在绘图...'
        self.plot_graph(x, x_lable, y)
        print '绘制完成！'
