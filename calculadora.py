from tkinter import *
import decimal 


ventana = Tk ()
ventana.title("Calculadora")

n=2
i = 0

#definir configuracion de los botones 
boton_config = {
    "font": ("Roman", 16),
    "bd": 4,
    "relief": RAISED,
}


# Entrada 
e_texto = Entry(ventana, font=("Arial 20"))
e_texto.grid(row=0, column=0, columnspan= 4, padx = 50 , pady=8)


# funciones 
def click_boton(valor):
      global i
      e_texto.insert(i, valor)
      i += 1 

def borrar ():
        e_texto.delete (-1, END)
        global i
        i = -1

def BACK ():
    global i
    i = i-1 
    e_texto.delete(i, END)

def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete (0, END)
    e_texto.insert(0, resultado)  

def Notacion ():
        resultado_texto = e_texto.get()
        resultado = decimal.Decimal(resultado_texto)
        resultado_notacion_cientifica = "{:e}".format(resultado)
        e_texto.delete(0, END)
        e_texto.insert(0, resultado_notacion_cientifica)
    
def exponencial():

    operaciones2=e_texto.get()
    resultado=decimal.Decimal (eval(operaciones2))
    e_texto.delete(0, END)
    e_texto.insert(0, str(resultado**n))
  
def exponente ():
    global i 
    e_texto.insert(i, "**")
    i +=2 
    e_texto.delete(END)



#dissable 
def BOTON_BLOQ():
    if (boton_ON['text'] == 'ON'):
     boton_ON ['text'] = 'OFF'
    else:
        boton_ON ['text'] = 'ON' 
    
    if (boton1 ['state'] == NORMAL ):
        boton1['state'] = DISABLED
    
    else: 
        boton1['state']= NORMAL     
        
    if (boton2 ['state'] == NORMAL ):
        boton2['state'] = DISABLED
    
    else: 
        boton2['state']= NORMAL  
        
    if (boton3 ['state'] == NORMAL ):
        boton3['state'] = DISABLED
    
    else: 
        boton3['state']= NORMAL  
        
    if (boton4 ['state'] == NORMAL ):
        boton4['state'] = DISABLED
    
    else: 
        boton4['state']= NORMAL
    
    if (boton5 ['state'] == NORMAL ):
        boton5['state'] = DISABLED
    
    else: 
        boton5['state']= NORMAL 
        
    if (boton6 ['state'] == NORMAL ):
        boton6['state'] = DISABLED
    
    else: 
        boton6['state']= NORMAL  
        
    if (boton7 ['state'] == NORMAL ):
        boton7['state'] = DISABLED
    
    else: 
        boton7['state']= NORMAL  

#botones

boton_ON = Button (ventana, text = "ON", width=6, height=2, command = lambda: BOTON_BLOQ (),  **boton_config)
boton1 = Button(ventana, text = "1", width=6, height=2,state= DISABLED, command = lambda: click_boton(1),  **boton_config)
boton2 = Button(ventana, text = "2", width=6, height=2,state= DISABLED, command = lambda: click_boton(2),  **boton_config)
boton3 = Button(ventana, text = "3", width=6, height=2,state= DISABLED, command = lambda: click_boton(3),  **boton_config)
boton4 = Button(ventana, text = "4", width=6, height=2,state= DISABLED, command = lambda: click_boton(4),  **boton_config)
boton5 = Button(ventana, text = "5", width=6, height=2,state= DISABLED, command = lambda: click_boton(5),  **boton_config)
boton6 = Button(ventana, text = "6", width=6, height=2,state= DISABLED, command = lambda: click_boton(6),  **boton_config)
boton7 = Button(ventana, text = "7", width=6, height=2,state= DISABLED, command = lambda: click_boton(7),  **boton_config)
boton8 = Button(ventana, text = "8", width=6, height=2, command = lambda: click_boton(8), **boton_config)
boton9 = Button(ventana, text = "9", width=6, height=2, command = lambda: click_boton(9),  **boton_config)
boton0 = Button(ventana, text = "0", width=13, height=2, command = lambda: click_boton(0),  **boton_config) 

boton_borrar = Button(ventana, text = "AC", width=6, height=2, command = lambda: borrar(), font=("Roman", 16), bd=4, relief=RAISED, bg="tomato")
boton_BACK = Button(ventana, text = "BA", width=6, height=2, command= lambda: BACK (),  **boton_config)
boton_parentesis1 = Button(ventana, text = "(", width=6, height=2, command = lambda: click_boton("("),  **boton_config)
boton_parentesis2 = Button(ventana, text = ")", width=6, height=2, command = lambda: click_boton(")"),  **boton_config)
boton_punto = Button(ventana, text = ".", width=6, height=2, command = lambda: click_boton("."),  **boton_config)
boton_notacion = Button (ventana, text= "*10", width=6, height=2, command= lambda: Notacion(),  **boton_config)
boton_exponencial = Button(ventana, text= "*2", width= 6, height=2, command= lambda: exponencial (),  **boton_config ) 
boton_exponente = Button(ventana, text= "^", width = 6, height=2, command= lambda: exponente(),  **boton_config)                 

boton_div = Button(ventana, text = "/", width=6, height=2, command = lambda: click_boton("/"),  **boton_config)
boton_mult = Button(ventana, text = "x", width=6, height=2, command = lambda: click_boton("*"),  **boton_config)
boton_sum = Button(ventana, text = "+", width=6, height=2, command = lambda: click_boton("+"),  **boton_config)
boton_res = Button(ventana, text = "-", width=6, height=2, command = lambda: click_boton("-"),  **boton_config)
boton_igual = Button(ventana, text = "=", width=6, height=2, command = lambda: hacer_operacion(),font=("Roman", 16), bd=4, relief=RAISED, bg="lightgreen")

# agregar papeles en pantalla 

boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5 )
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5 )
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5 )
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5 )
boton_BACK.grid(row= 1, column= 4, padx=5, pady=5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5 )
boton8.grid(row = 2, column = 1, padx = 5, pady = 5 )
boton9.grid(row = 2, column = 2, padx = 5, pady = 5 )
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5 )
boton_ON.grid (row= 2, column=4, padx=5, pady=5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5 )
boton5.grid(row = 3, column = 1, padx = 5, pady = 5 )
boton6.grid(row = 3, column = 2, padx = 5, pady = 5 )
boton_sum.grid(row = 3, column = 3, padx = 5, pady = 5 )
boton_exponencial.grid(row=3, column=4, padx= 5, pady=5)


boton1.grid(row = 4, column = 0, padx = 5, pady = 5 )
boton2.grid(row = 4, column = 1, padx = 5, pady = 5 )
boton3.grid(row = 4, column = 2, padx = 5, pady = 5 )
boton_res.grid(row = 4, column = 3, padx = 5, pady = 5 )
boton_exponente.grid (row = 4, column=4, padx= 5, pady=5)

boton0.grid(row = 5, column = 0,columnspan = 2, padx = 5, pady = 5 )
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5 )
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5 )
boton_notacion.grid (row= 5, column= 4, padx=5, pady = 5)


ventana.mainloop()
