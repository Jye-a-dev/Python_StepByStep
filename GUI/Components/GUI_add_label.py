from tkinter import ttk
import tkinter as tk

#precess process
win = tk.Tk()
ttk.Label(win, text="A Label")

#process
win.title("Test")
ttk.Label(win,text="Test Label").grid(column = 0, row = 0)

#run loop
win.mainloop()