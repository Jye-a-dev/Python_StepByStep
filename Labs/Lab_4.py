import os
import time
from threading import Thread
import tkinter as tk
from tkinter import Menu, Spinbox, messagebox, scrolledtext, ttk

win_test = tk.Tk()
win_test.withdraw()
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)
print(type(doubleData))
add_doubles = 1.222222222222222222222222 + doubleData.get()
print(add_doubles)
print(type(add_doubles))
strData = tk.StringVar()
strData.set('Hello StringVar')
varData = strData.get()
print(varData)
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())
intData = tk.IntVar()
print(intData)
print(intData.get())
win_test.destroy()

GLOBAL_CONST = 42
print(GLOBAL_CONST)

def usingGlobal():
    global GLOBAL_CONST
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777
    print(GLOBAL_CONST)

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

class OOP:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self._init_icon()
        self._create_menu()
        self._create_widgets()

    def _init_icon(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, 'PYC.ico')
        try:
            self.win.iconbitmap(icon_path)
        except Exception:
            pass

    def _create_menu(self):
        self.menu_bar = Menu(self.win)
        self.win.config(menu=self.menu_bar)

        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.win.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msg_box)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

    def _msg_box(self):
        messagebox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2022.')

    def _spin(self):
        value = self.spin.get()
        print("Spinbox value: " + value)
        self.scr.insert(tk.INSERT, value + '\n')

    def _spin2(self):
        value = self.spin2.get()
        print("Spinbox value: " + value)
        self.scr.insert(tk.INSERT, value + '\n')

    def _click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number.get())

    def _run_progressbar(self):
        self.progress_bar['maximum'] = 100
        for i in range(101):
            time.sleep(0.03)
            self.progress_bar['value'] = i
            self.progress_bar.update()
        self.progress_bar['value'] = 0

    def run_progressbar(self):
        Thread(target=self._run_progressbar, daemon=True).start()

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def stop_after_second(self):
        self.win.after(1000, self.progress_bar.stop)

    def _create_widgets(self):
        tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text='Tab 1')
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text='Tab 2')
        tabControl.pack(expand=1, fill="both")

        ToolTip(self.tab1, 'Hello GUI')
        ToolTip(self.tab2, 'Hello GUI')

        mighty = ttk.LabelFrame(self.tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=12, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')

        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, sticky='W')
        self.number = tk.StringVar()
        number_chosen = ttk.Combobox(mighty, width=12, textvariable=self.number, state='readonly')
        number_chosen['values'] = tuple(range(1, 11))
        number_chosen.grid(column=1, row=1, sticky='W')
        number_chosen.current(0)

        self.action = ttk.Button(mighty, text="Click Me!", command=self._click_me)
        self.action.grid(column=2, row=1)

        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2, sticky='W', pady=4)
        ToolTip(self.spin, 'This is a Spinbox control')

        self.spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=9, command=self._spin2, relief=tk.RAISED)
        self.spin2.grid(column=1, row=2, sticky='W', pady=4)
        ToolTip(self.spin2, 'This is a second Spinbox widget')

        self.scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, columnspan=3, pady=4)
        ToolTip(self.scr, 'This is a ScrolledText widget')

        mighty2 = ttk.LabelFrame(self.tab2, text=' The Snake ')
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
            ToolTip(curRad, 'This is a Radiobutton control')

        prog_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
        prog_frame.grid(column=0, row=2, columnspan=3, padx=8, pady=4, sticky='WE')

        btn_run = ttk.Button(prog_frame, text="Run Progressbar", command=self.run_progressbar)
        btn_run.grid(column=0, row=0, padx=4, pady=2, sticky='W')

        btn_start = ttk.Button(prog_frame, text="Start Progressbar", command=self.start_progressbar)
        btn_start.grid(column=0, row=1, padx=4, pady=2, sticky='W')

        btn_stop = ttk.Button(prog_frame, text="Stop immediately", command=self.stop_progressbar)
        btn_stop.grid(column=0, row=2, padx=4, pady=2, sticky='W')

        btn_stop_after = ttk.Button(prog_frame, text="Stop after second", command=self.stop_after_second)
        btn_stop_after.grid(column=0, row=3, padx=4, pady=2, sticky='W')

        self.progress_bar = ttk.Progressbar(self.tab2, orient='horizontal', length=280, mode='determinate')
        self.progress_bar.grid(column=0, row=1, padx=8, pady=8, sticky='WE')

        self.name_entered.focus()

oop = OOP()
oop._spin()
usingGlobal()
print('GLOBAL_CONST: ', GLOBAL_CONST)
oop.win.mainloop()