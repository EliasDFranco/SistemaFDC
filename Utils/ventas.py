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

#28-12-2024 se agregaron estás funcionalidades;
#02-01-2025 se subieron los cambios

        label_nombre = tk.Label(lblframe, text="Producto: ", bg="#BAFBEB", font="sans 12 bold")
        label_nombre.place(x=200 , y=12 )
        self.entry_nombre = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_nombre.place(x=280 , y=10, width=180)

        label_valor = tk.Label(lblframe, text="Precio: ", bg="#BAFBEB", font="sans 12 bold")
        label_valor.place(x=470 ,y=12)
        self.entry_valor = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_valor.place(x=540 , y=10 , width=180)

        label_cantidad = tk.Label(lblframe, text="Cantidad: ", bg="#BAFBEB", font="sans 12 bold")
        label_cantidad.place(x=730, y=12)
        self.entry_cantidad = ttk.Entry(lblframe, font="sans 12 bold")
        self.entry_cantidad.place(x=820 , y=10 )

        treFrame = tk.Frame(frame2, bg="#BAFBEB")
        treFrame.place(x=150, y=120, width=800, height=200)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM , fill=X)

        self.tree = ttk.Treeview(treFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command=self.tree.yview)
        scrol_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("Producto", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Cantidad", anchor="center")
        self.tree.column("Subtotal", anchor="center")

        self.tree.pack(expand= True, fill=BOTH)

        lblframe1 = LabelFrame(frame2, text="Opciones", bg="#BAFBEB", font="sans 12 bold")
        lblframe1.place(x=10 , y=380, width=1060, height=100)

#02-01-2025 Agregado estos botones
        boton_agregar = tk.Button(lblframe1, text= "Agregar artículo", bg="#BAFBEB", font="sans 12 bold")
        boton_agregar.place(x= 50, y= 10, width=240, height=50)

        boton_pagar = tk.Button(lblframe1, text= "Pagar ", bg="#BAFBEB", font="sans 12 bold")
        boton_pagar.place(x=400, y=10, width=240, height=50)

        boton_ver_facturas = tk.Button(lblframe1, text="Ver facturas: ", bg="#BAFBEB", font="sans 12 bold")
        boton_ver_facturas.place(x=750, y=10, width=240, height=50)


        