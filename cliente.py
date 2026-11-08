
"""
Modulo para la gestion de clientes de Software FJ.
"""

import re
from entidades import EntidadSistema
from excepciones import ErrorCliente, ErrorValidacion


class Cliente(EntidadSistema):
    """
    Representa un cliente registrado en el sistema.
    """

    def __init__(self, identificador, nombre, correo, telefono):

        super().__init__(identificador)

        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ErrorCliente(
                "El nombre del cliente es obligatorio."
            )

        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str):
            raise ErrorValidacion(
                "El correo debe ser texto."
            )

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, valor.strip()):
            raise ErrorCliente(
                "El correo electronico no es valido."
            )

        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str):
            raise ErrorValidacion(
                "El telefono debe ingresarse como texto."
            )

        numero = valor.strip()

        if not numero.isdigit() or not 7 <= len(numero) <= 15:
            raise ErrorCliente(
                "El telefono debe contener entre 7 y 15 digitos."
            )

        self._telefono = numero

    def obtener_descripcion(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}"
        )

    def __str__(self):
        return self.obtener_descripcion()

  
