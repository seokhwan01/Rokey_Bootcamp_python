# class Animal():
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
# cat=Animal("고양이","야옹")
# print(cat.name,cat.sound)

class Fruits:
    def __init__(self,name,color):
        self.name = name
        self.color=color
    def taste(self):       
        print(self.name,"새콤하다")
        
obj=Fruits("오렌지","주황색")
print(obj.name,obj.color)
obj.taste()

# class Cadd:
#     def fadd(self, a, b):
#         self.x = a
#         self.y = b
#         self.hap = self.x + self.y

# obj = Cadd()  # 생성자 없이 객체 생성
# obj.fadd(10, 20)
# print("객체 obj 내의 인스턴스 변수 x의 값은", obj.x)  # 10
# print("객체 obj 내의 인스턴스 변수 y의 값은", obj.y)  # 20
# print("객체 obj 내의 인스턴스 변수 hap의 값은", obj.hap)  # 30