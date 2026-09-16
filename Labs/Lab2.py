import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
#2474802010195 - Nguyễn Việt Duy Khoa
colors = ["Blue", "Gold", "Red"]
#function
def click_me():
    action.configure(text="** I have been Clicked! **")  
    action.configure(text="Hello " + name.get())

def _quit():
    win.quit()
    win.destroy()
    exit()

def _msgBox():
    messagebox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2026.')

def radCall():
    radSel = radVar.get()
    if radSel == 0:
        style.configure("Color.TLabelframe.Label", foreground="blue")
    elif radSel == 1:
        style.configure("Color.TLabelframe.Label", foreground="gold")
    elif radSel == 2:
        style.configure("Color.TLabelframe.Label", foreground="red")

win = tk.Tk()
win.title("Python GUI")

menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)
menu_bar.add_cascade(label="Help", menu=help_menu)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

style = ttk.Style()
style.configure("Color.TLabelframe.Label", foreground="blue")

#0
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ', style="Color.TLabelframe")
mighty.grid(column=0, row=0, padx=8, pady=4)

#1
ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')
name_entered.focus()

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

#4
chVardis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVardis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#5
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

#6
radVar = tk.IntVar()
radVar.set(99)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(mighty, text=col_name, variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)
    
#7
buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a Frame ', style="Color.TLabelframe")
buttons_frame.grid(column=0, row=7, columnspan=3, padx=10, pady=5, sticky=tk.W)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2, sticky=tk.W)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=2)

mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

chVarUn2 = tk.IntVar()
check2_tab2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn2)
check2_tab2.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

chVarEn2 = tk.IntVar()
check3_tab2 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn2)
check3_tab2.select()
check3_tab2.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

win.mainloop()