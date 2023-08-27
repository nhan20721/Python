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
    def __repr__(self):
        return f'Employee({self.first},{self.last},{self.pay})'
    def __str__(self):
        return  f'{self.full_name()} - {self.email}'
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.full_name())
emp1 = Employee('Trần', 'Nhân', 200)
emp2 = Employee('Nguyễn', 'Nam', 100)
print(emp1)
print(str(emp1))
print(repr(emp1))
print(emp1 + emp2)
print(len(emp1))

import datetime

today = datetime.datetime.now()
#Prints readable format for date-time object
print(str(today))
#Prints the official format for date-time object
print(repr(today))