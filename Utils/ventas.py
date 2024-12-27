from cgi import print_form
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#50C878", highlightbackground="gray", highlightthickness=2)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="Ventas", bg="#50C878", font="athene 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#BAFBEB", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0 , y=100, width=1100 , height=550)

        lblframe = LabelFrame(frame2, text="Información de la venta", bg="#BAFBEB", font="sans 16 bold")
        lblframe.place(x=10, y=10, width=1060, height=80)

        label_num_factura = tk.Label(lblframe, text="Número de\nfactura", bg="#BAFBEB", font="sans 12 bold")
        label_num_factura.place(x=10, y=5)
        self.num_factura = tk.StringVar()

        self.entry_num_factura = ttk.Entry(lblframe, textvariable=self.num_factura, state="readonly", font="sans 12 bold")
        self.entry_num_factura.place(x=100 , y=5, width=80)