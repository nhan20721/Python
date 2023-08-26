#Bài tập về động vật
#Xây dựng class cha
class Animal:
    #Constructor: Xây dựng ra đối tượng
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA):
        self.animal = animalTypeA
        self.name = nameA
        self.width = widthA
        self.weight = weightA
        self.height = heightA

    #Phát ra âm thanh
    def makeVoice(self):
        print("Unknow voice")

    #In thông tin
    def printMe(self):
        print("Animal type: {0}, name: {1}, width = {2}, height = {3}, weight = {4}".format(self.animal, self.name, self.width, self.weight, self.height))

#Xây dựng class con
class Dog(Animal):
    #Constructor của lớp con
    def __init__(self, nameA, widthA, heightA, weightA, isChampionA ) -> None:
        #Gọi constructor của lớp cha
        Animal.__init__(self, "Dog", nameA, widthA, heightA, weightA)
        #Gán giá trị cho thuộc tính bổ sung
        self.isChampion =isChampionA

    #Override method
    def makeVoice(self):
        print("{0}: gâu gâu".format(self.name))

    def takeCareTheHouse(self):
        print("{0}: zzzzzzz".format(self.name))

class Cat(Animal):
    #Constructor của lớp con
    def __init__(self, nameA, widthA, heightA, weightA, colorA ) -> None:
        #Gọi constructor của lớp cha
        Animal.__init__(self, "Cat", nameA, widthA, heightA, weightA)
        #Gán giá trị cho thuộc tính bổ sung
        self.color =colorA

    #Override method
    def makeVoice(self):
        print("{0}: meo meo".format(self.name))
    
    def catchTheMouse(self):
        print("{0}: catch a bitch".format(self.name))


dog1 = Dog("An", "100cm", "50cm", "40kg",False)
dog1.makeVoice()
dog1.printMe()
dog1.takeCareTheHouse()

cat1 = Cat("Nam","20cm", "10cm", "10kg", "Black")
cat1.makeVoice()
cat1.printMe()
cat1.catchTheMouse()

a1 = Animal("Con người", "Trần Ngọc Nhân","", "170cm", "90kg")
a1.makeVoice()
a1.printMe()
