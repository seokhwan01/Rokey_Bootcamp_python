# from tkinter import *
# oroot = Tk()
# olabel1=Label(oroot, text="레드",bg="red",fg="white",width=30,height=10)
# olabel2=Label(oroot, text="초록",bg="green",width=30,height=10)
# olabel3=Label(oroot, text="파랑",bg="blue",width=30,height=10)
# olabel1.pack()
# olabel2.pack()
# olabel3.pack()
# oroot.mainloop()
from tkinter import *
from tkinter import Tk, Button, Checkbutton, IntVar

# Tkinter 창 생성 및 크기 설정
oroot = Tk()
oroot.geometry("400x300")  # 창 크기 설정 (너비 x 높이)
oroot.title("조각 피자 주문 프로그램")
label=Label(oroot, text="피자")
label.pack()
pizza_menu = {0: ("치즈 피자",3200), 1: ("콤비네이션 피자",3500), 2: ("불고기 피자", 3600)}

# 체크박스 변수 저장 딕셔너리
check_value = {}

# 체크박스 생성 및 배치
for i in pizza_menu:
    check_value[i] = BooleanVar()  # 각 체크박스 상태를 저장할 변수
    check_btn = Checkbutton(oroot, text=f"{pizza_menu[i][0]} ({pizza_menu[i][1]})원", variable=check_value[i])
    check_btn.pack(anchor="w")  # 왼쪽 정렬
    
order_summary = StringVar()  # 주문내역을 출력할 변수
order_summary_label = Label(oroot, textvariable=order_summary, justify="left")
order_summary_label.pack()

def buy():
    total=0
    order_text = "주문내역:\n" 

    for i in check_value:
        if check_value[i].get():
            order_text += f"- {pizza_menu[i][0]} ({pizza_menu[i][1]}원)\n"
            total += pizza_menu[i][1]  # 총 금액 계산

            print(pizza_menu[i])
    order_text += f"\n총 가격: {total}원"
    order_summary.set(order_text)  # GUI에 주문내역 표시

            
option = Button(oroot, text="주문",command=buy)
option.pack()

oroot.mainloop()