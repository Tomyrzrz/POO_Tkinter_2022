#Timo Ruiz
#Comidas Tkinter -> POO

from tkinter import *
from tkinter import messagebox as ms

class Comidas():
  def __init__(self):
    self.color_fondo = "#dc5c05"  #Definimos los colores de la App y componentes
    self.color_buton = "#ff9e00"
    self.color_texto = "#f7d705"

    self.ventana = Tk()    #Definimos configuracion basicas de la ventana.
    self.ventana.title("Comidas") 
    self.ventana.resizable(0,0)
    self.ventana.geometry("520x500")
    self.ventana.configure(bg=self.color_fondo)

    #Definimos los componentes Label de la ventana
    self.lbl_combos = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="Selecciona los combos").grid(column=0, row=0, pady=7, padx=4, ipadx=3, ipady=3)                       
    self.lbl_cantidad = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="Cantidad").grid(column=0, row=1, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_precio = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="Precio").grid(column=2, row=1, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_precio_inf = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="$85.50").grid(column=2, row=2, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_precio_duo = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="$90.00").grid(column=2, row=3, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_precio_fam = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="$105").grid(column=2, row=4, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_precio_trio = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="$95.50").grid(column=2, row=5, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_subtotal = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="Subtotal:").grid(column=1, row=6, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_iva = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="IVA:").grid(column=1, row=7, pady=4, padx=4, ipadx=3, ipady=3)        
    self.lbl_total = Label(self.ventana, bg=self.color_fondo, fg=self.color_texto, font=("Daytona",12), text="Total:").grid(column=1, row=8, pady=4, padx=4, ipadx=3, ipady=3)        
    
    #Definimos las variables de los Entry
    self.number_pq_inf = StringVar()
    self.number_pq_duo = StringVar()
    self.number_pq_fam = StringVar()
    self.number_pq_trio = StringVar()
    self.subtotal = StringVar()
    self.iva = StringVar()
    self.total = StringVar()

    #Definimos los componentes Entry de la ventana, tener en cuenta que necesitas separar el grid en dos lineas.
    self.edt_numero_pq_inf = Entry(self.ventana, font=("Algerian"), width=5, textvariable=self.number_pq_inf, border="2px", relief="flat", state="disabled")
    self.edt_numero_pq_inf.grid(column=0, row=2, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_numero_pq_duo = Entry(self.ventana, font=("Algerian"), width=5, textvariable=self.number_pq_duo, border="2px", relief="flat", state="disabled")
    self.edt_numero_pq_duo.grid(column=0, row=3, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_numero_pq_fam = Entry(self.ventana, font=("Algerian"), width=5, textvariable=self.number_pq_fam, border="2px", relief="flat", state="disabled")
    self.edt_numero_pq_fam.grid(column=0, row=4, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_numero_pq_trio = Entry(self.ventana, font=("Algerian"), width=5, textvariable=self.number_pq_trio, border="2px", relief="flat", state="disabled")
    self.edt_numero_pq_trio.grid(column=0, row=5, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_subtotal = Entry(self.ventana, font=("Algerian"), width=6, textvariable=self.subtotal, border="2px", relief="flat", state="disabled").grid(column=2, row=6, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_iva = Entry(self.ventana, font=("Algerian"), width=6, textvariable=self.iva, border="2px", relief="flat", state="disabled").grid(column=2, row=7, pady=7, padx=4, ipadx=3, ipady=3)              
    self.edt_total = Entry(self.ventana, font=("Algerian"), width=6, textvariable=self.total, border="2px", relief="flat", state="disabled").grid(column=2, row=8, pady=7, padx=4, ipadx=3, ipady=3)              

    #Definimos los botones de la ventana, revisar los command para sus respectivos metodos.
    self.btn_aceptar = Button(self.ventana, font=("Impact"), width=8, bg=self.color_fondo, fg=self.color_texto, command=self.aceptar, text="Aceptar").grid(column=0, row=7, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            
    self.btn_new_shopping = Button(self.ventana, font=("Impact",10), width=13, bg=self.color_fondo, fg=self.color_texto, command=self.new_shopping, text="New Shopping").grid(column=0, row=8, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            
    self.btn_salir = Button(self.ventana, font=("Impact"), width=8, bg=self.color_fondo, fg=self.color_texto, command=self.salir, text="Salir").grid(column=2, row=9, padx=4, pady=2, ipadx=3, ipady=3, sticky="w")                            

    #Se definen las variables de los ChechButton
    self.chb_paq_infantil = IntVar()
    self.chb_paque_duo = IntVar()
    self.chb_paq_familiar = IntVar()
    self.chb_paque_trio = IntVar()
    #Se crean los CheckButton, tener en cuenta la variable asignada y los valores de onvalue y offvalue y la funcion asignada en el command
    self.chb_paq_inf = Checkbutton(self.ventana, command=self.habilitarCajas, text="Paquete Infantil", bg=self.color_fondo, fg=self.color_texto, variable=self.chb_paq_infantil, onvalue=1, offvalue=0, height=1, width=12, font=("Arial",12)).grid(column=1, row=2, padx=4, pady=1, ipadx=3, ipady=1)
    self.chb_paq_duo = Checkbutton(self.ventana, command=self.habilitarCajas, text="Paquete Duo", bg=self.color_fondo, fg=self.color_texto, variable=self.chb_paque_duo, onvalue=1, offvalue=0, height=1, width=12, font=("Arial",12)).grid(column=1, row=3, padx=4, pady=1, ipadx=3, ipady=1)
    self.chb_paq_fam = Checkbutton(self.ventana, command=self.habilitarCajas, text="Paquete Familiar", bg=self.color_fondo, fg=self.color_texto, variable=self.chb_paq_familiar, onvalue=1, offvalue=0, height=1, width=12, font=("Arial",12)).grid(column=1, row=4, padx=4, pady=1, ipadx=3, ipady=1)
    self.chb_paq_trio = Checkbutton(self.ventana, command=self.habilitarCajas, text="Paquete Trio", bg=self.color_fondo, fg=self.color_texto, variable=self.chb_paque_trio, onvalue=1, offvalue=0, height=1, width=12, font=("Arial",12)).grid(column=1, row=5, padx=4, pady=1, ipadx=3, ipady=1)

    self.ventana.mainloop()  #Metodo para mostrar la ventana diseñada
  
  #Metodo asignado a los Checkbutton
  def habilitarCajas(self):
    if self.chb_paque_duo.get() == 1:
      self.edt_numero_pq_duo.config(state="normal")
    else:
      self.chb_paque_duo.get() == 0
      self.edt_numero_pq_duo.config(state="disabled")
    if self.chb_paq_familiar.get() == 1:
      self.edt_numero_pq_fam.config(state="normal")
    else:
      self.chb_paq_familiar.get() == 0
      self.edt_numero_pq_fam.config(state="disabled")
    if self.chb_paq_infantil.get() == 1:
      self.edt_numero_pq_inf.config(state="normal")
    else:
      self.chb_paq_infantil.get() == 0
      self.edt_numero_pq_inf.config(state="disabled")
    if self.chb_paque_trio.get() == 1:
      self.edt_numero_pq_trio.config(state="normal")
    else:
      self.chb_paque_trio.get() == 0
      self.edt_numero_pq_trio.config(state="disabled")

  #Metodo para realizar los calculos de las comidas, primero se verifica que esten checados y tenga solo numeros.
  def aceptar(self):
    suma = 0
    if self.number_pq_trio.get() == 0 and self.number_pq_duo.get() == 0 and self.number_pq_fam.get() == 0 and self.number_pq_inf.get() == 0:
      ms.showerror("Error", "Debes seleccionar algun paquete")
    elif not self.number_pq_inf.get().isdigit() and self.chb_paq_infantil.get() == 1:        
       ms.showerror("Tontito", "Escribe solo numeros.")
    elif not self.number_pq_fam.get().isdigit() and self.chb_paq_familiar.get() == 1:     
       ms.showerror("Tontito", "Escribe solo numeros.")
    elif not self.number_pq_duo.get().isdigit() and self.chb_paque_duo.get() == 1:     
       ms.showerror("Tontito", "Escribe solo numeros.") 
    elif not self.number_pq_trio.get().isdigit() and self.chb_paque_trio.get() == 1:     
       ms.showerror("Tontito", "Escribe solo numeros.")
    else:
      if self.chb_paq_infantil.get() == 1:
        suma = suma + float(self.number_pq_inf.get()) * 85.50
      if self.chb_paque_duo.get() == 1:
        suma = suma + float(self.number_pq_duo.get()) * 90
      if self.chb_paq_familiar.get() == 1:
        suma = suma + float(self.number_pq_fam.get()) * 105
      if self.chb_paque_trio.get() == 1:
        suma = suma + float(self.number_pq_trio.get()) * 95.50
      iva = suma * 0.15
      total = suma + iva
      self.subtotal.set(str(suma))
      self.iva.set(str(iva))
      self.total.set(str(total))

  #Metodo para el boton de nueva compra.
  def new_shopping(self):
    self.total.set(0)
    self.iva.set(0)
    self.number_pq_duo.set(0)
    self.number_pq_fam.set(0)
    self.number_pq_inf.set(0)
    self.number_pq_trio.set(0)
    self.subtotal.set(0)
    self.edt_numero_pq_duo.configure(state="disabled")
    self.edt_numero_pq_fam.configure(state="disabled")
    self.edt_numero_pq_inf.configure(state="disabled")
    self.edt_numero_pq_trio.configure(state="disabled")
    self.chb_paque_duo.set(0)
    self.chb_paq_familiar.set(0)
    self.chb_paq_infantil.set(0)
    self.chb_paque_trio.set(0)
  def salir(self):
    self.ventana.destroy()

#Se crea el objeto de la clase para poder la ventana.
window1 = Comidas()

