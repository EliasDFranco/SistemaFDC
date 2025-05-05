from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=600)
        self.config(bg="#C6D9E3")
        self.widgets()

    def show_frames(self, container):
            top_level = tk.Toplevel(self)
            frame = container(top_level)
            frame.configure(bg="#C6D9E3")
            frame.pack(fil="both", expand= True)
            
            top_level.geometry("1100x650+120+20")
            top_level.resizable(False, False)
            
            # Permite que la ventana de inicio se superponga a Ventas o Inventario
            top_level.transient(self.master)
            top_level.grab_set()
            top_level.focus_set()
            top_level.lift()

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

    def widgets(self):
        frame1 = tk.Frame(self, bg="#BAFBEB")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)
        
        # Configurando par que se muestre un icono dentro del botón ventas
        imagen_pil = Image.open("iconos/compras.png")
        imagen_resize = imagen_pil.resize((40,40))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)
        
        boton_ventas = Button(frame1, bg="#50C878", fg="black", font="helvetica 20 bold", text="Ir a ventas", command=self.ventas)
        boton_ventas.config(image=imagen_tk, compound=LEFT, padx=30) # Aqui lo agrego dentro de botón
        boton_ventas.image = imagen_tk
        boton_ventas.place(x=500, y=30, width=240, height=60)


        # Configurando par que se muestre un icono dentro del botón inventario
        imagen_pil = Image.open("iconos/inventario.png")
        imagen_resize = imagen_pil.resize((40,40))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)
        
        boton_inventario = Button(frame1, bg="#50C878", fg="black", font="helvetica 20 bold", text="Ir al inventario", command=self.inventario)
        boton_inventario.config(image=imagen_tk, compound=LEFT, padx=-10) # También agregamos dentro del botón
        boton_inventario.image = imagen_tk
        boton_inventario.place(x=500, y=130, width=240, height=60)

        self.logo_image = Image.open("imagenes/cajaregistradora.png")
        self.logo_image  = self.logo_image.resize((300,280))
        self.logo_image =  ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="white") 
        self.logo_label.place(x=40, y=20)


        #Copyright 
        copyright_label = tk.Label(frame1, text= "© 2024 Franco Duarte Comercial - Todos los derechos reservados", font="sans 8 bold")
        copyright_label.place(x=200 , y=350)