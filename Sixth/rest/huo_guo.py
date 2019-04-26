import restaurant


class Huoguo(restaurant.Restaurant):
    def __init__(self, name, category, customers, huo_guo_type, employee):
        super().__init__(name, category, customers)
        self.huo_guo_type = huo_guo_type
        self.employee = employee

    def get_employee_counts(self):
        print('员工人数：{}'.format(self.employee))

    def set_employee_counts(self, counts):
        self.employee += counts
