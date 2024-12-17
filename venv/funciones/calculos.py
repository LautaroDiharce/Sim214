import random
import numpy as np
import math
import clases.pasajero as psj


#anda bien
def calcular_viaje(a,b):
    rnd= random.random()
    #print(rnd)
    tiempo_viaje = a+rnd*(b-a)
    return tiempo_viaje

def calcular_pasajeros_bajan(a,b):
    rnd= random.random()
    #print(rnd)
    tiempo_viaje = round(a+rnd*(b-a))
    return tiempo_viaje


#revisar
def llgada_pasajero(lambda_):
    rnd= random.random()
    t_llegada = -(lambda_)*(math.log(1-rnd))
    #rint("random_lamda",rnd)
    #print(t_llegada)
    return t_llegada

  
def calcular_bajada(cant_pas_actual,d):
    return cant_pas_actual*d

def calcular_subida(cant_cola,a):
    return cant_cola*a

def cargar_ascensor(cola, h,p,hmax):
    pueden_subir=hmax-(h-p)
    if len(cola)>pueden_subir: 
        cola=cola[:pueden_subir]
    
    return cola

def recalcular_colas(cola_actual,pasajeros_actual):
    
    # Creando las listas de objetos
    lista1 = cola_actual
    lista2 = pasajeros_actual

    # Convirtiendo las listas en conjuntos (basados en el atributo 'nombre')
    conjunto1 = set(pasajero.id for pasajero in lista1)
    conjunto2 = set(pasajero.id for pasajero in lista2)
    print(conjunto1)
    print(conjunto2)
    # Calculando la diferencia de conjuntos (elementos en lista1 pero no en lista2)
    diferencia = conjunto1 - conjunto2
    print(diferencia)
    # Creando una nueva lista con los elementos restantes
    resultado = [pasajero for pasajero in lista1 if pasajero.id in diferencia]

    for pasajero in resultado:
        print(pasajero)
    return resultado

def espera_puertas(reloj, proximo_pas,t_puertas,A,h,hmax):
    espera = reloj +t_puertas
    print("espera",espera/60)
    print("prox_pas_espera_puertas",proximo_pas/60)
    add_pas = 0 
    if proximo_pas <= espera and h!=hmax:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        espera = proximo_pas+A+t_puertas
        add_pas = 1
    elif proximo_pas <= espera and h==hmax:
        add_pas=2
    return espera,add_pas