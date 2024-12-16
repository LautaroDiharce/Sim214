class Ascensor:
  def __init__(self, Capacidad, Cant_pas_actual, E,Direccion):
    self.capacidad= Capacidad
    self.cant_actual= Cant_pas_actual
    self.e = E
    self.dir=Direccion
    self.Acum_permanencia = 0

  def check_detenerse(cola, reloj, t_prox_pas,t_ascensor,Cant_pas_actual):
    if cola == 0 and  Cant_pas_actual==0 and reloj+t_prox_pas >= reloj+t_ascensor: stop = False
    else: stop=True
    return stop

  def espera_puertas(reloj, t_prox_pas,t_puertas,A):
    espera = t_puertas  
    if reloj + t_prox_pas <= reloj + espera:
      espera = t_prox_pas+A+ t_puertas

    return espera

  def __str__(self):
      return f"Ascensor (Capacidad: {self.capacidad}, Cantidad actual de pasajeros: {self.cant_actual}, Dirección: {self.dir})"

