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

class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        self.tip_window = None
        self.widget.bind('<Enter>', self.mouse_enter)
        self.widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_window or not self.tip_text:
            return
        x_left = self.widget.winfo_rootx() + 20
        y_top = self.widget.winfo_rooty() - 18
        self.tip_window = tk.Toplevel(self.widget)
        self.tip_window.overrideredirect(True)
        self.tip_window.geometry("+%d+%d" % (x_left, y_top))
        label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

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

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

def _spin2():
    value = spin2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2, sticky='W', pady=4)
ToolTip(spin, 'This is a Spin control')

spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=9, command=_spin2, relief=tk.RIDGE)
spin2.grid(column=1, row=2, sticky='W', pady=4)
ToolTip(spin2, 'This is a 2nd Spin control')

scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, pady=4)

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