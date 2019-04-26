# -*- coding:utf8 -*-

# 初始化数字列表
numbers = list(range(1, 8, 2))
for index, i in enumerate(numbers):
    if index == len(numbers) - 1:
        continue
    print(i * '*')

# 翻转之后的数字列表
for j in numbers[::-1]:
    print(j * '*')
