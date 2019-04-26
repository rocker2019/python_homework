import datetime


class Restaurant:
    def __init__(self, name, category, customers):
        self.name = name
        self.category = category
        self.business_hour = 8
        self.customers = customers

    def get_restaurant_info(self):
        print('餐馆名字：{}，餐馆类型：{}'.format(self.name, self.category))

    def get_business_hour(self):
        print('餐馆营业开始时间：{}'.format(self.business_hour))
        current_hour = datetime.datetime.now().hour
        if current_hour < self.business_hour:
            print('餐馆正在休息')
        else:
            print('餐馆正在营业')

    def get_customers_count(self):
        print('餐馆用餐人数：{}'.format(self.customers))

    def set_customers_count(self, count):
        if count > self.customers:
            self.customers = count
        else:
            return

# barbecue = Restaurant('rocker烧烤店', '自助', 20)
# barbecue.get_restaurant_info()
# barbecue.get_business_hour()
# barbecue.set_customers_count(23)
# barbecue.get_customers_count()
