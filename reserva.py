from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente == "":
                raise ValueError("Cliente invalido")

            if not isinstance(servicio, Servicio):
                raise TypeError("Servicio invalido")

            if horas <= 0:
                raise ValueError("Horas invalidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:
            raise Exception(f"Error al crear reserva: {e}")
from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente == "":
                raise ValueError("Cliente invalido")

            if not isinstance(servicio, Servicio):
                raise TypeError("Servicio invalido")

            if horas <= 0:
                raise ValueError("Horas invalidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:
            raise Exception(f"Error al crear reserva: {e}")

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):
        costo = self.servicio.calcular_costo(self.horas)
        return costo