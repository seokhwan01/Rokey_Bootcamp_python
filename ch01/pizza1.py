import tkinter as tk
from tkinter import messagebox

# 피자 가격 목록 (2배로 조정)
pizza_prices = {
    "치즈 피자": 6000,
    "페퍼로니 피자": 7000,
    "고구마 피자": 8000,
    "불고기 피자": 9000,
}

# 주문 내역 저장
order_list = []
total_price = 0  # 총 주문 금액

def add_to_order():
    global total_price
    try:
        # 선택된 피자에서 이름만 추출
        selected_pizza_full = pizza_var.get()
        selected_pizza = selected_pizza_full.split(" (")[0]  # "치즈 피자 (6000원)" → "치즈 피자"
        
        quantity = int(quantity_entry.get())

        if selected_pizza == "":
            messagebox.showwarning("경고", "피자를 선택하세요!")
            return

        if quantity <= 0:
            messagebox.showwarning("경고", "1개 이상의 피자를 주문하세요!")
            return

        price_per_piece = pizza_prices[selected_pizza]
        order_price = price_per_piece * quantity
        total_price += order_price  # 총 주문 금액 업데이트

        # 주문 내역 업데이트
        order_list.append(f"{selected_pizza} x {quantity}개 = {order_price}원")
        update_order_list()

        # 입력 초기화
        quantity_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("오류", "유효한 수량을 입력하세요!")

def update_order_list():
    order_text.set("\n".join(order_list))
    total_label.config(text=f"총 주문 금액: {total_price}원")

def reset_order():
    global order_list, total_price
    order_list = []
    total_price = 0
    update_order_list()

# tkinter GUI 생성
root = tk.Tk()
root.title("피자 조각 주문 프로그램")

# 피자 선택
tk.Label(root, text="피자 종류를 선택하세요:").grid(row=0, column=0, padx=10, pady=10)
pizza_var = tk.StringVar(value="")
pizza_menu = tk.OptionMenu(root, pizza_var, *[
    f"{pizza} ({price}원)" for pizza, price in pizza_prices.items()
])
pizza_menu.grid(row=0, column=1, padx=10, pady=10)

# 피자 수량 입력
tk.Label(root, text="수량:").grid(row=1, column=0, padx=10, pady=10)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

# 추가 버튼
add_button = tk.Button(root, text="추가하기", command=add_to_order)
add_button.grid(row=2, column=0, padx=10, pady=10)

# 초기화 버튼
reset_button = tk.Button(root, text="초기화", command=reset_order)
reset_button.grid(row=2, column=1, padx=10, pady=10)

# 주문 내역 표시
tk.Label(root, text="주문 내역:").grid(row=3, column=0, padx=10, pady=10)
order_text = tk.StringVar(value="")
order_listbox = tk.Label(root, textvariable=order_text, justify="left", font=("Arial", 10), anchor="w")
order_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 총 주문 금액 표시
total_label = tk.Label(root, text="총 주문 금액: 0원", font=("Arial", 12), fg="blue")
total_label.grid(row=5, column=0, columnspan=2, pady=10)

# GUI 실행
root.mainloop()
