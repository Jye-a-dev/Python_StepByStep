import tkinter as tk
from tkinter import ttk, scrolledtext

win = tk.Tk()
win.title("Python GUI")

# --- Widgets từ Chapter 1 ---
ttk.Label(win, text="Enter a name:").grid(column=0, row=0, sticky=tk.W)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0, sticky=tk.W)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1, sticky=tk.W)
number_chosen.current(0)

action = ttk.Button(win, text="Click Me!")
action.grid(column=2, row=1)

ch1 = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=ch1, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

ch2 = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=ch2)
check2.grid(column=1, row=3, sticky=tk.W)

ch3 = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=ch3)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

scrol_w, scrol_h = 30, 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

colors = ["Blue", "Gold", "Red"]
radVar = tk.IntVar()
radVar.set(99)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(win, text=col_name, variable=radVar, value=col)
    curRad.grid(column=col, row=6, sticky=tk.W)

# --- Thêm LabelFrame và 3 Labels theo hàng ngang ---
buttons_frame = ttk.LabelFrame(win, text='')
buttons_frame.grid(column=0, row=7, padx=20, pady=40)

ttk.Label(buttons_frame, text="Label1 -- sooooo much loooonger...").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)
# Đặt ngay dưới các câu lệnh tạo 3 Label:
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)
name_entered.focus()
win.mainloop()