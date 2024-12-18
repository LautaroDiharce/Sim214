import clases
import clases.ascensor as ac
from clases import pasajero as psj
import funciones.calculos as cal
import random
import numpy as np
import math
import pandas as pd
from tkinter import * 

# P = pasajeros que descienden
# H = pasajeros totales
# D = segundos que toma al pasajero descender
# Dir = direccion del ascensor
# A = segundos que toma al pasajero ascender
# Cmax = capacidad maxima = 6
# E = tiempo de espera para cerrar puertas
# L = minutos entre arribo de pasajeros 70% baja #0% sube
# determinar el tiempo de permanencia del ascensor en el piso 15.
# H1 = 5 || Dir = up || Pas_sube_1 = 3 ||Pas_baja_1 =5
contador_listbox =0
capacidad = 6  
ascensor_a = 180 #3min
ascensor_b= 540 #9min
p = 5
h=6
init_subida = 3
init_bajada = 5
e=5 #seg
d=5 #seg
a=5 #seg
prob_subida:float
prob_subida = 0.7
prob_bajada = 1-prob_subida
lambda_ =300 #seg
reloj = 0.0
contador_pas = 1
dir = "sube"
cola_sube=[]
cola_baja=[]
pasajeros_tot = []

def pasajeros_iniciales(pasajeros_actual):
    #### TODO: agregar inicializador de direccion
    global contador_pas
    while contador_pas <= p:
        pasajeros_actual.append(psj.Pasajero(contador_pas,0,d,a,0.5))
        contador_pas +=1
        #print("ini_actual")
    for pasajero in pasajeros_actual:
        print(pasajero)
    return pasajeros_actual

def cola_sube_inicial(cola_sube):
    global contador_pas
    while contador_pas <= p+init_subida:
        cola_sube.append(psj.Pasajero(contador_pas,0,d,a,0.5))
        contador_pas +=1
        #print("ini_up")
    for pasajero in cola_sube:
        print(pasajero)
    return cola_sube

def cola_baja_inicial(cola_baja):
    global contador_pas
    while contador_pas <= p+init_subida+init_bajada:
        cola_baja.append(psj.Pasajero(contador_pas,0,d,a,0.9))
        contador_pas +=1
        #print("ini_down")
    for pasajero in cola_baja:
        print(pasajero)
    return cola_baja

pasajeros_actual=[]
cola_sube=[]
cola_baja=[]
p = 5
contador_pas = 1
reloj = 0.0
dir = "sube"
asc=ac.Ascensor(capacidad,p,e,dir)
pasajeros_actual=pasajeros_iniciales(pasajeros_actual)
cola_sube=cola_sube_inicial(cola_sube)
cola_baja=cola_baja_inicial(cola_baja)
pasajeros_tot=pasajeros_actual+cola_sube+cola_baja  
#for persona in pasajeros_tot:print(persona)
t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)
t_prox_llegada=cal.llgada_pasajero(lambda_)

lista1 = pasajeros_tot
lista2 = pasajeros_actual

# Convirtiendo las listas en conjuntos (basados en el atributo 'nombre')
conjunto1 = set(pasajero.id for pasajero in lista1)
conjunto2 = set(pasajero.id for pasajero in lista2)
print(conjunto1)
print(conjunto2)
# Calculando la diferencia de conjuntos (elementos en lista1 pero no en lista2)
#TODO: revisar cosistencia de la diferencia
diferencia = conjunto1 - conjunto2
print(diferencia)
# Creando una nueva lista con los elementos restantes
resultado = [pasajero for pasajero in lista1 if pasajero.id in diferencia]


def test_lsbx(lsbx:Listbox):
    global contador_listbox
    contador_listbox +=1
    print("test listbox")
    print(lsbx)
    # lsbx.insert(END,str(vector[0]))
    # if contador_listbox == 10:
    #     contador_listbox=0
    #     listbox.update()

