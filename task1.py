import tkinter as tk
from tkinter import *
from tkinter import ttk  


window = tk.Tk()
window.title("multiplication module")

entryint1 = tk.Entry(window,text = "", width = 10)
multsign = tk.Label(window,text = "x")
entryint2 = tk.Entry(window,text = "", width = 10)
equalsign = tk.Button(window,text = "=" )
result = tk.Entry(window,text = "", width = 20)

entryint1.grid(row=1, column = 1)
multsign.grid(row=1, column = 2)
entryint2.grid(row=1, column = 3)
equalsign.grid(row=1, column = 4)
result.grid(row=1, column = 5)

window.mainloop()


