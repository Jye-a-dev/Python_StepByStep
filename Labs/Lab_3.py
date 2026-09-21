import os
import time
from threading import Thread
import tkinter as tk
from tkinter import Menu, Spinbox, messagebox, scrolledtext, ttk

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

def _msg_box():
    messagebox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2022.')

def _msg_warning():
    messagebox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')

def _msg_error():
    messagebox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston - we DO have a serious PROBLEM!')

def _msg_multi():
    messagebox.askyesnocancel('Python Message Multi Choice Box', 'Are you sure you really wish to do this?')

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

def _spin2():
    value = spin2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number.get())

def _run_progressbar():
    progress_bar['maximum'] = 100
    for i in range(101):
        time.sleep(0.03)
        progress_bar['value'] = i
    progress_bar['value'] = 0

def run_progressbar():
    Thread(target=_run_progressbar, daemon=True).start()

def start_progressbar():
    progress_bar.start()

def stop_progressbar():
    progress_bar.stop()

def stop_after_second():
    win.after(1000, progress_bar.stop)

def draw_canvas(event=None):
    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    canvas.create_rectangle(0, 0, w/2, h/2, fill="orange", outline="")
    canvas.create_rectangle(w/2, 0, w, h/2, fill="blue", outline="")
    canvas.create_rectangle(0, h/2, w/2, h, fill="blue", outline="")
    canvas.create_rectangle(w/2, h/2, w, h, fill="orange", outline="")

win = tk.Tk()
win.title("Python GUI")

current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'PYC.ico')
try:
    win.iconbitmap(icon_path)
except Exception:
    pass

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msg_box)
menu_bar.add_cascade(label="Help", menu=help_menu)

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')
tabControl.pack(expand=1, fill="both")

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

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2, sticky='W', pady=4)
ToolTip(spin, 'This is a Spinbox widget')

spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=9, command=_spin2, relief=tk.RAISED)
spin2.grid(column=1, row=2, sticky='W', pady=4)
ToolTip(spin2, 'This is a second Spinbox widget')

scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, pady=4)
ToolTip(scr, 'This is a ScrolledText widget')

mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4, sticky='W')

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

prog_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
prog_frame.grid(column=0, row=2, columnspan=3, padx=8, pady=4, sticky='WE')

btn_run = ttk.Button(prog_frame, text="Run Progressbar", command=run_progressbar)
btn_run.grid(column=0, row=0, padx=4, pady=2, sticky='W')

btn_start = ttk.Button(prog_frame, text="Start Progressbar", command=start_progressbar)
btn_start.grid(column=0, row=1, padx=4, pady=2, sticky='W')

btn_stop = ttk.Button(prog_frame, text="Stop immediately", command=stop_progressbar)
btn_stop.grid(column=0, row=2, padx=4, pady=2, sticky='W')

btn_stop_after = ttk.Button(prog_frame, text="Stop after second", command=stop_after_second)
btn_stop_after.grid(column=0, row=3, padx=4, pady=2, sticky='W')

progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=280, mode='determinate')
progress_bar.grid(column=0, row=1, padx=8, pady=8, sticky='WE')

canvas = tk.Canvas(tab3, width=320, height=200, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", draw_canvas)

name_entered.focus()
win.mainloop()