import os
import tkinter as tk
from tkinter import Menu, Spinbox, scrolledtext, ttk

win = tk.Tk()
win.title("Python GUI")

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'PYC.ico')
try:
    win.iconbitmap(icon_path)
except Exception:
    pass

# Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

# Notebook Tabs
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

# --- Tab 1 ---
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1, sticky='W')
number_chosen.current(0)

action = ttk.Button(mighty, text="Click Me!")
action.grid(column=2, row=1)

# Adding a Spinbox widget
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8)
spin.grid(column=0, row=2)

scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3)

# --- Tab 2 ---
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

ch1 = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=ch1, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

ch2 = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=ch2)
check2.grid(column=1, row=0, sticky=tk.W)

ch3 = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=ch3)
check3.select()
check3.grid(column=2, row=0, sticky=tk.W)

colors = ["Blue", "Gold", "Red"]
radVar = tk.IntVar()
radVar.set(99)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(mighty2, text=col_name, variable=radVar, value=col)
    curRad.grid(column=col, row=1, sticky=tk.W)

buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=2, columnspan=3)
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0)

name_entered.focus()
win.mainloop()