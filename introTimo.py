#Timo Ruiz
#Interfaces 1

from tkinter import *
from tkinter import messagebox
#Tkinter solo soporta imagenes GIF y PNG
from PIL import ImageTk, Image     #Usar PIL para imagenes JPG y JPEG
#Debes instalar pillow con el comando -> pip install pillow

import os
#Rutas dinamicas para las imagenes del programa
absolute_folder_path = os.path.dirname(os.path.realpath(__file__)) #Aqui se obtiene la ruta del archivo python base
absolute_image_path = os.path.join(absolute_folder_path, 'tkinter.png') #Aqui se une la ruta base con el nombre de la imagen
absolute_image_path2 = os.path.join(absolute_folder_path, 'imagentk.jpg') #Aqui se repite para otra imagen

ventana = Tk()   #es un objeto de tipo TK (Tk es una ventana)
ventana.geometry("450x350")   #Tamaño
ventana.title("Tom Rvys")     #Titulo
ventana.resizable(1,1)        #Permitir que se estire la ventana
ventana.configure(background="#000000")   #Color de fondo
#      #12   3A     BC
#      Red  Green  Blue
#ventana.iconbitmap("favicon.ico")  #Poner el icono
color_button = "#888888"
color_texto = "#6666FF"

#Para colocar Textos usamos la clase Label()
#Para colocar Botones usamos la clase Button()
#Para colocar Cajas de Texto usamos la clase Entry()
lbl_titulo = Label(ventana, text="Mi primer ventana", fg=color_texto, font=("Arial",20), bg="#000000")
# text -> Texto que mostrara  fg -> color de letras    font -> tipo de letras y tamaño   bg -> color de fondo
lbl_titulo.grid(column=1, row=0, pady=5, padx=5, ipady=5, ipadx=5)
# column -> columna donde se colocara     row -> fila donde se colocara     padx -> espacio dentro del objeto en eje x
# pady -> espacio dentro del objeto en eje      ipadx -> espacio afuera del objeto eje x
# ipady -> espacio afuera del objeto en eje y

lbl_nombre = Label(ventana, text="Nombre:", fg=color_texto, font=("Arial",20), bg="#000000")
lbl_nombre.grid(column=0, row=1, padx=5, pady=5, ipady=5, ipadx=5)

#Variables donde se almacena la informacion
nombre = StringVar()
apellido = StringVar()

#Las variables creadas antes se asignan al atributo    textvariable
edt_nombre = Entry(ventana, fg="#0000FF", textvariable=nombre)
edt_nombre.grid(column=1, row=1, columnspan=2, padx=5, pady=5, ipady=5, ipadx=5)

lbl_apellido = Label(ventana, fg=color_texto, font=("Arial",20), bg="black", text="Apellidos:")
lbl_apellido.grid(column=0, row=2, padx=5, pady=5, ipady=5, ipadx=5)

edt_apellido = Entry(ventana, fg=color_texto, textvariable=apellido)
edt_apellido.grid(column=1, row=2, columnspan=2, padx=5, pady=5, ipady=5, ipadx=5)

# TAREA
# INDICAR QUE LE FALTA AL USUARIO
# TAREA EN EL CUADERNO
# Que son y para que sirven, un ejemplo en python de METODOS ESTATICOS
def saludar():    
  if nombre.get() != "" and nombre.get() != None and apellido.get() != None and apellido.get() != "":
    #nombre.get()   nos sirve para obtener el valor de las cajas a donde fueron asignadas
    mensaje = "Hola " + nombre.get() + " " + apellido.get() + " bienvenido al bello mundo de la programacion."
    messagebox.showinfo(title="Saludo", message=mensaje)
    nombre.set("")       #Asignar un valor a la caja
    apellido.set("")
  elif nombre.get() == "" and apellido.get() != "":
    messagebox.showerror(title="Error", message="Te falta el nombre")
  elif apellido.get() == "" and nombre.get() != "":
    messagebox.showerror(title="Error", message="Te falta el apellido")
  else:
    messagebox.showerror(title="Error", message="No hay datos llena el nombre y el apellido")

#Funcion de salir de la ventana de Tkinter
def salir():
  ventana.destroy()

#Funcion para limpiar los campos de la ventana de Tkinter
def limpiar():
  nombre.set("")
  apellido.set("")

#Se crea una variable para ubicar y contener la imagen y sus caracteristicas
imagen = PhotoImage(file=absolute_image_path, height="100", width="100")
contenedor = Label(ventana, image=imagen).grid(column=0, row=4)  #Aqui la variable para contener la imagen

#PIL solution    
img = ImageTk.PhotoImage(Image.open(absolute_image_path2), size="100x100")  # PIL solution
contenedor2 = Label(ventana, image=img).grid(column=0, row=5)


btn_guardar = Button(ventana, text="Saludar", bg=color_button, fg=color_texto, width=9, font=("Arial",16), command=lambda:saludar())
# EL ATRIBUTO command SIRVE PARA VINCULAR UNA FUNCION
# width -> se usa para el largo del objeto
btn_guardar.grid(column=1, row=3, padx=5, pady=5, ipady=5, ipadx=5)

ventana.mainloop()  #Este metodo hace que la ventana se mantenga visible


