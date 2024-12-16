import random
import numpy as np
import math


#anda bien
def calcular_viaje(a,b):
    rnd= random.random()
    print(rnd)
    tiempo_viaje = a+rnd*(b-a)
    return tiempo_viaje


#revisar
def llgada_pasajero(lambda_):
    rnd= random.random()
    lambda_=300
    t_llegada = -(1/lambda_)*(math.log(1-rnd))
    print(t_llegada)
    return t_llegada

  
def calcular_bajada(cant_pas_actual,d):
    return cant_pas_actual*d

def calcular_subida(cant_cola,a):
    return cant_cola*a

def cargar_ascensor(cola, h)
    if len(cola)>h: 
        cola=cola[:h]
    return cola

def recalcular_colas(cola_actual,pasajeros_actual):
    
    # Creando las listas de objetos
    lista1 = pasajeros_actual
    lista2 = cola_actual

    # Convirtiendo las listas en conjuntos (basados en el atributo 'nombre')
    conjunto1 = set(pasajero.id for pasajero in lista1)
    conjunto2 = set(pasajero.id for pasajero in lista2)

    # Calculando la diferencia de conjuntos (elementos en lista1 pero no en lista2)
    #TODO: revisar cosistencia de la diferencia
    diferencia = conjunto1 - conjunto2
    #print(diferencia)
    # Creando una nueva lista con los elementos restantes
    resultado = [pasajero for pasajero in lista1 if pasajero.id in diferencia]

    #for persona in resultado:
    #    print(persona)
    return resultado