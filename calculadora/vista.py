import tkinter
from turtle import right 
import modelo as logica
ventana = tkinter.Tk()
bit = ventana.iconbitmap('calculator-icon_34473.ico')
#window
ventana.title('calculadora')
ventana.geometry("400x300")
ventana.configure(bg='#49A')
title = tkinter.Label(ventana,text='ingresa los dos valores a operar', bg='#96e6a1', )
title.pack(fill=tkinter.X)
valorUno = tkinter.Entry(ventana)
valorUno.pack()
valorDos = tkinter.Entry(ventana)
valorDos.pack()



#functions
def suma():
    n1 = float(valorUno.get())
    n2 = float(valorDos.get())
    operacion = logica.Calculadora(n1,n2)
    result = operacion.suma
    etiqueta = tkinter.Label(ventana,text= result)
    etiqueta.pack()
    
    
def resta():
    n1 = float(valorUno.get())
    n2 = float(valorDos.get())
    operacion = logica.Calculadora(n1,n2)
    result = operacion.resta
    etiqueta = tkinter.Label(ventana,text= result)
    etiqueta.pack()




def  multiplicacion():
    n1 = float(valorDos.get())
    n2 = float(valorDos.get())
    operacion = logica.Calculadora(n1,n2)
    result = operacion.producto
    etiqueta = tkinter.Label(ventana,text= result)
    etiqueta.pack()

def division():
    n1 = float(valorUno.get())
    n2 = float(valorDos.get())
    operacion = logica.Calculadora(n1,n2)
    result = operacion.division
    etiqueta = tkinter.Label(ventana,text= result)
    etiqueta.pack()
    
#buttons
suma = tkinter.Button(ventana,text="+", bg='#96e6a1', command= suma)
suma.place(x=50, y=65)
resta = tkinter.Button(ventana,text="-", bg='#96e6a1', command= resta)
resta.place(x=150, y=65)

multi = tkinter.Button(ventana,text="X", bg='#96e6a1', command= multiplicacion)
multi.place(x=250, y=65)

mult = tkinter.Button(ventana,text="%", bg='#96e6a1', command= division)
mult.place(x=350, y=65)




ventana.mainloop()