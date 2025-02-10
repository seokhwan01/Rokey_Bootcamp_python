# list1 = [1, 2, 3]
# list2 = ["a", "b", "c"]

# zipped = zip(list1, list2)
# print(list(zipped))  # ✅ 리스트로 변환하여 출력

# arr1=[1,2,3]
# arr2=[4,5,6,7]
# sum_list=[a+b for a,b in zip(arr1,arr2)]
# print(sum_list)
# n=int(input())
# # for i in range(n):
# #     for j in range(i+1):
# #         print("*",end="")
# #     print("\n")
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print("\n")

# n=6
# for i in range(n,0,-1):
#     print("*"*i)
# n=4
# for i in range(4):
#     print(" "*(n-i-1) +"*"*(2*i+1))
# for i in range(n-2,-1,-1):
#     print(" "*(n-i-1) +"*"*(2*i+1))
# num=int(input())
# flag=True
# if num==1:
#     print("소수 아님")
#     flag=False
# else:
#     for i in range(2,num//2):
#         if num%i==0:
#             flag=False
#             break
# if flag==True:
#     print("소수")
# else:
#     print("소수 아님")

import random
word_list = [
"Apple",
"Elephant",
"Apple",
"Buffalo",
"Capture",
"Lantern",
"Mystery",
"Pirate",
"Volcano",
"Diamond",
"Theater",
"Journey",
"Galaxy",
"Octopus",
"Tremble",
"Blanket",
"Serpent",
"Network",
"Phoenix",
"Foreman",
"Pyramid",
"Sunrise",
"Fortress",
]
chance=10
hidden=random.choice(word_list).lower()

print(hidden)

hidden_list=list("*"*len(hidden))
check_list=[0]*len(hidden)
print(f"check_list = {check_list}")
count = 0
while chance>0:
    print(1)
    input_char = input("입력하세요 : ")
    flag=0
    for i in range(len(check_list)):
        if check_list[i]==0 and hidden[i]==input_char:

            print("맞았습니다")
            hidden_list[i]=input_char
            check_list[i]=1
            flag=1
            count+=1
            break
    if flag==0:
        print("틀렸습니다")
        
    for i in hidden_list:
        print(i,end="")
    print("\n")
    chance-=1

    if count==len(hidden):
        break