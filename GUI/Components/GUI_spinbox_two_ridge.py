import os
import tkinter as tk
from tkinter import Menu, Spinbox, scrolledtext, ttk

win = tk.Tk()
win.title("Python GUI")

# Thiết lập Icon cửa sổ an toàn
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'PYC.ico')
try:
    win.iconbitmap(icon_path)
except Exception:
    pass

# --- Menu Bar ---
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

# --- Notebook Tabs ---
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill="both")

# ==================== TAB 1 ====================
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Nhập tên
ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

# Chọn số qua Combobox
ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = tuple(range(1, 11))
number_chosen.grid(column=1, row=1, sticky='W')
number_chosen.current(0)

# Nút Click Me
action = ttk.Button(mighty, text="Click Me!")
action.grid(column=2, row=1)

# Khung ScrolledText (chuyển xuống row=3 để tránh đè lên Spinbox)
scr = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, pady=4)
# Hàm callback xử lý sự kiện khi nhấn nút mũi tên tăng/giảm trên Spinbox
def _spin():
    """
    Callback function cho Spinbox:
    - value = spin.get(): Lấy giá trị số hiện tại hiển thị trên Spinbox.
    - print(value): In giá trị ra màn hình console/terminal để debug.
    - scr.insert(tk.INSERT, ...): Chèn giá trị vừa chọn kèm ký tự xuống dòng ('\\n')
      vào vị trí con trỏ hiện tại của khung văn bản ScrolledText.
    """
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Thêm Spinbox widget (chỉnh tại row=2)
# from_=0, to=10: Dải giá trị từ 0 đến 10
# bd=8: Độ dày đường viền 3D xung quanh Spinbox
# command=_spin: Gán hàm _spin được kích hoạt mỗi khi nhấn nút mũi tên
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8,  command=_spin)
spin.grid(column=0, row=2)

spin.grid(column=0, row=2, sticky='W', pady=4)

def _spin2():
    value = spin2.get()  
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=9,  command=_spin2, relief=tk.RIDGE)

# ==================== TAB 2 ====================
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# 3 Checkbutton
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

# 3 Radiobutton
colors = ["Blue", "Gold", "Red"]
radVar = tk.IntVar()
radVar.set(99)
for col, col_name in enumerate(colors):
    curRad = tk.Radiobutton(mighty2, text=col_name, variable=radVar, value=col)
    curRad.grid(column=col, row=1, sticky=tk.W)

# Frame phụ chứa Labels
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=2, columnspan=3)
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0)

name_entered.focus()
win.mainloop()