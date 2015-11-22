# -*- coding: utf-8 -*-
Edad1 = 10
Nombre1 = "Anakin"
Bando1 = "Ninguno"

Edad2 = 17
Nombre2 = "Obiwan"
Bando2 = "Jedi"

Edad3 = 896
Nombre3 = "Yoda"
Bando3 = "Jedi"

def mensaje(edad,nombre,bando):
    print "El personaje " + nombre +" hizo su aporte al bando de los " + bando + " cuando tenia "+ str(edad) +" años."

mensaje(Edad1,Nombre1,Bando1)
mensaje(Edad2,Nombre2,Bando2)
mensaje(Edad3,Nombre3,Bando3)


#Crear la clase que define un objeto
class Personaje:
    def __init__(self,Edad,Nombre,Bando):
        #Creamos variables globales con la informacion del objeto al crearse
        self.Nombre = Nombre
        self.Edad = Edad
        self.Bando = Bando
    
    def mensajepel(self, pelicula):
        print "En la pelicula "+ str(pelicula) + "."
        
    def mensaje(self):
        #usamos las variables globales
        print "El personaje " + self.Nombre +" hizo su aporte al bando de los " + self.Bando + " cuando tenia "+ str(self.Edad) +" años."
        
    
    Edad = 0
    Nombre = "no tiene"
    Bando = "no tiene"

#Crear el objeto p1 de la clase Personaje
p1 = Personaje(17,"Anakin","Ninguno")
#Crear el objeto p2 de la clase Personaje
p2 = Personaje(196,"Yoda","Jedi")

p1.mensaje()
p1.mensajepel(1)
p2.mensaje()
p2.mensajepel(1)

p1.Edad = 23
p1.Bando = "Sith"
p1.mensaje()
p1.mensajepel(3)