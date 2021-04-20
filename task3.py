import tkinter as tk
from tkinter import *
from tkinter import ttk  

window = tk.Tk()
window.title("That dog which looks like Snoopy but not really Snoopy")
window.geometry("250x133")

doggy = PhotoImage(file="dog.png")
goodboi = tk.Label(window, image=doggy)

Potato = tk.Label(window, text = "Pochacco!")
Descript = tk.Label(window, text = "A cuddly little puppy! This is from the same \ncreator who brought you Keropi and Kero Kero", bg = "#00FFFF")

goodboi.place(x=59,y=0)
Potato.place(x=125,y=41.5)
Descript.place(x=0,y=98)

window.mainloop()