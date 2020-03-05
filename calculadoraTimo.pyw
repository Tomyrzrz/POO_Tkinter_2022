#Hacer la interfaz de la
#calculadora de WINDOWS

from tkinter import *
from tkinter import messagebox

#---------------RAIZ----------------
ventana_raiz = Tk()
ventana_raiz.title("Calculadora")
ventana_raiz.config(bg="white")
ventana_raiz.resizable(0,0)

#--------------------VARIABLES GLOBALES-------------------------
operacion = ""
resultados = 0

#---------------------FUNCIONES DE LA CALCULADORA---------------#
def ponerNumeros(pnumero):
	global operacion
	if numeroPantalla.get() == "0":
		numeroPantalla.set(pnumero[1:len(pnumero)])
	
	if operacion != "":
		numeroPantalla.set(pnumero)
		operacion = ""
	else:
		numeroPantalla.set( numeroPantalla.get() + pnumero)

def queOperacion(poperacion, pnumero):
	global operacion
	global resultados
	operacion = poperacion
	if poperacion == "suma":
		resultados = resultados + int(pnumero)
		numeroPantalla.set(resultados)


#---------------------TITULO SUPERIOR-------------------------#
framesu = Frame(ventana_raiz, width=300, height=700)
framesu.config(bg="#CCCCCC", bd=1, relief="groove") #groove
framesu.pack()
menu = PhotoImage(file="menu.png")
Label(framesu, image=menu, bg="#CCCCCC", width=50, height=50).grid(row=0,column=0, padx=10)
Label(framesu, text="Estandar", bg="#CCCCCC", font=("Arial", 14)).grid(row=0,column=1, padx=10,columnspan=2, sticky="E")
keep = PhotoImage(file="keep.png")
Label(framesu, image=keep, bg="#CCCCCC", width=50, height=50).grid(row=0,column=3,padx=14)
alarma = PhotoImage(file="alarm.png")
Label(framesu, image=alarma, bg="#CCCCCC", width=50, height=50).grid(row=0,column=4, padx=10)

#-----------------------PANTALLA---------------------------#
frame = Frame(ventana_raiz, width=300, height=700)
frame.config(bg="#CCCCCC", bd=1, relief="groove") #groove
frame.pack()
numeroPantalla = StringVar()
txt_pantalla = Entry(frame, textvariable=numeroPantalla, 
	bg="gray", font=("Arial",21),bd=2, justify="right")
txt_pantalla.grid(row=1,column=0,pady=1,padx=1,sticky="S", 
	columnspan=6, ipady=10)
numeroPantalla.set("0")

#-----------------------FILA 1 ---------------------------#
btn_mc = Button(frame, text="MC", bg="#777777", fg="#555555", font=("Arial",14))
btn_mc.grid(row=2,column=0,padx=1,pady=1, ipady=2, ipadx=3)

btn_mr = Button(frame, text="MR", bg="#777777", fg="#555555", font=("Arial",14))
btn_mr.grid(row=2,column=1,padx=1,pady=1, ipady=2, ipadx=3)

btn_mmas = Button(frame, text="M+", bg="#666666", font=("Arial",14))
btn_mmas.grid(row=2,column=2,padx=1,pady=1, ipady=2, ipadx=3)

btn_mmenos = Button(frame, text="M-", bg="#666666", font=("Arial",14))
btn_mmenos.grid(row=2,column=3,padx=1,pady=1, ipady=2, ipadx=4)

btn_ms = Button(frame, text="MS", bg="#666666", font=("Arial",14))
btn_ms.grid(row=2,column=4,padx=2,pady=1, ipady=2, ipadx=3)

btn_mplus = Button(frame, text="M^", bg="#777777",fg="#555555", font=("Arial",14))
btn_mplus.grid(row=2,column=5,padx=2,pady=1,ipady=2, ipadx=4)

#-------------------FILA 2--------------------------------#
frame2 = Frame(frame, width=300, height=700)
frame2.config(bg="#777777", bd=1, relief="groove") #groove
frame2.grid(row=3,column=0,columnspan=6)

btn_porcent = Button(frame2, text=" % ", bg="#999999", font=("Arial",15))
btn_porcent.grid(row=0,column=0,padx=1,ipady=7, ipadx=18)

btn_ce = Button(frame2, text=" CE", bg="#999999", font=("Arial",15))
btn_ce.grid(row=0,column=1,padx=1,ipady=7, ipadx=18)

btn_c = Button(frame2, text=" C ", bg="#999999", font=("Arial",15))
btn_c.grid(row=0,column=2,padx=1,ipady=7, ipadx=18)

btn_erase = Button(frame2, text=" <-", bg="#999999", font=("Arial",15))
btn_erase.grid(row=0,column=3,padx=1,ipady=7, ipadx=18)

#-------------------FILA 3--------------------------------#
btn_inverso = Button(frame2, text="1/x", bg="#999999", font=("Arial",15))
btn_inverso.grid(row=1,column=0,padx=1,ipady=7, ipadx=20)

btn_exponent = Button(frame2, text="x^2", bg="#999999", font=("Arial",15))
btn_exponent.grid(row=1,column=1,padx=1,ipady=7, ipadx=20)

btn_raiz = Button(frame2, text=" √x", bg="#999999", font=("Arial",15))
btn_raiz.grid(row=1,column=2,padx=1,ipady=7, ipadx=18)

btn_division = Button(frame2, text=" /  ", bg="#999999", font=("Arial",15))
btn_division.grid(row=1,column=3,padx=1,ipady=7, ipadx=18)

#-------------------FILA 4--------------------------------#
btn_7 = Button(frame2, text=" 7  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("7"))
btn_7.grid(row=2,column=0,padx=1,ipady=7, ipadx=19)

btn_8 = Button(frame2, text=" 8  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("8"))
btn_8.grid(row=2,column=1,padx=1,ipady=7, ipadx=20)

btn_9 = Button(frame2, text=" 9 ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("9"))
btn_9.grid(row=2,column=2,padx=1,ipady=7, ipadx=20)

btn_multiplicacion = Button(frame2, text=" X ", bg="#999999", font=("Arial",15))
btn_multiplicacion.grid(row=2,column=3,padx=1,ipady=7, ipadx=18)

#-------------------FILA 5--------------------------------#
btn_4 = Button(frame2, text=" 4  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("4"))
btn_4.grid(row=3,column=0,padx=1,ipady=7, ipadx=19)

btn_5 = Button(frame2, text=" 5  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("5"))
btn_5.grid(row=3,column=1,padx=1,ipady=7, ipadx=20)

btn_6 = Button(frame2, text=" 6 ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("6"))
btn_6.grid(row=3,column=2,padx=1,ipady=7, ipadx=20)

btn_resta = Button(frame2, text=" -  ", bg="#999999", font=("Arial",15))
btn_resta.grid(row=3,column=3,padx=1,ipady=7, ipadx=18)

#-------------------FILA 5--------------------------------#
btn_1 = Button(frame2, text=" 1  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("1"))
btn_1.grid(row=4,column=0,padx=1,ipady=7, ipadx=19)

btn_2 = Button(frame2, text=" 2  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("2"))
btn_2.grid(row=4,column=1,padx=1,ipady=7, ipadx=20)

btn_3 = Button(frame2, text=" 3 ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("3"))
btn_3.grid(row=4,column=2,padx=1,ipady=7, ipadx=20)

btn_suma = Button(frame2, text=" + ", bg="#999999", font=("Arial",15), command=lambda:queOperacion("suma", numeroPantalla.get()))
btn_suma.grid(row=4,column=3,padx=1,ipady=7, ipadx=18)

#-------------------FILA 6--------------------------------#
btn_mm = Button(frame2, text="+/-", bg="#DDDDDD", font=("Arial",15))
btn_mm.grid(row=5,column=0,padx=1,ipady=7, ipadx=21)

btn_0 = Button(frame2, text=" 0  ", bg="#DDDDDD", 
	font=("Arial",15), command=lambda:ponerNumeros("0"))
btn_0.grid(row=5,column=1,padx=1,ipady=7, ipadx=20)

btn_punto = Button(frame2, text=" .  ", bg="#DDDDDD", font=("Arial",15), command=lambda:ponerNumeros("."))
btn_punto.grid(row=5,column=2,padx=1,ipady=7, ipadx=19)

btn_igual = Button(frame2, text=" = ", bg="#999999", font=("Arial",15))
btn_igual.grid(row=5,column=3,padx=1,ipady=7, ipadx=18)





ventana_raiz.mainloop()

