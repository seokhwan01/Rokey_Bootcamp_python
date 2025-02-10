from tkinter import Tk, Button, Radiobutton, IntVar

# Tkinter 창 생성 및 크기 설정
oroot = Tk()
oroot.geometry("200x100")  # 창 크기 설정 (너비 x 높이)

# 라디오 버튼에 들어갈 메뉴 (딕셔너리)
lunch = {0: "A런치", 1: "B런치", 2: "C런치"}

# 선택된 값을 저장할 변수 (정수형)
radio_value = IntVar()  # 선택된 라디오 버튼 값 저장
radio_value.set(1)  # 기본값으로 B런치(1) 선택

# 라디오 버튼 생성 및 배치
orb1 = Radiobutton(oroot, text=lunch[0], variable=radio_value, value=0)
orb2 = Radiobutton(oroot, text=lunch[1], variable=radio_value, value=1)
orb3 = Radiobutton(oroot, text=lunch[2], variable=radio_value, value=2)

orb1.pack()
orb2.pack()
orb3.pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

# "시작버튼" 추가
option = Button(oroot, text="주문",command=buy)
option.pack()

# Tkinter 실행 루프
oroot.mainloop()
