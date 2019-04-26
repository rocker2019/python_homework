import Sixth.rest.huo_guo as huo_guo

name = ['精品火锅', '火锅', 20, '四川', 6]

obj = huo_guo.Huoguo(*name)

# 打印餐馆信息
obj.get_restaurant_info()

# 获取开业时间并判断当前是否营业
obj.get_business_hour()

# 用餐人数变化
obj.set_customers_count(18)
obj.get_customers_count()
obj.set_customers_count(25)
obj.get_customers_count()

# 三人入职 两人离职
obj.set_employee_counts(3)
obj.set_employee_counts(-2)
obj.get_employee_counts()
