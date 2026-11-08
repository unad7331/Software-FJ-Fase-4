
"""
Modulo para gestionar las reservas de Software FJ.
"""

from datetime import datetime
from cliente import Cliente
from servicios import Servicio
from excepciones import (
    ErrorReserva,
    ErrorValidacion,
    ReservaNoPermitida,
    ServicioNoDisponible
)


class Reserva:
    """
    Gestiona las reservas de clientes y servicios.
    """

    ESTADOS_VALIDOS = (
        "Pendiente",
        "Confirmada",
        "Cancelada"
    )

    def __init__(self, identificador, cliente, servicio, duracion):

        if not isinstance(identificador, str) or not identificador.strip():
            raise ErrorValidacion(
                "El identificador de reserva es obligatorio."
            )

        if not isinstance(cliente, Cliente):
            raise ErrorValidacion(
                "Debe proporcionar un cliente valido."
            )

        if not isinstance(servicio, Servicio):
            raise ErrorValidacion(
                "Debe proporcionar un servicio valido."
            )

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorValidacion(
                "La duracion debe ser numerica."
            )

        if duracion <= 0:
            raise ErrorReserva(
                "La duracion debe ser mayor que cero."
            )

        servicio.validar_parametros(duracion)

        self._identificador = identificador.strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha_creacion = datetime.now()
        self._fecha_confirmacion = None

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    def calcular_costo(self, impuesto=0, descuento=0):
        """Calcula el costo total de la reserva."""

        if self.estado == "Cancelada":
            raise ReservaNoPermitida(
                "No se puede calcular una reserva cancelada."
            )

        return self.servicio.calcular_total(
            self.duracion,
            impuesto,
            descuento
        )

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.estado != "Pendiente":
            raise ReservaNoPermitida(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.servicio.validar_parametros(self.duracion)

            self._estado = "Confirmada"
            self._fecha_confirmacion = datetime.now()

            return (
                f"Reserva {self.identificador} confirmada correctamente."
            )

        except ServicioNoDisponible as error:
            raise ReservaNoPermitida(
                "No se puede confirmar: servicio no disponible."
            ) from error

        except Exception as error:
            raise ReservaNoPermitida(
                "Ocurrio un error al confirmar la reserva."
            ) from error

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.estado == "Cancelada":
            raise ReservaNoPermitida(
                "La reserva ya se encuentra cancelada."
            )

        self._estado = "Cancelada"

        return (
            f"Reserva {self.identificador} cancelada correctamente."
        )

    def procesar(self):
        """Procesa la reserva y devuelve su informacion."""

        try:
            if self.estado == "Cancelada":
                raise ReservaNoPermitida(
                    "No se puede procesar una reserva cancelada."
                )

            costo = self.calcular_costo()

            return {
                "reserva": self.identificador,
                "cliente": self.cliente.nombre,
                "servicio": self.servicio.nombre,
                "duracion": self.duracion,
                "estado": self.estado,
                "costo": costo
            }

        except ReservaNoPermitida:
            raise

        except Exception as error:
            raise ErrorReserva(
                "Error durante el procesamiento de la reserva."
            ) from error

    def __str__(self):
        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )

  
