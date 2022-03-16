#Timo ruiz
#Conversor de monedas con Tkinter

#Importar librerias basicas de Tkinter
from tkinter import *
from tkinter import messagebox as ms

#Objeto y configuracion basica de la ventana raiz del programa
raiz = Tk()
raiz.title("Conversor Monedas")
raiz.geometry("650x350")
raiz.configure(background="gray60")

#Variables para colores
color_boton = "#9802AD"
color_textos = "#000000"
color_fondo = "gray60"
color_fondo2 = "gray50"
color_cajas = "#CCCFFF"

#Variables para almacenar los valores de las cajas de texto
pesos = StringVar()
pesos_dolares = StringVar()
dolares = StringVar()
euros = StringVar()

#Funcion para limpiar las cajas
def limpiar():
  pesos.set("")    #Asigna un valor vacio a las cajas de texto
  pesos_dolares.set("")
  dolares.set("")
  euros.set("")

#Funcion para salir de la vetana principal del programa
def salir():
  raiz.destroy()   #Destruye la ventan inicial

#Funcion para calcular las conversiones de monedas
def calcular(pPesos):
  if pPesos == "":    #Revisa si la variable enviada esta vacia
    ms.showerror("Error", message="No has escrito los pesos.")
  elif pPesos.isdigit():   #Revisa si la variable es solo digitos
    dollars = float(pPesos) * 20.88
    euross = float(pPesos) * 22.94
    dolares.set(str(dollars))
    euros.set(str(euross))
    pesos_dolares.set(pPesos)    #Asignamos los valores a las respectivas cajas
  else:    #Si no se ingresan numero envia un mensaje de error
    ms.showerror(title="Tonto", message="Debes escribir solo numeros.")

#Se agregan dos objetos de tipo frame para darle formato y diseño a la ventana.
frame = Frame(raiz, width=650, height=100, border=1, bg=color_fondo2).grid(row=0, column=0, columnspan=5, rowspan=1)
frame2 = Frame(raiz, width=650, height=250, border=1, bg=color_fondo).grid(row=1, column=0, columnspan=5, rowspan=3)

#Se agregan los componentes en los frames
lbl_pesos = Label(frame, text="Pesos: $", font=("sans-serif",14), fg=color_textos, bg=color_fondo2)
lbl_pesos.grid(column=0, row=0, pady=5, padx=5, ipady=10, ipadx=6)

edt_pesos = Entry(frame, font=("sans-serif",8), fg=color_textos, bg=color_fondo2, textvariable=pesos)
edt_pesos.grid(column=1, row=0, pady=5, padx=5, ipady=10, ipadx=6)

#Aqui se asignan las funciones creadas anteriormente a los botones de la ventana.
btn_calcular = Button(frame2, text="Calcular", width=7, bd=1, font=("arial",12), command=lambda:calcular(pesos.get()))            
btn_calcular.grid(row=1, column=0, pady=5, padx=5, ipadx=6, ipady=10)

btn_limpiar = Button(frame2, text="Limpiar", width=7, bd=1, font=("arial",12), command=lambda:limpiar())
btn_limpiar.grid(row=2, column=0, pady=5, padx=5, ipadx=6, ipady=10)

btn_salir = Button(frame2, text="Salir", width=7, bd=1, font=("arial",12), command=lambda:salir())
btn_salir.grid(row=3, column=0, pady=5, padx=5, ipadx=6, ipady=10)

edt_pesos_d = Entry(frame, font=("sans-serif",8), fg=color_textos, bg=color_fondo, state="disabled", textvariable=pesos_dolares)
edt_pesos_d.grid(column=1, row=1, pady=5, padx=5, ipady=10, ipadx=6)
lbl_peso = Label(frame, text="Pesos=", font=("sans-serif",14), fg=color_textos, bg=color_fondo)
lbl_peso.grid(column=2, row=1, pady=5, padx=5, ipady=10, ipadx=6)

edt_pesos_d = Entry(frame, font=("sans-serif",8), fg=color_textos, bg=color_fondo, state="disabled", textvariable=dolares)
edt_pesos_d.grid(column=3, row=1, pady=5, padx=5, ipady=10, ipadx=6)
lbl_dolar = Label(frame, text="Dolares", font=("sans-serif",14), fg=color_textos, bg=color_fondo)
lbl_dolar.grid(column=4, row=1, pady=5, padx=5, ipady=10, ipadx=6)

edt_pesos_e = Entry(frame, font=("sans-serif",8), fg=color_textos, bg=color_fondo, state="disabled", textvariable=pesos_dolares)
edt_pesos_e.grid(column=1, row=2, pady=5, padx=5, ipady=10, ipadx=6)
lbl_pesos = Label(frame, text="Pesos=", font=("sans-serif",14), fg=color_textos, bg=color_fondo)
lbl_pesos.grid(column=2, row=2, pady=5, padx=5, ipady=10, ipadx=6)

edt_pesos_e = Entry(frame, font=("sans-serif",8), fg=color_textos, bg=color_fondo, state="disabled", textvariable=euros)
edt_pesos_e.grid(column=3, row=2, pady=5, padx=5, ipady=10, ipadx=6)
lbl_pesos = Label(frame, text="Euros", font=("sans-serif",14), fg=color_textos, bg=color_fondo)
lbl_pesos.grid(column=4, row=2, pady=5, padx=5, ipady=10, ipadx=6)

#Se inicia la actividad principal con el metodo mainloop
raiz.mainloop()


