
"""
Modulo de registro de eventos y errores
del sistema Software FJ.
"""

import logging
import os


# Crear carpeta de registros si no existe.
os.makedirs("logs", exist_ok=True)


# Configuracion del sistema de registro.
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    force=True
)


class LoggerSistema:
    """
    Clase encargada de registrar los eventos
    y errores que ocurren en Software FJ.
    """

    @staticmethod
    def registrar_evento(mensaje):
        """Registra un evento informativo."""

        logging.info(mensaje)

    @staticmethod
    def registrar_advertencia(mensaje):
        """Registra una advertencia."""

        logging.warning(mensaje)

    @staticmethod
    def registrar_error(mensaje):
        """Registra un error."""

        logging.error(mensaje)

    @staticmethod
    def registrar_excepcion(mensaje):
        """Registra un error con informacion de la excepcion."""

        logging.exception(mensaje)
      
