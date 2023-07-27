import tkinter as tk

# 創建一個新視窗並設定標題
window = tk.Tk()
window.title('BMI 計算器')

# 配置相關視覺化元件, 並利用 grid 進行元件布局
# 建立標籤與輸入框
# sticky 填充對齊: e(東/右方), s(南/下方), w(西/左方), n(北/上方)
# ew: 水平對齊, ns: 垂直對齊, nsew: 四方對齊
height_label = tk.Label(window, text="身高(公分)")
height_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)
height_entry = tk.Entry(window)  # 輸入框
height_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

weight_label = tk.Label(window, text="體重(kg)")
weight_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
weight_entry = tk.Entry(window)  # 輸入框
weight_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

submit_button = tk.Button(window, text="計算 BMI")
submit_button.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

result_label = tk.Label(window, text='結果顯示會在這裡')
result_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=5)



# 開始主循環
window.mainloop()
