import tkinter
from tkinter import messagebox

def button_ok_click():  # 按下 button_ok 要做的事情
    messagebox.showinfo("Message", "Hello Python")

def button_cancel_click():  # 按下 button_cancel 要做的事情
    win.quit()

win = tkinter.Tk()

win.title("我的 GUI 視窗")

label = tkinter.Label(win, text="Hello", bg='red', fg='yellow', font=('Arial, 18'), width=30, height=3)
label.pack(padx=10, pady=10)

button_ok = tkinter.Button(win, text="OK", command=button_ok_click)
button_ok.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

button_cancel = tkinter.Button(win, text="Cancel", command=button_cancel_click)
button_cancel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

win.mainloop()
