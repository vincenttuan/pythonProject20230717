import tkinter

win = tkinter.Tk()

win.title("我的 GUI 視窗")

label = tkinter.Label(win, text="Hello", bg='red', fg='yellow', font=('Arial, 18'), width=30, height=3)
label.pack(padx=10, pady=10)

button_ok = tkinter.Button(win, text="OK")
button_ok.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

button_cancel = tkinter.Button(win, text="Cancel")
button_cancel.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

win.mainloop()
