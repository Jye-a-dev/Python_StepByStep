from tkinter import ttk
import tkinter as tk

win = tk.Tk()
ttk.Label(win, text="A Label")

#process
win.title("Test")
ttk.Label(win,text="Test Label").grid(column = 0, row = 0)
a_label = ttk.Label(win, text="Testing")
a_label.grid(column=0, row = 0)

ttk.Label(win,text="Nhập vào tên em: ").grid(column=0,row=0)

#Process function
def click_me():
    action.configure(text="** I have been Clicked! **")  
    a_label.configure (foreground='red')  
    a_label.configure(text='A Red Label')
    action.configure(text="Hello " + name.get())


#run loop
action = ttk.Button(win,text="test", command=click_me)
action.grid(column=1, row = 0)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row = 1) 

win.mainloop()
