
"""
Excepciones personalizadas del sistema Software FJ.
"""


class ErrorSistema(Exception):
    """Excepcion general del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error cuando los datos ingresados no son validos."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con la gestion de clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con la gestion de servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con las reservas."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Error cuando un servicio no esta disponible."""
    pass


class ReservaNoPermitida(ErrorReserva):
    """Error cuando una reserva no puede realizarse."""
    pass


