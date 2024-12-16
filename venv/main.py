import clases
import clases.ascensor as ac
import clases.pasajero as psj
import funciones.calculos as cal
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
p = 5
h=6
init_subida = 3
init_bajada = 5
e=5 #seg
d=5 #seg
a=5 #seg
prob_subida = 0.7
prob_bajada = 1-prob_subida
lambda_ =300 #seg
corte = 3600 #60 min

contador_pas = 1
dir = "sube"

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

def iniciar_simulacion():
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
    while reloj <= corte:
        if min(t_viaje,t_prox_llegada)== t_viaje: proximo_evento ="ascensor" 
        else: proximo_evento ="pasajero" 
        match proximo_evento:
            case "ascensor" :
                if dir == "sube":cola_actual=cola_sube
                else:cola_actual=cola_baja

                parar = asc.check_detenerse(cola_actual,reloj,t_prox_llegada,t_viaje,p)
                if parar == False:
                    reloj+= t_viaje
                    t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)
                    #cambio la direccion para proxima iteracion
                    if dir == "sube":
                        dir="baja"
                    else:
                        dir = "sube"
                else:
                    reloj+= t_viaje
                    #sumo al reloj el tiempo de bajada
                    reloj+= cal.calcular_bajada(p,d)
                    #limpio los pasajeros que bajan del ascensor y añado los nuevos
                    pasajeros_actual.clear()
                    pasajeros_actual=cal.cargar_ascensor(cola_actual,h)
                    p=len(pasajeros_actual)
                    #sumo al reloj el tiempo de subida de los pasajeros
                    reloj+=cal.calcular_subida(p,a)
                    #Recalculo la cola quitando los pasajeros que suben al ascensor
                    cola_actual=cal.recalcular_colas(cola_actual,pasajeros_actual)
                    #sumo al reloj el tiempo de espera de las puertas
                    #TODO:agregar pasajero nuevo a lista pasajeros actuales
                    reloj+=asc.espera_puertas(reloj,t_prox_llegada,e,a)

                    #cambio la direccion para proxima iteracion y reasigno la cola
                    if dir == "sube":
                        cola_sube=cola_actual
                        dir="baja"
                    else:
                        cola_baja=cola_actual
                        dir = "sube"
                    #calculo la proxima llegada del ascensor
                    t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)

            case "pasajero":
                reloj+=t_prox_llegada
                t_prox_llegada=cal.llgada_pasajero(lambda_)+reloj
                tmp_pasajero=psj.Pasajero(contador_pas,t_prox_llegada,d,a,random.random())
                if tmp_pasajero.dir_pas == "Sube": 
                    cola_sube.append(tmp_pasajero)
                else: cola_baja.append(tmp_pasajero)
                pasajeros_tot.append(tmp_pasajero)
    print(pasajeros_tot)
    for persona in pasajeros_tot:
        print(persona)

iniciar_simulacion()

