import tkinter as tk

def show_selection():
    print(f"Selected option: {selected_option.get()}")

root = tk.Tk()

options_list = ['Option 1', 'Option 2', 'Option 3']
selected_option = tk.StringVar()
selected_option.set(options_list[0])

option_menu = tk.OptionMenu(root, selected_option, *options_list)
option_menu.pack()

# 선택한 옵션을 출력하는 버튼 추가
button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack()

root.mainloop()
