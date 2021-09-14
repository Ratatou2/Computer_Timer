from tkinter import *
import tkinter as tk
import os


def set_time():
    # print(tk.Entry.get(entry))  # 입력창에 들어있는 값을 출력해줍니다.
    # print(type(int(tk.Entry.get(entry))))
    sec = int(tk.Entry.get(entry))
    minute = sec * 60
    os.system(f'shutdown -s -t {minute}')
    # os.system('shutdown -s -t 3600')


def cancel_time():
    os.system('shutdown -a')

window = Tk()
window.title("Computer Timer")

# 설명 창
lb_hi = Label(window, text="< 시간(분)을 설정하십시오 >")
lb_hi.place(x=60, y=10)

# 입력창
entry = tk.Entry(fg="gray19", bg="snow", width=20)
entry.place(x=70, y=34)

# 버튼 2개 위치
# load_bt = tk.Button(window, text='설정', width=10)
# load_bt.place(x=50, y=60)
# save_bt = tk.Button(window, text='취소', width=10)
# save_bt.place(x=150, y=60)

bt_set = Button(window, text='설정', width=5, command=set_time)
bt_set.place(x=90, y=62)
# bt_set.bind('<Return>', set_time)

bt_cancel = Button(window, text='초기화', width=5, command=cancel_time)
bt_cancel.place(x=140, y=62)

window.geometry('280x100')
window.mainloop()