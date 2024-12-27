from cgi import print_form
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#50C878", highlightbackground="grey", highlightthickness=2)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="Ventas", bg="#50C878", font="athene 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x= 5, y=0, width=1090, height=90)