from tkinter import ttk
import tkinter as tk

win = tk.Tk()
ttk.Label(win, text="A Label")

#process
win.title("Test")
ttk.Label(win,text="Test Label").grid(column = 0, row = 0)
a_label = ttk.Label(win, text="Testing")
a_label.grid(column=0, row = 0)

#Process function
def click_me():
    action.configure(text="** I have been Clicked! **")  
    a_label.configure (foreground='red')  
    a_label.configure(text='A Red Label')

#run loop
action = ttk.Button(win,text="test", command=click_me)
action.grid(column=1, row = 0)
win.mainloop()
