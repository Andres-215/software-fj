# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# =========================================
# CLASE ABSTRACTA SERVICIO
# =========================================

# Esta clase representa un servicio general
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre, precio_base):

        # Validamos que el precio sea correcto
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        # Atributos del servicio
        self.nombre = nombre
        self.precio_base = precio_base

    # Método abstracto
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto
    @abstractmethod
    def descripcion(self):
        pass

# =========================================
# CLASE RESERVA DE SALA
# =========================================

# Esta clase hereda de Servicio
class ReservaSala(Servicio):

    # Método para calcular el costo
    def calcular_costo(self, horas):

        # Validamos las horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        # Calculamos el total
        total = self.precio_base * horas

        return total

    # Método descripción
    def descripcion(self):

        return f"Servicio de reserva de sala: {self.nombre}"