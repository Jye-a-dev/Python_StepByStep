import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"
colors = ["Pink", "Black", "Green"]

# Process functions
def click_me():
    action.configure(text="** I have been Clicked! **")  
    a_label.configure(foreground='red')  
    a_label.configure(text='A Red Label')
    action.configure(text="Hello " + name.get())

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)
    elif radSel == 4:
        win.configure(background=colors[0])
    elif radSel == 5:
        win.configure(background=colors[1])
    elif radSel == 6:
        win.configure(background=colors[2])

# Window initialization
win = tk.Tk()
win.title("Test")

# Row 0: Labels & Action Button
ttk.Label(win, text="Nhập vào tên: ").grid(column=0, row=0, sticky=tk.W)
ttk.Label(win, text="Choose a number: ").grid(column=1, row=0, sticky=tk.W)

action = ttk.Button(win, text="test", command=click_me)
action.grid(column=2, row=1)

# Row 1: Entry & Combobox
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)
name_entered.focus()

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1, sticky=tk.W)
number_chosen.current(0)

# Row 2: Status Label
a_label = ttk.Label(win, text="Testing")
a_label.grid(column=0, row=2, sticky=tk.W)

# Row 3: Checkbuttons
chVardis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVardis, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="unChecked", variable=chVarUn)
check2.grid(column=1, row=3, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=3, sticky=tk.W)

# Row 4: Static Radiobuttons (1-3)
radVar = tk.IntVar()
radVar.set(99)

rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=4, sticky=tk.W)

rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=4, sticky=tk.W)

rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=4, sticky=tk.W)

# Row 5: Dynamic Radiobuttons (4-6)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(win, text=col_name, variable=radVar, value=col + 4, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Row 6: ScrolledText Area
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=6, columnspan=3, pady=5)

# Run loop
win.mainloop()