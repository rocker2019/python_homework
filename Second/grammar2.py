# -*- coding:utf8 -*-

# ################# 字符串类型 ################
print("Hello, World!")
print('hello, world!')  # 推荐单引号
salas = 'I\'m rocker.\nThis is the second day\'s homework'
print(salas)
print('我参加的是python实战圈，希望圈子越来越好'.format())

# 字符串运算
motto = ' Where there is a will, There is a way '
print('title:', motto.title())
print('capitalize:', motto.capitalize())
print('lower:', motto.lower())
print('upper:', motto.upper())
print('swap case:', motto.swapcase())
print('isalnum:', motto.isalnum())
print('is digit:', motto.isdigit())

# 字符串分隔
print(motto.split())  # 空格分隔
print(motto.split('is'))
print(salas.splitlines())

# 字符串删除两边空白
print(motto.strip())
print(motto.rstrip())
print(motto.lstrip())

# 字符串中并不允许修改值，只允许覆盖值

# 字符串切片 [start:end:step]
print(motto[6:])
print(motto[:6])
print(motto[::5])
print(motto[::-1])
