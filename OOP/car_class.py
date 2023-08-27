class Car:
    tax = 1
    car_number = 0
    def __init__(self,brand,model,founded_year,price):
        self.brand = brand
        self.model = model
        self.founded_year = founded_year
        self.price = price
        Car.car_number += 1
    def Brand(self):
        return self.brand
    def GetValue(self):
        return (self.price * self.tax)
    @classmethod
    def set_tax(cls):
        cls.tax = 1.5
    @classmethod
    def from_string(cls, car_string):
        brand, model, founded_year, price = car_string.split('-')
        founded_year =int(founded_year)
        price = int(price)
        return cls(brand, model, founded_year, price)
    @staticmethod
    def check_price(price):
        if price <= 1000:
            print('This car is cheap')
        else:
            print('This car is expensive')

car_temp = 'Toyota-Camry-1969-800'

print(Car.car_number)

car1 = Car('Vinfast','LuxA',2017, 1000)
car2 = Car('BMW','i320',1916,700)

car2.tax = 2

car3 = Car.from_string(car_temp)
print(car3.brand, car3.model, car3.founded_year, car3.price)

print(f'{car1.model} price {car1.GetValue()}$')
print(f'{car2.model} price {car2.GetValue()}$')

print(Car.tax,car1.tax,car2.tax)

print(car1.__dict__)
print(Car.car_number)

car1.set_tax()
print(Car.tax)
print(car1.GetValue())

car1.check_price(car1.price)
car2.check_price(car2.price)