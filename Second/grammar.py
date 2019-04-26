print('Basic Grammar')
# ################# 常量与变量 #################
'''
均存在内存中，常量是不可变的变量
命名规则
常量：一般采用大写字母，单词间下划线相连，如 PI | APP_URL
变量；只能是字母、数字和下划线的组合，但不能以数字开头，不能使用python关键字作为变量名
'''

# ################# 变量命名方法 #################
'''
驼峰式写法：firstName
下划线连接式写法：first_name
'''

# ################# 数字类型 ################
print("1 + 2 = {}".format(1 + 2))  # 使用format，{}作为占位符
print("7 % 2 = {}".format(7 % 2))
print("12 // 5 = {}".format(12 // 5))

print("10 * 2 = %d" % (10 * 2))  # 使用%， %s作为占位符
print("15 / 2 = %d, 4 - 5 = %d" % (15 / 2, 4 - 5))
print("3 ** 4 = %d" % (3 ** 4))

a = 101
b = 100
print(f'{a} is bigger than {b}')  # version > 3.6
print("0.1 + 0.2 = {}".format(0.1 + 0.2))  # 结果包含的小数位数可能是不确定的

# ################# 布尔类型 ################
'''
1. True Or False,注意不是true or false
2. 0、空字符串、None 都被看作False，其他数值和非空字符串被看作True
3. 可进行正常的逻辑与或非运算 and or not 
'''