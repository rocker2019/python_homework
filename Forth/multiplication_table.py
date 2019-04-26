# -*- coding:utf8 -*-
# 生成九九乘法表

# 初始化表格为空
table = ''

for i in range(1, 10):
    for j in range(1, 10):
        if i < j:
            continue

        table += '{} * {} = {}\t'.format(j, i, i * j)

        # 边界情况下换行
        if i == j:
            table += '\n'

print(table)
