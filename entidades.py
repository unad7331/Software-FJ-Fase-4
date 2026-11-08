
from abc import ABC, abstractmethod
from datetime import datetime
from excepciones import ErrorValidacion


class EntidadSistema(ABC):
    """
    Clase abstracta que representa las entidades
    generales del sistema Software FJ.
    """

    def __init__(self, identificador):
        if not isinstance(identificador, str):
            raise ErrorValidacion(
                "El identificador debe ser texto."
            )

        if not identificador.strip():
            raise ErrorValidacion(
                "El identificador no puede estar vacio."
            )

        self._identificador = identificador.strip()
        self._fecha_registro = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @abstractmethod
    def obtener_descripcion(self):
        """
        Metodo abstracto que deben implementar
        las clases derivadas.
        """
        pass

    def mostrar_informacion(self):
        return (
            f"Identificador: {self.identificador} | "
            f"Fecha de registro: "
            f"{self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')}"
        )

  
