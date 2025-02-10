from collections import deque

def insert():
    n=int(input("1:오른쪽 삽입 ,2:왼쪽 삽입 "))
    i=int(input("삽입할 값 : "))
    if n==1:
        dq.append(i)
    elif n==2:
        dq.appendleft(i)
        
def delete():
    n=int(input("1:오른쪽 삭제 ,2:왼쪽 삭제 "))
    if n==1:
        dq.pop()
    elif n==2:
        dq.popleft()
        
def circular():
    n=int(input("1:오른쪽 회전 ,2:왼쪽 회전 "))
    i=int(input("회전 수 : "))
    if n==1:
        for j in range(i):
            dq.appendleft(dq.pop())
            print(dq)
    elif n==2:
        for j in range(i):
            dq.append(dq.popleft())
            print(dq)

dq=deque()
while True:
    num=int(input("1:삽입 , 2:삭제, 3:회전 ,0:종료 "))
    if num==0:
        break
    elif num==1:
        insert()
    elif num==2:
        delete()
    elif num==3:
        circular()
    else:
        print("잘못된 입력")
    print(dq)
    