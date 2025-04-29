from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 #Importamos sqlite3

class Inventario(tk.Frame): 
    db_name = "Database/database_fdc.db" # Aquí conecto la bd a una variable
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.com = sqlite3.connect(self.db_name)
        self.cursor = self.com.cursor # Cursor que permite hacer las consultas que necesitamos
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#50C878", highlightbackground="grey", highlightthickness=2)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="Inventarios", bg="#50C878", font="Arial 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x= 5, y=0, width=1090, height=90)

#09-01-2025 
        frame2 = tk.Frame(self, bg="#BAFBEB", highlightthickness=1, highlightbackground="gray")
        frame2.place(x=0 , y=100, width=1100, height=550)

        labelframe = LabelFrame(frame2, text="Productos", font="sans 21 bold", bg="#BAFBEB")
        labelframe.place(x=20, y=30, width=400, height=500)

        lblnombre = Label(labelframe, text="Nombre: ", font="sans 14 bold", bg="#BAFBEB")
        lblnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font="sans 14 bold")
        self.nombre.place(x=140, y=20, width=240, height=40)

        lblproveedor = Label(labelframe, text="Proveedor: ", font="sans 14 bold" , bg="#BAFBEB")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font="sans 14 bold")
        self.proveedor.place(x=140, y=80, width=240, height=40)

        lblprecio = Label(labelframe, text="Precio: ", font="sans 14 bold", bg="#BAFBEB" )
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font="sans 14 bold")
        self.precio.place(x=140 , y=140 , width=240 , height=40)

        lblcosto = Label(labelframe, text="Costo: ", font="sans 14 bold", bg="#BAFBEB")
        lblcosto.place(x=10 , y=200)
        self.costo = ttk.Entry(labelframe, font="sans 14 bold")
        self.costo.place(x=140 , y=200 , width=240 , height=40)

        lblstock = Label(labelframe, text="Stock: ", font="sans 14 bold", bg="#BAFBEB")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font="sans 14 bold")
        self.stock.place(x=140, y=260, width=240, height=40)

        boton_agregar = tk.Button(labelframe, text="Ingresa", font="sans 14 bold", bg="#22CBA6")
        boton_agregar.place(x=80, y=340, width=240, height=40)

        boton_editar = tk.Button(labelframe, text="Editar", font="sans 14 bold", bg="#22CBA6")
        boton_editar.place(x=80, y=400, width=240 , height=40 )

        #Creando tabla en la parte derecha
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        scrol_y = ttk.Scrollbar(treFrame)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM, fill=X)

        self.tre = ttk.Treeview(treFrame, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set, height=40,
        columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scrol_y.config(command=self.tre.yview)
        scrol_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="id")
        self.tre.heading("PRODUCTO", text="Producto")
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("PRECIO", text="Precio")
        self.tre.heading("COSTO", text="Costo")
        self.tre.heading("STOCK", text="Stock")

        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PRODUCTO", width=100, anchor="center")
        self.tre.column("PROVEEDOR", width=100, anchor="center")
        self.tre.column("PRECIO", width=100, anchor="center")
        self.tre.column("COSTO", width=100, anchor="center")
        self.tre.column("STOCK", width=70, anchor="center")
        
        self.mostrarInventario() # Llamo a la funciónn mostrar inventario para que me muestre en el apartado de "Inventarios", los productos que hya disponible
        botonActualizar = Button(frame2, text="Actualizar inventario", font="sans 14 bold", command=self.actualizarInventario)
        botonActualizar.place(x=440, y=480, width=260, height=50)
    #29-04-2025
    def ejeConsulta(self, consulta, parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
        return result
    
    def validacion(self, nombre, prov, precio, costo, stock):
        if not (nombre and prov and precio and costo and stock):
            return False 
        try: 
            float(precio)
            float(costo)
            int(stock)
        except ValueError:
            return False
        return True
    
    def mostrarInventario(self):
        consulta = "SELECT * FROM inventario ORDER BY id DESC"
        result =  self.ejeConsulta(consulta)
        for elemento in result:
            try: 
                precioGS = "GS {:,.0f}".format(float(elemento[3])) if elemento[3] else ""
                costoGS = "GS {:,.0f}".format(float(elemento[4])) if elemento[4] else ""
            except ValueError: 
                precioGS = elemento[3]
                costoGS = elemento[4]
            self.tre.insert("", 0 , text=elemento[0], values=(elemento[1], elemento[2], precioGS, costoGS, elemento[5]))
            
    def actualizarInventario(self):
        for item in self.tre.get_children():
            self.tre.delete(item)
            
        self.mostrarInventario()
        
        messagebox.showinfo("Actualización", "El inventario ha sido actualizado correctamente")