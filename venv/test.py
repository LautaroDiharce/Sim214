import clases
import clases.ascensor as ac
from clases import pasajero as pas
import funciones
import random
import numpy as np
import math
import pandas as pd

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

capacidad = 6  
ascensor_a = 180 #3min
ascensor_b= 540 #9min
h = 5
init_subida = 3
init_bajada = 5
e=5 #seg
d=5 #seg
a=5 #seg
prob_subida = 0,7
prob_bajada = 1-prob_subida
lambda_ =300 #seg
reloj = 0.0
contador_pas = 1
dir = "sube"
cola_sube=[]
cola_baja=[]
pasajeros_tot = []



pasajero=pas.Pasajero(1,15,5,5,0.5)
pasajeros_tot.append(pasajero)
cola_sube.append(pasajero)
print(pasajero)
pasajero=pas.Pasajero(2,30,5,5,0.88)
pasajeros_tot.append(pasajero)
pasajero=pas.Pasajero(3,30,5,5,0.88)
pasajeros_tot.append(pasajero)
pasajero=pas.Pasajero(4,30,5,5,0.88)
pasajeros_tot.append(pasajero)

print(pasajeros_tot)
for persona in pasajeros_tot:
    print(persona)

