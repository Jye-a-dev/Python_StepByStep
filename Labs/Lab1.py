import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
#2474802010195 - Nguyễn Việt Duy Khoa
colors = ["Blue", "Gold", "Red"]

def click_me():
    action.configure(text="Hello " + name.get() + " " + number.get())

def radCall():
    radSel = radVar.get()
    win.configure(background=colors[radSel])

win = tk.Tk()
win.title("Python GUI")
win.resizable(False, False)

ttk.Label(win, text="Enter a name:").grid(column=0, row=0, sticky=tk.W)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)
name_entered.focus()

ttk.Label(win, text="Choose a number:").grid(column=1, row=0, sticky=tk.W)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1, sticky=tk.W)
number_chosen.current(0)

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

chVardis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVardis, state='disabled')
check1.select()
check1.grid(column=0, row=2, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.grid(column=1, row=2, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=2, sticky=tk.W)

radVar = tk.IntVar()
radVar.set(99)

for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(win, text=col_name, variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=3, sticky=tk.W)

scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=4, columnspan=3, pady=5)

win.mainloop()