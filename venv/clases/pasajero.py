import random

class Pasajero:
    def direccion(self,rnd_dir):
        rnd = random.random()
        return "Sube" if rnd_dir <= 0.7 else "Baja"

    def __init__(self, id, hs_llegada, D, A,rnd_dir,estado='Espera'):
        #direccion=direccion()
        self.id = id
        self.hs_llegada = hs_llegada
        self.d = D
        self.a = A
        self.dir_pas = self.direccion(rnd_dir)  # Calculamos la dirección al crear el objeto
        self.estado = estado


    def __str__(self):
        return f"Pasajero (ID: {self.id}, Hora de llegada: {self.hs_llegada}, Dirección: {self.dir_pas})"

