# Timo Ruiz
# Calculos de Sueldo x Hora -- Ejercicio del Cuadernillo de Practicas.
# Tkinter con POO

from tkinter import *
from tkinter import messagebox as ms

class Sueldos:    #Se declara una clase de acuerdo al problema planteado.
  def __init__(self):   #TODAS las configuraciones iniciales de la ventana y sus componentes se colocan aqui en el metodo constructor de la clase
    self.color_fondo = "#000099"
    self.color_fondo2 = "#000088"
    self.color_textos = "#FFFFFF"   
    self.color_boton = "#FF1100"    #Declaramos las veriables de colores
    
    self.ventana = Tk()     #Declaramos la ventana principal y sus configuraciones
    self.ventana.geometry("650x500")
    self.ventana.configure(background=self.color_fondo)
    self.ventana.title("Calculo de Sueldos")
    self.ventana.resizable(0,0)
    
    #Aqui todas las etiquetas de la ventana, revisar posiciones en el grid,   border -> tamaño de borde   relief -> Tipo de borde 
    self.lbl_datos = Label(self.ventana, text="Datos", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=0, padx=35, pady=5, ipady=5, ipadx=5)     #Sticky -> Posicion del componente respecto del espacio ocupado        
    self.lbl_nombre = Label(self.ventana, text="Nombre: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=1, padx=35, pady=5, ipady=5, ipadx=5)           
    self.lbl_sueldoxhora = Label(self.ventana, text="Sueldo x Hora: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=2, padx=35, pady=5, ipady=5, ipadx=5)           
    self.lbl_cant_horas = Label(self.ventana, text="Cantidad de horas trabajadas: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",10)).grid(column=0, sticky="w", row=3, padx=35, pady=5, ipady=5, ipadx=5)           
    self.lbl_cant_horas_ext = Label(self.ventana, text="Cantidad Horas Extras: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",12)).grid(column=0, sticky="w", row=4, padx=35, pady=5, ipady=5, ipadx=5)           
    self.lbl_resultado = Label(self.ventana, text="Resultado", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=5, padx=35, pady=5, ipady=5, ipadx=5)           
    self.lbl_sueldo = Label(self.ventana, text="Sueldo: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=6, padx=45, pady=5, ipady=5, ipadx=5)           
    self.lbl_impuestos = Label(self.ventana, text="Impuestos: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=7, padx=45, pady=5, ipady=5, ipadx=5)           
    self.lbl_sueldo_neto = Label(self.ventana, text="Sueldo Neto: ", bg=self.color_fondo, border=2, relief="sunken",
      fg=self.color_textos, font=("Tahoma",14)).grid(column=0, sticky="w", row=8, padx=45, pady=5, ipady=5, ipadx=5)           

    #Declarar las variables donde vamos a almacenar los valores de las cajas
    self.nombre = StringVar()
    self.sueldoxhora = StringVar()
    self.horas_trabajadas = IntVar()
    self.horas_extras = IntVar()
    self.sueldo = StringVar()
    self.impuestos = StringVar()
    self.sueldo_neto = StringVar()

    #Se agregan las cajas y sus variables para cada una de ellas. Revisar el grid para sus posiciones
    self.edt_nombre = Entry(self.ventana, font=("Arial",14), border="1px dashed", textvariable=self.nombre).grid(column=1, row=1, sticky="w", pady=5, ipady=6)
    self.edt_sueldoxhora = Entry(self.ventana, font=("Arial",14), border="1px dashed", textvariable=self.sueldoxhora).grid(column=1, row=2, sticky="w", pady=5, ipady=6)
    self.edt_cant_horas = Entry(self.ventana, font=("Arial",14), border="1px dashed", textvariable=self.horas_trabajadas).grid(column=1, row=3, sticky="w", pady=5, ipady=6)
    self.edt_horas_extras = Entry(self.ventana, font=("Arial",14), border="1px dashed", textvariable=self.horas_extras).grid(column=1, row=4, sticky="w", pady=5, ipady=6)
    self.edt_sueldo = Entry(self.ventana, state="disabled", font=("Arial",14), border="1px dashed", textvariable=self.sueldo).grid(column=1, row=6, sticky="w", pady=5, ipady=6)
    self.edt_impuestos = Entry(self.ventana, state="disabled", font=("Arial",14), border="1px dashed", textvariable=self.impuestos).grid(column=1, row=7, sticky="w", pady=5, ipady=6)
    self.edt_sueldo_neto = Entry(self.ventana, state="disabled", font=("Arial",14), border="1px dashed", textvariable=self.sueldo_neto).grid(column=1, row=8, sticky="w", pady=5, ipady=6)

    #Se agregan los botones, tener en cuenta el atributo command donde se agrega la funcion que hara el boton. Revisar sus posiciones.
    self.btn_calcular = Button(self.ventana, font=("Comic Sans MS",12), width="8", text="Calcular", bg=self.color_boton, fg=self.color_textos, command=self.calcular).grid(column=2, row=6, sticky="e", padx=10, ipady=5, ipadx=5)
    self.btn_limpiar = Button(self.ventana, font=("Comic Sans MS",12), width="8", text="Limpiar", bg=self.color_boton, fg=self.color_textos, command=self.limpiar).grid(column=2, row=7, sticky="e", padx=10, ipady=5, ipadx=5)
    self.btn_salir = Button(self.ventana, font=("Comic Sans MS",12), width="8", text="Salir", bg=self.color_boton, fg=self.color_textos, command=self.salir).grid(column=2, row=8, sticky="e", padx=10, ipady=5, ipadx=5)

    #Por ultimo se agrega el metodo para lanzar la ventana principal en el constructor.
    self.ventana.mainloop()

  #Se definen los metodos que puede realizar la clase (funciones que agregamos en los botones)  
  def calcular(self):
    if self.nombre.get() != "" and self.sueldoxhora.get() != "" and self.horas_trabajadas.get() != 0:       #Se revisa que los campos tengan algo escrito.
      salary = float(self.sueldoxhora.get()) * self.horas_trabajadas.get() + (self.horas_extras.get() * float(self.sueldoxhora.get()) * 2)
      impuest = salary * 0.15
      salary_net = salary - impuest
      self.sueldo.set(salary)
      self.impuestos.set(impuest)
      self.sueldo_neto.set(salary_net)
    else:       #Si no tienen en los campos se envia el mensaje. (Revisar bibliotecas importadas)
      ms.showwarning("Advertencia debes todos los campos", "Llena los campos por favor.")
  
  #Metodo para limpiar las cajas
  def limpiar(self):
    self.nombre.set("")
    self.sueldoxhora.set("")
    self.horas_trabajadas.set(0)
    self.horas_extras.set(0)
    self.sueldo.set("")
    self.impuestos.set("")
    self.sueldo_neto.set("")

  #Metodo para salir de la ventana.
  def salir(self):
    self.ventana.destroy();

# Para construir la ventana del tipo sueldo solamente creamos un objeto (instacia) de la clase, 
# al hacer esto estamos llamando al constructor de la clase donde se diseña y ejecuta la ventana.
ventana1 = Sueldos()
