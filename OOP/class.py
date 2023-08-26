#Ví dụ về tạo class đơn giản
class SimpleClass:
    #Attribute (thuộc tính)
    i=5
    #_init_
    def __init__(self):
        #Attribute of an instance of class
        self.j = 7

    #Method
    def printMe(self):
        print(self.j)

objectA = SimpleClass()
objectB = SimpleClass()

objectA.printMe()           #.printMe gọi phương thức (method) bên trong đối tượng
print(objectB.i)

#Thay đổi giá trị của thuộc tính
objectA.i = 100
objectB.j = 500
print(objectA.i)
objectB.printMe()

class SimpleClass2():
    #Constructor
    def __init__(self) -> None:
        self.name = "Nhân"
    
    #Method
    def hello(self):
        print("Hello "+self.name)
    
    #Static methods
    @staticmethod
    def hi(name):
        print("Hi "+name)

objectC = SimpleClass2()
objectD = SimpleClass2()

objectC.hello()
objectD.hi("Peter")
SimpleClass2.hi("Nam")