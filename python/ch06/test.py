# def fdiv(num1,num2):
#     if num2==0:
#         print("0으로는 나눌 수 없습니다")
#     else:
#         print(num1/num2)
# if __name__ =="__main__":
#     a,b = map(int,input("a,b 입력 : ").split())
#     fdiv(a,b)
# def sum_of_multiples(num):
#     total = 0
#     for i in range (101):
#         if i%num==0:#배수이면
#             total+=i
#     return total

# if __name__ =="__main__":
#     n=int(input("(1~9)사이 정수 입력 : "))
#     result = sum_of_multiples(n)
#     print(result)
def str_len(sta):
    count=0
    for i in sta:
        count+=1
    return count
sta="ptyhon example"
#print(len(sta))
print(str_len(sta))