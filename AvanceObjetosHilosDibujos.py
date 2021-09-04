#Proyecto UMG - Sistemas Operativos
#AÑO 2021
#python3

import threading
import time
import logging
import turtle
from turtle import RawTurtle, TurtleScreen
from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
import random

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

#geometria de ventana para Turtle
ventana=Tk()
ventana.geometry("900x500")
ventana.title("Carrera de Objetos - manejo de Hilos")
ventana.configure(background="black")
ventana.resizable(0,0)

canvas = Canvas(master = ventana, width = 850, height = 450)
canvas.pack()

#se crea variable para llamar el screen y utilizar el canvas
screen = TurtleScreen(canvas)

# turtle que hace las lineas
t = turtle.RawTurtle(screen)

#instancia de cada objeto
r = turtle.RawTurtle(screen)
a = turtle.RawTurtle(screen)
n = turtle.RawTurtle(screen)
#l = turtle.RawTurtle(canvas)

# se registran las imagenes
r.screen.register_shape('goku.gif')
a.screen.register_shape('nino.gif')
n.screen.register_shape('correCaminos.gif')

#manejo de creación de lineas de pista
t.speed(0)
t.penup()
t.goto(-230,120)

# diseña las lineas de pista
for paso in range(13):
    t.write(paso)
    t.right(90)
    t.forward(10)
    t.pendown()
    # linea vertical
    t.forward(280)
    t.penup()
    t.backward(290)
    t.left(90)
    t.forward(40)

# limpia la ventana de geometria
def reiniciar():
    # tortuga 1 
    r.color('red')
    r.shape('turtle')
    r.shape("goku.gif")
    r.shapesize(4,2)
    r.penup()
    r.goto(-300,130)
    r.pendown()

    # tortuga 2
    a.color('blue')
    a.shape('turtle')
    a.shape("nino.gif")
    a.penup()
    a.goto(-300,0)
    a.pendown()

    # tortuga 3
    n.color('black')
    n.shape('turtle')
    n.shape('correCaminos.gif')
    n.shapesize(1,2)
    n.penup()
    n.goto(-300,-80)
    n.pendown()
 
def competir(id):
    #logging.debug("Ejecutando para el id " +str(id))
    #pass

    #variable para el manejo de aleatorio para avance de objeto
    aleatorio= [10,40]

    # si el id del hilo es el mismo entra
    if id == 1:
        for turn in range(20):
            r.forward(random.choice(aleatorio))
            logging.debug("Ejecutando para el id " + str(id) + " Turno "+ str(turn) )
            time.sleep(1)
            r.penup()
    
    if id == 2:
        for turn in range(20):
            a.forward(random.choice(aleatorio))
            logging.debug("Ejecutando para el id " +str(id))
            time.sleep(1)
            a.penup()

    if id == 3:
        for turn in range(20):
            n.forward(random.choice(aleatorio))
            logging.debug("Ejecutando para el id " +str(id))
            time.sleep(1)
            n.penup()

    # compara la posición x para determinar quien finaliza en una mayor posición e indicar el ganador o si finaliza en empate.
    if r.xcor() > a.xcor() and r.xcor() > n.xcor():
        messagebox.showinfo(message='Ganó - Goku')
        logging.info("Ejecutado para el id " +str(id))
        #print('gana Rojo')
    else:
        if a.xcor() > r.xcor() and a.xcor() > n.xcor():
            messagebox.showinfo(message='Ganó - Niño')
            logging.info("Ejecutado para el id " +str(id))
            #print('gana Azul')
        else:
            if n.xcor() > r.xcor() and n.xcor() > a.xcor():
                messagebox.showinfo(message='Ganó - Corre Caminos')
                logging.info("Ejecutado para el id " +str(id))
                #print('gana Negro')
            else:
                # si son iguales en almenos dos muestra empate
                if r.xcor() == a.xcor() or r.xcor()== n.xcor() or a.xcor() == n.xcor() or n.xcor() == r.xcor():
                    messagebox.showerror(message='Empate!')
    
# funcion que inicia los hilos.
def iniciar():
    t1 = threading.Thread(name="hilo_1", target=competir, args=(1, ))
    t2 = threading.Thread(name="hilo_2", target=competir, args=(2, ))
    t3 = threading.Thread(name="hilo_3", target=competir, args=(3, ))
    t1.start()
    t2.start()
    t3.start()

#muestra en otra ventana a los estudiantes
def estudiantes():  
    ventanados=Tk()
    ventanados.geometry("400x200")
    ventanados.title("Estudiantes")
    ventanados.configure(background="black")
    label = ttk.Label(ventanados, text=
        '           Curso - Sistemas Operativos\n\n'
        'Maurizzio Alessandro de León Arredondo - 0494-17-14262\n'
        'Luis Fernando Guzmán Ortíz             - 0494-07-4802\n'
        'Carlos Enrique Martinez Mansilla       - 0494-09-11209\n'
        'Luis Antonio Fernández diaz            - 0900-19-14501\n' )
    label.pack(side="top", fill="both", expand=True, padx=15, pady=15)

reiniciar()

#definicion de botones
salir = ttk.Button(master=ventana, text='Salir', command=ventana.destroy,  width=3)
salir.pack(side=LEFT)

limpiar = ttk.Button(master=ventana, text='Estudiantes', command=estudiantes)
limpiar.pack(side=LEFT)

crear = ttk.Button(master=ventana, text='Reiniciar', command=reiniciar)
crear.pack(side=RIGHT)

crear = ttk.Button(master=ventana, text='Iniciar', command=iniciar)
crear.pack(side=RIGHT)


ventana.mainloop()

