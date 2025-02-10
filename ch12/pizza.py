path = "C:\\rokey\\ch12\\order.txt"
while True:
    num = int(input("1 : 주문 추가 , 2 : 주문 읽기 , 3 : 종료 ").strip())
    print(type(num),num)
    
    if num==1:
        print("1if")
        mode="a"
        with open(path,mode,encoding="utf-8") as f:
            order=input("피자 입력 : ")
            order +="\n"
            f.write(order)
          
    elif num==2:
        mode="r"
        with open(path,mode,encoding="utf-8") as f:
            lines=f.readlines()
            for line in lines:
                print(line)

        
    elif num==3:
        break
    else:
        print("다시 입력")