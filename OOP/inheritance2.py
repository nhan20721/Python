class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first +'-'+last+'@email.com'
        self.pay = pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_co_salary(self):
        self.pay = int (self.pay * self.co_salary)
        return self.pay

class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang = pro_lang

class Manager(Employee):
    co_salary = 1.5
    def __init__(self, first, last, pay,employees = None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('----',emp.full_name())

class Secretary(Employee):
    co_salary = 1.05
    def __init__(self, first, last, pay,job):
        super().__init__(first,last,pay)
        self.job = job

dev1 = Developer('Trần','Nhân', 200, 'Python')
dev2 = Developer('Nguyễn','Nam', 200, 'Java')
src1 = Secretary('Nguyễn','Minh', 400, 'Embedded C++')
print(dev1.full_name())
print(dev1.apply_co_salary())
man1 = Manager('Đào','Tuấn', 1000, [dev1,dev2])
man1.remove_employee(dev2)
man1.add_employee(src1)
man1.print_emp()