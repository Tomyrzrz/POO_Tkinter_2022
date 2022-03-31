#Timo Ruiz
#Calculo de Areas - Tkinter - POO

from tkinter import *
from tkinter import messagebox as msg

class Areas():
  def __init__(self):
    self.color_fondo = "#a1d2ce"   #Se crean los colores de la ventana, estos pueden cambiar segun convenga
    self.color_buton = "#78cad2"
    self.color_texto = "#5497a7"

    self.ventana = Tk()  #Configuration basica de la ventana
    self.ventana.title("Calculo de Areas")
    self.ventana.resizable(0,0)
    self.ventana.geometry("350x400")
    self.ventana.configure(bg=self.color_fondo)

    #Etiquetas de texto de la ventana
    self.lbl_area = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Areas").grid(column=0, row=0, pady=7, padx=4, ipadx=3, ipady=3)                       
    self.lbl_figura_geo = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Figura Geométrica").grid(column=0, row=1, pady=7, padx=4, ipadx=3, ipady=3, columnspan=2)                       
    self.lbl_datos_requeridos = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Datos Requeridos: ").grid(column=0, row=3, pady=7, padx=4, ipadx=3, ipady=3, columnspan=2)                       
    self.lbl_base = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Base: ").grid(column=0, row=4, pady=7, padx=4, ipadx=3, ipady=3)                       
    self.lbl_radio = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Radio: ").grid(column=0, row=5, pady=7, padx=4, ipadx=3, ipady=3)                       
    self.lbl_resultado = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="El resultado es: ")
    self.lbl_resultado.grid(column=0, row=6, pady=7, padx=4, ipadx=3, ipady=3, columnspan=2)                       
    self.lbl_altura = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Algerian",12), text="Altura: ").grid(column=2, row=4, pady=7, padx=4, ipadx=3, ipady=3)                       

    #Variables de los valores de los Entry
    self.number_base = StringVar()
    self.number_radio = StringVar()
    self.number_altura = StringVar()
    #Components de los Entry de la ventana.
    self.edt_numero_base = Entry(self.ventana, font=("Arial"), width=5, textvariable=self.number_base, border="2", relief="groove", state="disabled")
    self.edt_numero_base.grid(column=1, row=4, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_numero_radio = Entry(self.ventana, font=("Arial"), width=5, textvariable=self.number_radio, border="2", relief="groove", state="disabled")
    self.edt_numero_radio.grid(column=1, row=5, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_numero_altura = Entry(self.ventana, font=("Arial"), width=4, textvariable=self.number_altura, border="2", relief="groove", state="disabled")
    self.edt_numero_altura.grid(column=3, row=4, pady=7, padx=4, ipadx=3, ipady=3)              

    #Botones de la ventana.
    self.btn_aceptar = Button(self.ventana, font=("Comic"), width=10, bg=self.color_fondo, fg=self.color_texto, command=self.aceptar, text="Aceptar").grid(column=2, row=2, padx=4, pady=2, ipadx=3, ipady=3, sticky="w", columnspan=2)                            
    self.btn_resultado = Button(self.ventana, font=("Comic"), width=10, bg=self.color_fondo, fg=self.color_texto, command=self.resultado, text="Resultado:").grid(column=2, row=5, padx=4, pady=2, ipadx=3, ipady=3, sticky="w", columnspan=2)                            
    self.btn_limpiar = Button(self.ventana, font=("Comic"), width=10, bg=self.color_fondo, fg=self.color_texto, command=self.limpiar, text="Limpiar").grid(column=2, row=6, padx=4, pady=2, ipadx=3, ipady=3, sticky="w", columnspan=2)                            

    #ComboBox - OptionMenu
    self.opciones_areas = ["Triángulo","Rectángulo","Círculo"]
    self.menu_areas = StringVar()
    self.menu_areas.set(self.opciones_areas[0])
    self.cbx_areas = OptionMenu(self.ventana, self.menu_areas, *self.opciones_areas).grid(column=0, row=2, padx=4, pady=2, ipadx=3, ipady=3, columnspan=2)              

    self.ventana.mainloop()
  
  #Metodo para habilitar los Entry segun se haya elegido en las opciones
  def aceptar(self):
    if self.menu_areas.get() == "Triángulo":
      self.edt_numero_base.configure(state="normal")
      self.edt_numero_altura.configure(state="normal")
      self.edt_numero_radio.configure(state="disabled")
    elif self.menu_areas.get() == "Rectángulo":
      self.edt_numero_base.configure(state="normal")
      self.edt_numero_altura.configure(state="normal")
      self.edt_numero_radio.configure(state="disabled")
    else:
      self.edt_numero_base.configure(state="disabled")
      self.edt_numero_altura.configure(state="disabled")
      self.edt_numero_radio.configure(state="normal")
  
  #Metodo para obtener los resultados, primero se verifica que sean numeros y que esten habilitados
  def resultado(self):
    if self.number_altura.get().isdigit() and self.number_base.get().isdigit() and self.menu_areas.get() == "Triángulo" or self.menu_areas.get() == "Rectángulo":                
      if self.menu_areas.get() == "Triángulo":
        results = (float(self.number_altura.get()) * float(self.number_base.get()))/ 2
        texto = "El resultado es: " + str(results)
        self.lbl_resultado.configure(text=texto)
      else:
        results = float(self.number_altura.get()) * float(self.number_base.get())
        texto = "El resultado es: " + str(results)
        self.lbl_resultado.configure(text=texto)
    elif self.number_radio.get().isdigit():
      results = 3.141596 * float(self.number_radio.get()) * float(self.number_radio.get())
      texto = "El resultado es: " + str(results)
      self.lbl_resultado.configure(text=texto)
    else:
      msg.showwarning("Bro", "Debes escribir solo numeros.")
  
  def limpiar(self):
    self.number_altura.set("")
    self.number_base.set("")
    self.number_radio.set("")
    self.lbl_resultado.configure(text="El resultado es: ")
    self.menu_areas.set(self.opciones_areas[0])

window1 = Areas()