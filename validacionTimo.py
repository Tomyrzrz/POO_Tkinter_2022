#Timo Ruiz
#Validacion de numeros ->  Tkinter -> POO
from tkinter import *
from tkinter import messagebox as msg

class Validacion():
  def __init__(self):
    #Definimos colores generales de la pantalla
    self.color_fondo = "khaki1"
    self.color_buton = "khaki2"
    self.color_texto = "#000000"

    #Definimos configuraciones basicas de la pantalla
    self.ventana = Tk()
    self.ventana.title("Validacion de numeros")
    self.ventana.resizable(0,0)
    self.ventana.geometry("400x450")
    self.ventana.configure(bg=self.color_fondo)
    
    #Agregamos las etiquetas que ocupamos en la pantalla  
    self.lbl_numero = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",14), text="Número:").grid(column=0, row=0, pady=7, padx=4, ipadx=3, ipady=3)                       
    self.lbl_revisar = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",14), text="Revisar").grid(column=0, row=1, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_resultado = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",14), text="Resultado=").grid(column=0, row=6, pady=7, padx=5, ipadx=3, ipady=3)        

    #Difinimos las variables que serviran de almacen para las Cajas de Texto.
    self.number = IntVar()
    self.result = StringVar()

    #Agregamos las cjas de texto en la pantalla - Revisar las textvariable para colocar las variables anteriores
    self.edt_numero = Entry(self.ventana, font=("Algerian"), width=7, textvariable=self.number, border="2px", relief="flat").grid(column=1, row=0, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_resultado = Entry(self.ventana, font=("Algerian"), width=12, textvariable=self.result, border="2px", relief="flat", state="disabled").grid(column=1, row=6, pady=7, padx=4, ipadx=3, ipady=3)              

    #Definimos las variables para los radioButtons de la pantalla
    self.tipo_numero = IntVar()
    self.tipo = ""

    #Agregamos los RedioButtons en la pantalla - Revisar las "variable" y "value" para colocar las variables anteriores.
    self.rbtn_esPar = Radiobutton(self.ventana, command=self.cambiar, text="Es Par", font=("Arial",16), bg=self.color_fondo, value=0, variable=self.tipo_numero).grid(column=1, row=2, sticky="w", pady=2, padx=4, ipadx=3, ipady=3)                                         
    self.rbtn_esImpar = Radiobutton(self.ventana, command=self.cambiar, text="Es Impar", font=("Arial",16), bg=self.color_fondo, value=1, variable=self.tipo_numero).grid(column=1, row=3, sticky="w", pady=2, padx=4, ipadx=3, ipady=3)                                         
    self.rbtn_esPerfecto = Radiobutton(self.ventana, command=self.cambiar, text="Es Perfecto", font=("Arial",16), bg=self.color_fondo, value=2, variable=self.tipo_numero).grid(column=1, row=4, sticky="w", pady=2, padx=4, ipadx=3, ipady=3)                                         

    #Agregamos los botones a la pantalla - Revisar los "command" de cada boton que llama a una funcion al darle click
    self.btn_revisar = Button(self.ventana, font=("Impact"), width=8, bg=self.color_fondo, fg=self.color_texto, command=self.revisar, text="Revisar").grid(column=2, row=1, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            
    self.btn_limpiar = Button(self.ventana, font=("Impact"), width=8, bg=self.color_fondo, fg=self.color_texto, command=self.limpiar, text="Limpiar").grid(column=2, row=3, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            
    self.btn_salir = Button(self.ventana, font=("Impact"), width=8, bg=self.color_fondo, fg=self.color_texto, command=self.salir, text="Salir").grid(column=2, row=6, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            

    #Metodo principal para visaulizar la pantalla.
    self.ventana.mainloop()
  
  #Metodo "revisar" colocado en los buttons
  def revisar(self):
    if self.tipo == "Par":  #Se revisa si el radioButton "par" esta seleccionado 
      residuo = self.number.get() % 2   #Se almacena el "residuo" de la division del "number" dividido entre 2
      if residuo == 0:  #Si el residuo de la division es "0" entonces el numero si es par.
        self.result.set("Si es Par")
      else:
        self.result.set("No es Par")
    elif self.tipo == "Impar":  #Se revisa si el radioButton "impar" esta seleccionado 
      response = self.number.get() % 2   #Se almacena el "residuo" de la division del "number" dividido entre 2
      if response == 0:  #Si el residuo de la division es "0" entonces el numero No es impar
        self.result.set("No es Impar")
      else:
        self.result.set("Si es Impar")
    else:
      self.saberPerfecto(self.number.get()) #Si no se selecciona el "par" o el "impar" entonces se llama al metodo "saberPerfecto"
  
  def saberPerfecto(self, numero):  #El metodo "saberPerfecto" recibe el numero de la caja de texto
    suma = 0    #Se crea una variable para almacenar la suma de los numero que son divisores exactos positivos del numero
    for i in range(1, numero):  #Se hace un for para dividir el numero entre todos sus numeros anteriores positivos comenzando del 1
      if (numero % i == 0):  #Si el residuo de la division entre 2 del numero es 0 entonces ese numero se suma
        suma += i   #Se suman los numero que son divisores exactos positivos.
    if numero == suma:    #Se revisa si la suma obtenida es igual al numero
      self.result.set("Si es Perfecto")  #Si es igual entonces es un Numero Perfecto
    else:
      self.result.set("No Perfecto")  #Si NO es igual entonces NO es Numero Perfecto

  #Metodo para limpiar las cajas de la pantalla
  def limpiar(self):
    self.tipo_numero.set(None)
    self.result.set("")
    self.number.set(0)
  
  #Metodo para salir del programa
  def salir(self):
    self.ventana.destroy()

  #Metodo para revisar los cambios de la seleccion de los RadioButtons 
  def cambiar(self):
    if self.tipo_numero.get() == 0:  #Cada que haya un cambio se obtiene su valor, si es "0" entonces se selecciono "Par"
      self.tipo = "Par"
    elif self.tipo_numero.get() == 1:  #Si es "1" entonces se selecciono "Impar"
      self.tipo = "Impar"
    else:
      self.tipo = "Perfecto"   #Si no es "0" o "1" entonces se selecciono Perfecto

#Se crea un objeto de la clase de la pantalla para inicializarla
ventana1 = Validacion()