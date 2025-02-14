# def func_add(a,b):
#     return a+b
# print(func_add(1,2))

# def func_nadd(n):
#     total=0
#     for i in range(1,n+1):
#         total+=i
#     print(total)
# func_nadd(10)
# x=5

# def ex():
#     global x
#     x=15
#     print(x)
# ex()
# print(x)

# arr=[1,2,3]
# max=arr[0]
# for i in arr:
#     if max<i:
#         max=i
# print(max)
# import math
# print(math.factorial(5))
class Animal:
    def speak(self):
        return "Animal sepeaks"
class Dog(Animal):
    def speak(self):
        return "Woof"
dog=Dog()
print(dog.speak())