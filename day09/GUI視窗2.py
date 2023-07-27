import tkinter

value = 0  # global 全域變數

def update():
    global value  # 宣告此 value 為 global value
    value += 1
    var.set(str(value))  # 將 value 的最新內容給 var, 因為 label 的內容會指向 var


win = tkinter.Tk()
win.geometry("100x50")

var = tkinter.StringVar()
var.set(str(value))
label = tkinter.Label(win, textvariable=var)
label.pack()

button_add = tkinter.Button(win, text="Add", command=update)
button_add.pack()

win.mainloop()





