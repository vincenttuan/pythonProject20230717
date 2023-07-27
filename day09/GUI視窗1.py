import tkinter

win = tkinter.Tk()

label = tkinter.Label(win, text="Hello")
label.pack()

button_ok = tkinter.Button(win, text="OK")
button_ok.pack(side=tkinter.LEFT)

button_cancel = tkinter.Button(win, text="Cancel")
button_cancel.pack(side=tkinter.RIGHT)

win.mainloop()
