# import random
# arr=[0,1,2]
# print(random.choice(NotADirectoryError))
class Car:
    def __init__(self,wheel,price):
        self.wheel=wheel
        self.price=price
car=Car(4,3200)
#print(car.wheel)
#print(car.price)

class Bicycle(Car):
    def __init__(self, year, wheel, price,name):
        super().__init__(wheel, price)  # 부모(Car) 클래스의 __init__() 호출
        self.year = year  # 자식(Bicycle) 클래스의 새로운 속성 추가
        self.name=name
    def sound(self):
        print("따르릉~")
    def drivetrain(self):
        print(self.name)
    def info(self):
        print(f"year : {self.year} \nwheel : {self.wheel} \nprice : {self.price}")
        self.drivetrain()
bicycle=Bicycle(2025,2,10,"시마노")
#bicycle.drivetrain()
bicycle.info()
# print(bicycle.wheel)
# print(bicycle.price)
# print(bicycle.year)
# bicycle.sound()
#print(__name__)