from tkinter import ttk
from tkinter import *

#LOGICA DE SISTEMAS
#PRIMER SEMESTRE, INGENIERÍA EN SISTEMAS
#SULMA FABIOLA MARTÍNEZ ZUÑIGA
#CARNET:0907-19-25172

#PROGRAMA QUE MUESTRA EL RESULTADO DE UNA DIVISIÓN, EXAMINANDO SI EL DIVISOR ES 0 O NO

class Desk:
    def __init__(self, window):
    
        #ancho
        ancho = 800
        #alto
        alto = 600
        
        # asignamos la ventana a una variable de la clase llamada wind
        self.wind = window

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry
        self.wind.geometry(str(ancho)+'x'+str(alto))

        #centramos el contenido 
        self.wind.columnconfigure(0, weight=1)
        
        #le damos un titulo a la ventana
        self.wind.title('EXAMEN LOGICA DE SISTEMAS')
        
        # creamos un contenedor
        frame = LabelFrame(self.wind, text = 'INGRESAR 3 VALORES')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        # creamos un etiqueta
        Label(frame, text = 'NUMERO 1: ').grid(row = 1, column = 0)
        
        #creamos un input donde ingresar valores
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 1, column = 1)
        
        # igual que arriba una etiqueta y un campo input para ingresar valores
        Label(frame, text = 'NUMERO 2: ').grid(row = 2, column = 0)
        self.var2 = Entry(frame)
        self.var2.grid(row = 2, column = 1)

        #creamos un tercer campo
        Label(frame, text = 'NUMERO 3: ').grid(row = 3, column = 0)
        self.var3 = Entry(frame)
        self.var3.grid(row = 3, column = 1)
        
    
        #Botones
        Button(frame, text= 'BOTON1', command= self.funcion1, background= "light blue").grid(row= 7, columnspan= 2, sticky= W + E)
        Button(frame, text= 'BOTON2', command= self.funcion2, background= "light blue").grid(row= 8, columnspan= 2, sticky= W + E)

        #designamos un área para mensajes
        self.message = Label(text = '', fg = 'fuchsia')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        
    # creamos una función para validar que los campos no esten en blanco
    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0
    
    

    #FUNCION PRIMER BOTÓN
    def funcion1(self):
    
        if int(self.var1.get()) < int(self.var3.get()):
            resultado1 = int(self.var1.get())* int(self.var2.get()) * int(self.var3.get())
            self.message['text'] = 'Se ha realizado una multiplicación de los 3 números. '+ 'Resultado: {}'.format(resultado1)
        else:    

            if int(self.var1.get())== int(self.var3.get()):
                resultado1 = int(self.var1.get()) + int(self.var2.get()) + int(self.var3.get())
                self.message['text'] = 'Se ha realizado una suma de los 3 números. '+ 'Resultado: {}'.format(resultado1)
            else:

                if int(self.var2.get())== 0:
                    if int(self.var1.get()) < int(self.var3.get()):
                        resultado1 = int(self.var3.get())- int(self.var1.get())
                        self.message['text'] = 'Se ha realizado una resta del número 3 menos el número 1. '+ 'Resultado: {}'.format(resultado1)
                    else:
                        resultado1 = int(self.var1.get()) - int(self.var3.get())
                        self.message['text'] = 'Se ha realizado una resta del número 1 menos el número 3. '+ 'Resultado: {}'.format(resultado1)
    
    #funcion 2 concatenar los input                   
    def funcion2(self):

        resultado1 = int(self.var1.get()) * int(self.var2.get()) + int(self.var3.get())
    
        #for para que imprima un mensaje por el numero del resultado anterior
        for i in range(resultado1):
            self.message['text'] = 'Se ha concatenado los 3 números. '+ int(self.var1.get()) + int(self.var2.get()) + int(self.var3.get()
            


#validamos si estamos en la aplicación inicial
if __name__ == '__main__':
    
    #asignamos la propiedad de tkinter a la variable window
    window = Tk()
    
    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana 
    app = Desk(window)

    #ejecutamos un mainloop para que se ejecute la ventana
    window.mainloop()