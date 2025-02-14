class Human:
    eyes=2
    nose=1
    mouth=1
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("부모 실행")
    def introduce(self):
        print(f"이름 : {self.name} 나이 : {self.age}")
    def eat(self):
        print("먹다")
    def sleep(self):
        print("자다")
    def talk(self):
        print("말하다")
        
class Student(Human):
    def study(self):
        print("공부하다")
s1 = Student("정석환","25")
s1.introduce()
s1.study()