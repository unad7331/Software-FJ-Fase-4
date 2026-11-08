
"""
Modulo de servicios especializados de Software FJ.
Incluye abstraccion, herencia y polimorfismo.
"""

from abc import ABC, abstractmethod
from entidades import EntidadSistema
from excepciones import ErrorServicio, ErrorValidacion


class Servicio(EntidadSistema, ABC):
    """Clase abstracta para los servicios de la empresa."""

    def __init__(self, identificador, nombre, precio_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)):
            raise ErrorValidacion("El precio debe ser numerico.")

        if precio_base <= 0:
            raise ErrorServicio("El precio debe ser mayor que cero.")

        self._nombre = nombre.strip()
        self._precio_base = float(precio_base)
        self._disponible = True

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible

    def cambiar_disponibilidad(self, estado):
        if not isinstance(estado, bool):
            raise ErrorValidacion("La disponibilidad debe ser verdadera o falsa.")
        self._disponible = estado

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ErrorServicio("El servicio no esta disponible.")

    def calcular_total(self, cantidad, impuesto=0, descuento=0):
        """Calcula el costo aplicando impuestos y descuentos opcionales."""

        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)):
            raise ErrorValidacion("La cantidad debe ser numerica.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise ErrorValidacion("El impuesto debe ser numerico.")

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise ErrorValidacion("El descuento debe ser numerico.")

        if cantidad <= 0:
            raise ErrorServicio("La cantidad debe ser mayor que cero.")

        if not 0 <= impuesto <= 100:
            raise ErrorServicio("El impuesto debe estar entre 0 y 100.")

        if not 0 <= descuento <= 100:
            raise ErrorServicio("El descuento debe estar entre 0 y 100.")

        subtotal = self.calcular_costo(cantidad)
        valor_descuento = subtotal * descuento / 100
        base = subtotal - valor_descuento
        total = base + (base * impuesto / 100)

        return round(total, 2)

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def obtener_descripcion(self):
        return self.describir_servicio()


class ReservaSala(Servicio):
    """Servicio de reserva de salas por horas."""

    def __init__(self, identificador, nombre, precio_base, capacidad):
        super().__init__(identificador, nombre, precio_base)

        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise ErrorServicio("La capacidad debe ser un entero positivo.")

        self.capacidad = capacidad

    def validar_parametros(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ErrorServicio("Las horas de reserva deben ser positivas.")

        self.validar_disponibilidad()
        return True

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)
        return round(self.precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"Reserva de sala: {self.nombre}. "
            f"Capacidad: {self.capacidad} personas. "
            f"Precio por hora: ${self.precio_base}"
        )


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos por dias."""

    def __init__(self, identificador, nombre, precio_base, unidades):
        super().__init__(identificador, nombre, precio_base)

        if isinstance(unidades, bool) or not isinstance(unidades, int) or unidades <= 0:
            raise ErrorServicio("Las unidades deben ser un entero positivo.")

        self.unidades = unidades

    def validar_parametros(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ErrorServicio("Los dias de alquiler deben ser enteros positivos.")

        self.validar_disponibilidad()
        return True

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)
        return round(self.precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"Alquiler de equipo: {self.nombre}. "
            f"Unidades disponibles: {self.unidades}. "
            f"Precio por dia: ${self.precio_base}"
        )


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria especializada por horas."""

    def __init__(self, identificador, nombre, precio_base, especialidad):
        super().__init__(identificador, nombre, precio_base)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ErrorServicio("Debe indicar la especialidad.")

        self.especialidad = especialidad.strip()

    def validar_parametros(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ErrorServicio("Las horas de asesoria deben ser positivas.")

        self.validar_disponibilidad()
        return True

    def calcular_costo(self, cantidad):
        self.validar_parametros(cantidad)
        return round(self.precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"Asesoria especializada: {self.nombre}. "
            f"Especialidad: {self.especialidad}. "
            f"Precio por hora: ${self.precio_base}"
        )
      
