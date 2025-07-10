from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox
import sqlite3 #Importamos la libreria de la BD
class Ventas(tk.Frame):
    db_name = "database_fdc.db" #Variable declarada para hacer la conexión con el archivo de la DB
    
    def __init__(self, parent):
        super().__init__(parent)
        self.numeroFacturaActual = self.obtener_numeroFacturaActual()
        self.widgets()
        self.mostrarNumeroFactura()
        

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
        self.entry_nombre = ttk.Combobox(lblframe, font="sans 12 bold", state="readonly") #Cambiamos ENTRY por COMMBOBOX
        self.entry_nombre.place(x=280 , y=10, width=180)

        self.cargarProductos()

        label_valor = tk.Label(lblframe, text="Precio: ", bg="#BAFBEB", font="sans 12 bold")
        label_valor.place(x=470 ,y=12)
        self.entry_valor = ttk.Entry(lblframe, font="sans 12 bold", state="readonly")
        self.entry_valor.place(x=540 , y=10 , width=180)

        self.entry_nombre.bind("<<ComboboxSelected>>", self.actualizarPrecio)

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
        boton_agregar = tk.Button(lblframe1, text= "Agregar artículo", bg="#BAFBEB", font="sans 12 bold", command=self.registrar)
        boton_agregar.place(x= 50, y= 10, width=240, height=50)

        boton_pagar = tk.Button(lblframe1, text= "Pagar ", bg="#BAFBEB", font="sans 12 bold", command= self.abrirVentanaPago)
        boton_pagar.place(x=400, y=10, width=240, height=50)

        boton_ver_facturas = tk.Button(lblframe1, text="Ver facturas: ", bg="#BAFBEB", font="sans 12 bold", command=self.abrirVentanaPago)
        boton_ver_facturas.place(x=750, y=10, width=240, height=50)

#15-01-2025 Creación de un último label 
        self.label_sumaTotal = tk.Label(frame2, text="Total a pagar: 0 Gs", bg="#BAFBEB", font="sans 25 bold")
        self.label_sumaTotal.place(x=360 , y=335)

#Función cargar productos desde la BD
    def cargarProductos(self):
        try: 
            conn = sqlite3.connect(self.db_name)
            c= conn.cursor()
            c.execute("SELECT nombre FROM inventario")

            producto = c.fetchall()
            self.entry_nombre["values"] = [producto[0] for producto in producto]
#Iniciamos un loop para ver si existe algún producto
            if not producto:
                print("No se han encontrado productos en la Base de Datos.")
            conn.close() #Aqui se cierra el loop

        except sqlite3.Error as e:
            print(f"Error al cargar productos desde la Base de Datos", e)
        
#Función para actualizar los precios desde la BD
    def actualizarPrecio(self, event):
        nombreProducto = self.entry_nombre.get()
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT precio FROM inventario WHERE nombre = ?", (nombreProducto,))
            precio = c.fetchone()
            if (precio):
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, precio[0])
                self.entry_valor.config(state="readonly")

            else:
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.insert(0, "Precio no disponible")
                self.entry_valor.config(state="readonly")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"al obtener el precio: {e}")
        finally:
            conn.close()

#Función para actualizar el total a pagar 
    def actualizarTotal(self):
        total = 0.0 
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        self.label_sumaTotal.config(text="Total a pagar: Gs {total:.0f}")

#Función para registrar los productos
    def registrar(self):
        producto = self.entry_nombre.get()
        precio = self.entry_valor.get()
        cantidad = self.entry_cantidad.get()

        if producto and precio and cantidad:
            try:
                cantidad = int(cantidad)
                if not self.verificarStock(producto, cantidad):
                    messagebox.showerror("Error", "Stock insuficiente para el producto seleccionado")
                    return  
                precio = float(precio)
                subtotal = cantidad * precio

                self.tree.insert("","end", values=(producto, f"{precio:.0f}", cantidad, f"{subtotal:.0f}"))

                self.entry_nombre.set("")
                self.entry_valor.config(state="normal")
                self.entry_valor.delete(0, tk.END)
                self.entry_valor.config(state="readonly")
                self.entry_cantidad.delete(0, tk.END)
        
                self.actualizarTotal()
            except ValueError:
                messagebox.showerror("Error", "Cantidad o precio no válido")

        else:
            messagebox.showerror("Error","Debe de completar todos los campos")

    def verificarStock(self, nombre, producto, cantidad):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT stock FROM inventarios WHERE nombre = ?",(nombre))
            stock = c.fetchone()
            if stock and stock[0] >= cantidad:
                return True
            return False

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al verificar el stock: {e}")
            return False
        finally:
            conn.close()

    def obtenerTotal(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        return total

#Función para ventana
    def abrirVentanaPago(self):
        if not self.tree.get_children():
            messagebox.showerror("Error", "No hay articulos para pagar")
            return 
        ventanaPago = Toplevel(self)
        ventanaPago.title("Realizar pago")
        ventanaPago.geometry("400x400")
        ventanaPago.config(bg="#BAFBEB")
        ventanaPago.resizable(False, False)

        label_total = tk.Label(ventanaPago, bg="#BAFBEB", text=f"Total a pagar: Gs {self.obtenerTotal():.0f}", font="sans 18 bold")
        label_total.place(x=70, y=20)

        label_cantidadPagada = tk.Label(ventanaPago, bg="#BAFBEB", text="Cantidad pagada", font="sans 14 bold")
        label_cantidadPagada.place(x=100, y=90)
        entry_cantidadPagada = ttk.Entry(ventanaPago, font="sans 14 bold")
        entry_cantidadPagada.place(x=100, y=130)

        label_vuelto = tk.Label(ventanaPago, bg="#BAFBEB", text="", font="sans 14 bold")
        label_vuelto.place(x=100 , y=190)

#Función para calcular el vuelto/cambio 
        def calcularVuelto(self):
            try:
                cantidadPagada = float(entry_cantidadPagada.get())
                total = self.obtenerTotal()
                vuelto = cantidadPagada - total
                if vuelto < 0:
                    messagebox.showerror("Error", "La cantidad pagada es insuficiente")
                    return
                label_vuelto.config(text=f"Vuelto: Gs {vuelto:.0f}")
            except ValueError:
                messagebox.showerror("Error", "Cantidad pagada no válida")

        botonCalcular = tk.Button(ventanaPago, text="Calcular vuelto", bg="white", font="sans 12 bold", command=calcularVuelto)
        botonCalcular.place(x=100, y=240, width=240, height=40)

        botonPagar = tk.Button(ventanaPago, text="Pagar", bg="white", font="sans 12 bold", command=lambda: self.pagar(ventanaPago, entry_cantidadPagada, label_vuelto))
        botonPagar.place(x=100 , y=300 , width=240, height=40 )

#Función de pagar
    def pagar(self, ventanaPago, entry_cantidadPagada, label_vuelto):
        try: 
            cantidadPagada = float(entry_cantidadPagada.get())
            total  = self.obtenerTotal()
            vuelto = cantidadPagada - total
            if vuelto < 0: 
                messagebox.showerror("Error", "La cantidad pagada es insuficiente")
                return

            conn = sqlite3.connect(self.db_name)     
            c = conn.cursor()
            try:
                for child in self.tree.get_children():
                    item = self.tree(child, "values")
                    nombreProducto = item[8]
                    cantidadVendida = int(item[2])
                    if not self.verificarStock(nombreProducto, cantidadVendida):
                        messagebox.showerror("Error", f"Stock insuficiente para el producto: {nombreProducto}")

                    c.execute("INSERT INTO ventas (factura, nombre_articulo, valor_articulo, cantidad, subtotal) VALUES(?,?,?,?,?)",
                    (self.numeroFacturaActual, nombreProducto, float(item[1]), cantidadVendida, float(item[3])))

                    c.execute("UPDATE inventario SET stock = stock - ? WHERE = ?", (cantidadVendida, nombreProducto))

                conn.commit()
                messagebox.showinfo("Exito", "Venta registrada exitosamente")

                self.numeroFacturaActual += 1
                self.mostrarNumeroFactura()

                for child in self.tree.get_children():
                    self.tree.delete(child)
                self.label_suma_total.config(text="Total a pagar: Gs 0")
                
                ventanaPago.destroy() #Destroy para que se cierre la ventana

            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error al registrar la venta: {e}")
            finally:
                conn.close()

        except ValueError:
            messagebox.showerror("Error", "Cantidad pagada no válida")

    def obtener_numeroFacturaActual(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try: 
            c.execute("SELECT MAX(factura) FROM ventas")
            maxFactura = c.fetchone()[0]
            if maxFactura:
                return maxFactura +1
            else: 
                    return 1
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el número de factura: {e}")
            return 1 
        finally:
            conn.close()

    def mostrarNumeroFactura(self):
        self.NumeroFactura.set(self.numeroFacturaActual)

    def abrirVentanaFactura(self):
        ventanaFacturas = Toplevel
        ventanaFacturas.title("Factura ")
        ventanaFacturas.geometry("800x500")
        ventanaFacturas.config(bg="#BAFBEB")
        ventanaFacturas.resizable(False, False)

        facturas = Label(ventanaFacturas, text="facturas registradas", bg="#BAFBEB", font="sans 36 bold")
        facturas.place(x=150 ,  y=15)
        
        treFrame = tk.Frame(ventanaFacturas, bg="#BAFBEB")
        treFrame.place(x=10, y=100, width=780, height=380)

        scrol_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scrol_y.pack(side=RIGHT, fill=Y)

        scrol_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scrol_x.pack(side=BOTTOM , fill=X)

        tree_Facturas = ttk.Treeview(treFrame, columns=("ID", "Factura", "Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scrol_y.set, xscrollcommand=scrol_x.set)
        scrol_y.config(command= tree_Facturas.yview)
        scrol_x.config(command= tree_Facturas.xview)

        tree_Facturas.heading("#1", text="ID")
        tree_Facturas.heading("#2", text="Factura")
        tree_Facturas.heading("#3", text="Producto")
        tree_Facturas.heading("#4", text="Precio")
        tree_Facturas.heading("#5", text="Cantidad")
        tree_Facturas.heading("#6", text="Subtotal")

        tree_Facturas.column("ID", width=70 ,anchor="center")
        tree_Facturas.column("Factura", width=100, anchor="center")
        tree_Facturas.column("Producto", width=200, anchor="center")
        tree_Facturas.column("Precio", width=200, anchor="center")
        tree_Facturas.column("Cantidad", width=130, anchor="center")
        tree_Facturas.column("Subtotal", width=130, anchor="center")

        tree_Facturas.pack(expand= True, fill=BOTH)

        self.cargarFacturas(tree_Facturas)

    def cargarFacturas(self, tree):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT * FROM ventas")
            facturas = c.fetchall()
            for factura in facturas:
                tree.insert("","end", values=factura)
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar las facturas: {e}")