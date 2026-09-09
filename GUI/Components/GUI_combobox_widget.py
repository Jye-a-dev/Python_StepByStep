import tkinter as tk
from tkinter import ttk

# Process function
def click_me():
    action.configure(text="** I have been Clicked! **")  
    a_label.configure(foreground='red')  
    a_label.configure(text='A Red Label')
    action.configure(text="Hello " + name.get())

# Window initialization
win = tk.Tk()
win.title("Test")

# Widgets
ttk.Label(win, text="A Label")
ttk.Label(win, text="Test Label").grid(column=0, row=0)

a_label = ttk.Label(win, text="Testing")
a_label.grid(column=0, row=0)

ttk.Label(win, text="Nhập vào tên: ").grid(column=0, row=0)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

action = ttk.Button(win, text="test", command=click_me)
action.grid(column=1, row=0)
action.configure(state='disabled')

ttk.Label(win, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
number_chosen.grid(column=1, row = 1)
number_chosen.current(0)
# Run loop
win.mainloop()