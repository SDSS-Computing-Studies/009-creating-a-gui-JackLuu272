import tkinter as tk
from tkinter import *
from tkinter import ttk  


window = tk.Tk()
window.title("multiplication module")
window.geometry("307x25")

entryint1 = tk.Entry(window,text = "", width = 10)
multsign = tk.Label(window,text = "x")
entryint2 = tk.Entry(window,text = "", width = 10)
equalsign = tk.Button(window,text = "=" )
result = tk.Entry(window,text = "", width = 20)

entryint1.place(x=0, y=0)
multsign.place(x=70, y=0)
entryint2.place(x=90, y=0)
equalsign.place(x=157, y=0)
result.place(x=180, y=0)

window.mainloop()


