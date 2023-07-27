import tkinter as tk
from tkinter import ttk

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

weight_label = tk.Label(window, text="體重(公斤)")
weight_label.grid(row=1, column=0, sticky='w', padx=5, pady=5)
weight_entry = tk.Entry(window)  # 輸入框
weight_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

submit_button = tk.Button(window, text="計算 BMI")
submit_button.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

result_label = tk.Label(window, text='結果顯示會在這裡')
result_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

# 創建一個 treeview 來顯示計算結果的歷史紀錄
history_treeview = ttk.Treeview(window, columns=('序號', '身高', '體重', 'BMI'), show='headings')
# 定義每一個欄位與標題
history_treeview.column('序號', width=50)
history_treeview.column('身高', width=100)
history_treeview.column('體重', width=100)
history_treeview.column('BMI', width=100)
history_treeview.heading('序號', text='序號')
history_treeview.heading('身高', text='身高')
history_treeview.heading('體重', text='體重')
history_treeview.heading('BMI', text='BMI')
# 利用 gird 布局 history_treeview
history_treeview.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

# 開始主循環
window.mainloop()
