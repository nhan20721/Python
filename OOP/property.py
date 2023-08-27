class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    @property
    def full_name(self):
        return f'{self.brand} {self.model}'
    @full_name.setter
    def full_name(self, fullName):
        brand, model = fullName.split(" ")
        self.brand = brand
        self.model = model
    @full_name.deleter
    def full_name(self):
        self.brand = None
        self.model = None
        print('Deleted')
car1 = Car('Vinfast', 'LuxA 2.0')
print(car1.full_name)
car1.full_name = 'BMW i8'
print(car1.brand)
print(car1.model)
del car1.full_name
print(car1.full_name)