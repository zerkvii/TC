# -*- coding:utf-8 -*-
import re as re

start_day = 1
start_week = 3

with open('train.txt', 'rb') as f:
    for line in f:
        # print(line.decode('UTF-8').split()[0])
        date = line.decode('UTF-8').split()[0]  # 记录天数
        day_of_week = line.decode('UTF-8').split()[1]  # 记录星期
        brand = line.decode('UTF-8').split()[2]  # 记录品牌
        count = line.decode('UTF-8').split()[3]  # 记录总量
f.close()
