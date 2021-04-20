import tkinter as tk
from tkinter import *
from tkinter import ttk  

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

doggy = PhotoImage(file="dog.png")
goodboi = tk.Label(window, image=doggy)

searcher = tk.Button(window, text = "Search by Name")
inserter = tk.Entry(window, text = "")

opener = tk.Label(window, text = "Client Database")

who = tk.Label(window, text = "Name")
what = tk.Label(window, text = "Type")
which = tk.Label(window, text = "Breed")
whose = tk.Label(window, text = "Owner")
when = tk.Label(window, text= "Birthdate")

input1 = tk.Entry(window, text = "")
input2 = tk.Entry(window, text = "")
input3 = tk.Entry(window, text = "")
input4 = tk.Entry(window, text = "")
input5 = tk.Entry(window, text = "")

saver = tk.Button(window, text = "Save Entry", bg="#D3D3D3")
goback = tk.Button(window, text = "< Previous")
cont = tk.Button(window, text = "Next >")

goodboi.grid(row = 1, column = 1, rowspan = 2)
searcher.grid(row = 1, column = 4)
inserter.grid(row = 1, column = 5)

opener.grid(row = 1, column = 3, rowspan = 2)

who.grid(row = 4, column = 1)
what.grid(row = 4, column = 2)
which.grid(row = 4, column = 3)
whose.grid(row = 4, column = 4)
when.grid(row = 4, column = 5)

input1.grid(row = 5, column =1)
input2.grid(row = 5, column =2)
input3.grid(row = 5, column =3)
input4.grid(row = 5, column =4)
input5.grid(row = 5, column =5)

saver.grid(row = 6, column = 3)
goback.grid(row = 6, column = 1)
cont.grid(row = 6, column = 5)

window.mainloop()