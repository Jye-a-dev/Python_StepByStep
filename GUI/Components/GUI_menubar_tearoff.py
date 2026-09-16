import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import Menu


win = tk.Tk()
win.title("Python GUI")

# Tạo Frame bao bọc chính
mighty = ttk.LabelFrame(win, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Chuyển parent sang mighty:
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action = ttk.Button(mighty, text="Click Me!")
action.grid(column=2, row=1)

ch1 = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=ch1, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

ch2 = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=ch2)
check2.grid(column=1, row=3, sticky=tk.W)

ch3 = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=ch3)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

colors = ["Blue", "Gold", "Red"]
radVar = tk.IntVar()
radVar.set(99)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(mighty, text=col_name, variable=radVar, value=col)
    curRad.grid(column=col, row=6, sticky=tk.W)

buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0)

# Thêm trước vòng lặp win.mainloop():
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=file_menu)


name_entered.focus()
win.mainloop()