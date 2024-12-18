import clases.ascensor as ac
import clases.pasajero as psj
import funciones.calculos as cal
import random
#import interfaz.ui as ui

# P = pasajeros que descienden
# H = pasajeros totales
# D = segundos que toma al pasajero descender
# Dir = direccion del ascensor
# A = segundos que toma al pasajero ascender
# Hmax = capacidad maxima = 6
# E = tiempo de espera para cerrar puertas
# L = minutos entre arribo de pasajeros 70% baja #0% sube
# determinar el tiempo de permanencia del ascensor en el piso 15.
# H1 = 5 || Dir = up || Pas_sube_1 = 3 ||Pas_baja_1 =5

ascensor_a = 180 #3min
ascensor_b= 540 #9min
hmax=6
e=5 #seg
d=5 #seg
a=5 #seg
prob_subida = 0.7
prob_bajada = 1-prob_subida
lambda_ =300 #seg
corte = 5000 #60 min
contador_pas = 1

def pasajeros_iniciales(pasajeros_actual,h):
    global contador_pas
    while contador_pas <= h:
        pasajeros_actual.append(psj.Pasajero(contador_pas,0,d,a,0.5))
        contador_pas +=1
        ##print("ini_actual")
    #for pasajero in pasajeros_actual:
        #print(pasajero)
    return pasajeros_actual

def cola_sube_inicial(cola_sube,h,init_subida):
    global contador_pas
    while contador_pas <= h+init_subida:
        cola_sube.append(psj.Pasajero(contador_pas,0,d,a,0.5))
        contador_pas +=1
    return cola_sube

def cola_baja_inicial(cola_baja,h,init_subida,init_bajada):
    global contador_pas
    while contador_pas <= h+init_subida+init_bajada:
        cola_baja.append(psj.Pasajero(contador_pas,0,d,a,0.9))
        contador_pas +=1
    return cola_baja


def iniciar_simulacion(n_baja,n_sube,pas_actuales,iteraciones):
    reloj = 0.0
    h=int(pas_actuales)
    init_subida =int(n_sube)
    init_bajada = int(n_baja)
    p = cal.calcular_pasajeros_bajan(0,h)
    corte_i=int(iteraciones)
    cola_actual=[]
    cola_sube=[]
    cola_baja=[]
    vector=[]
    dir = "sube"
    asc=ac.Ascensor(hmax,h,e,dir)
    cola_actual=pasajeros_iniciales(cola_actual,h)
    cola_sube=cola_sube_inicial(cola_sube,h,init_subida)
    cola_baja=cola_baja_inicial(cola_baja,h,init_subida,init_bajada)
    pasajeros_tot=cola_actual+cola_sube+cola_baja  
    contador_pas = len(pasajeros_tot)
    t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)
    iteracion=0
    t_prox_llegada=cal.llgada_pasajero(lambda_)
    prox_asc=reloj+t_viaje
    proximo_pas=reloj+t_prox_llegada
    acumulador_permanencia=0
    while iteracion < corte_i:
    #while reloj <= corte:
        ##print("################################################################")
        ##print("cola sube pre calculo", len(cola_sube),"cola baja pre calculo", len(cola_baja))
        #print("iteracion",i)
        iteracion+=1
        ##print("Reloj" ,reloj/60)
        ##print("contador_pas",contador_pas)
        ##print("t_prox_llegada",proximo_pas/60)
        ##print("t_viaje",prox_asc/60)
        
        if min(prox_asc,proximo_pas)== prox_asc: proximo_evento ="ascensor" 
        else: proximo_evento ="pasajero" 
        #print(proximo_evento)
        match proximo_evento:
            case "ascensor" :
                #print("direccion del ascensor", dir)
                if dir == "sube":cola_actual=cola_sube
                else:cola_actual=cola_baja
                parar = asc.check_detenerse(len(cola_actual),reloj,t_prox_llegada,t_viaje,p)
                if parar == False:
                    reloj=prox_asc
                    t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)
                    #cambio la direccion para proxima iteracion
                    if dir == "sube":
                        dir="baja"
                    else:
                        dir = "sube"
                    prox_asc=reloj+t_viaje
                else:
                    reloj=prox_asc
                    #print("reloj1",reloj/60)
                    aux_permanencia_1=reloj
                    #print("van",h,"bajan",p)
                    #sumo al reloj el tiempo de bajada
                    reloj+= cal.calcular_bajada(p,d)
                    #print("bajan los vatos",reloj/60)
                    #calcular cuantos pasajeros nuevos suben
                    aux_pasajeros_suben=cal.cargar_ascensor(cola_actual,h,p,hmax)
                    h=h-p
                    #Recalculo la cantidad de pasajejos en el ascensor para dejar 6 maximo
                    p=len(aux_pasajeros_suben)
                    #for pasajero in aux_pasajeros_suben:
                        #print(pasajero)
                    #print("suben",p)
                    h=h+p
                    #print("ahora van",h)
                    #sumo al reloj el tiempo de subida de los pasajeros
                    reloj+=cal.calcular_subida(p,a)
                    #print("suben los vatos",reloj/60)
                    #Recalculo la cola quitando los pasajeros que suben al ascensor
                    #print("cola antes de subir",len(cola_actual))
                    cola_actual=cal.recalcular_colas(cola_actual,aux_pasajeros_suben)
                    #print("cola despues de subir",len(cola_actual))
                    #for pasajero in aux_pasajeros_suben:
                        #print(pasajero)
                    #sumo al reloj el tiempo de espera de las puertas
                    tmp_res=cal.espera_puertas(reloj,proximo_pas,e,a,h,hmax)
                    reloj=tmp_res[0]
                    #print("cierran las puertas",reloj/60)
                    #reasigno las colas quitando a quien subio al ascensor
                    if dir == "sube":
                        cola_sube.clear()
                        cola_sube=cola_actual
                        dir="baja"
                    else:
                        cola_baja=cola_actual
                        cola_baja.clear()
                        dir = "sube"
                    #si llego un pasajero antes de cerrar, lo agrego a la cola
                    match tmp_res[1]:
                        case 2:
                            contador_pas+=1
                            tmp_pasajero=psj.Pasajero(contador_pas,proximo_pas,d,a,random.random())
                            if tmp_pasajero.dir_pas == "Sube": 
                                cola_sube.append(tmp_pasajero)
                            else: cola_baja.append(tmp_pasajero)
                            pasajeros_tot.append(tmp_pasajero)
                            t_prox_llegada=cal.llgada_pasajero(lambda_)
                            proximo_pas=reloj+t_prox_llegada
                        case 1:
                            #print("wachin con lo justo--------------------")
                            #print("cola sube", len(cola_sube),"cola baja ", len(cola_baja))
                            contador_pas+=1
                            tmp_pasajero=psj.Pasajero(contador_pas,proximo_pas,d,a,random.random())
                            if tmp_pasajero.dir_pas.lower() == dir.lower(): 
                                #añadir al ascensor
                                h+=1
                                pasajeros_tot.append(tmp_pasajero)
                            else:
                                #añadir a la cola (contraria a la actual)
                                if tmp_pasajero.dir_pas == "Sube": 
                                    cola_baja.append(tmp_pasajero)
                                else: cola_sube.append(tmp_pasajero)
                            #print("cola sube", len(cola_sube),"cola baja ", len(cola_baja))
                            #print("wachin con lo justo--------------------")
                    ##print("cola sube", len(cola_sube),"cola baja ", len(cola_baja))
                    #auxiliar para fin de permanencia en el piso
                    aux_permanencia_2=reloj
                    acumulador_permanencia+=aux_permanencia_2-aux_permanencia_1
                    #cambio la direccion para proxima iteracion y reasigno la cola

                    #print("cola sube", len(cola_sube),"cola baja ", len(cola_baja))
                    #calculo la proxima llegada del ascensor
                    t_viaje=cal.calcular_viaje(ascensor_a,ascensor_b)
                    prox_asc=reloj+t_viaje
                    #reinicio las variables de pasajeros del ascensor
                    cola_actual.clear()
                    h=cal.calcular_pasajeros_bajan(0,hmax)
                    p = cal.calcular_pasajeros_bajan(0,h)
            case "pasajero":
                reloj=proximo_pas
                contador_pas+=1          
                tmp_pasajero=psj.Pasajero(contador_pas,proximo_pas,d,a,random.random())
                t_prox_llegada=cal.llgada_pasajero(lambda_)
                
                if tmp_pasajero.dir_pas == "Sube": 
                    cola_sube.append(tmp_pasajero)
                else: cola_baja.append(tmp_pasajero)
                #print("direccion del pasajero",tmp_pasajero.dir_pas)
                #print("cola sube", len(cola_sube),"cola baja ", len(cola_baja))
                pasajeros_tot.append(tmp_pasajero)
                proximo_pas=reloj+t_prox_llegada
        #mandar aca el vector
        vector.append([iteracion,round(reloj/60,2),proximo_evento,dir,len(cola_sube),len(cola_baja),h,p,round(acumulador_permanencia/60,2),len(pasajeros_tot)])
    # for valor in vector:
    #     print(valor)
    #print(vector)
    #print(reloj/60)
    #print("permanencia", acumulador_permanencia/60)
    #ui.agregar_elemento_a_grid([reloj,acumulador_permanencia])
    return vector

#iniciar_simulacion()


