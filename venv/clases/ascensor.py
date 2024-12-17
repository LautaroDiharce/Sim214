class Ascensor:
  def __init__(self, Capacidad, Cant_pas_actual, E,Direccion):
    self.capacidad= Capacidad
    self.cant_actual= Cant_pas_actual
    self.e = E
    self.dir=Direccion
    self.Acum_permanencia = 0

  def check_detenerse(self,cola_actual, reloj, t_prox_pas,t_ascensor,Cant_pas_actual_bajan):
    if cola_actual== 0 and  Cant_pas_actual_bajan==0 and reloj+t_prox_pas >= reloj+t_ascensor: stop = False
    else: stop=True
    return stop

  def espera_puertas(self,reloj, t_prox_pas,t_puertas,A):
    espera = t_puertas
    add_pas = False 
    if reloj + t_prox_pas <= reloj + espera:
        espera = t_prox_pas+A+ t_puertas
        add_pas = True


    return espera,add_pas

  def __str__(self):
      return f"Ascensor (Capacidad: {self.capacidad}, Cantidad actual de pasajeros: {self.cant_actual}, Dirección: {self.dir})"

