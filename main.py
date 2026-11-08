"""
PROYECTO SOFTWARE FJ
Sistema Integral de Gestion de Clientes,
Servicios y Reservas.

Curso: Programacion 213023
UNAD - Fase 4
"""

from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import (
    ErrorSistema,
    ErrorCliente,
    ErrorServicio,
    ErrorReserva
)
from logger import LoggerSistema


# Listas internas para almacenar la informacion.
clientes = []
servicios = []
reservas = []


def mostrar_titulo():
    print("=" * 65)
    print("       SISTEMA INTEGRAL DE GESTION SOFTWARE FJ")
    print("=" * 65)


def registrar_cliente(identificador, nombre, correo, telefono):
    """Registra un cliente y controla posibles errores."""

    try:
        cliente = Cliente(
            identificador,
            nombre,
            correo,
            telefono
        )

        clientes.append(cliente)

        LoggerSistema.registrar_evento(
            f"Cliente registrado: {cliente.nombre}"
        )

        print("Cliente registrado correctamente.")
        print(cliente)

        return cliente

    except ErrorCliente as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error de cliente: {error}")

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error del sistema: {error}")

    except Exception as error:
        LoggerSistema.registrar_excepcion(
            "Error inesperado al registrar cliente."
        )
        print(f"Error inesperado: {error}")

    return None


def registrar_servicio(servicio):
    """Registra un servicio y valida su informacion."""

    try:
        servicios.append(servicio)

        LoggerSistema.registrar_evento(
            f"Servicio registrado: {servicio.nombre}"
        )

        print("Servicio registrado correctamente.")
        print(servicio.describir_servicio())

        return servicio

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error al registrar servicio: {error}")

    except Exception:
        LoggerSistema.registrar_excepcion(
            "Error inesperado al registrar servicio."
        )
        print("Se produjo un error inesperado.")

    return None


def crear_reserva(identificador, cliente, servicio, duracion):
    """Crea una reserva y controla errores."""

    try:
        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion
        )

        reservas.append(reserva)

        LoggerSistema.registrar_evento(
            f"Reserva creada: {identificador}"
        )

        print("Reserva creada correctamente.")
        print(reserva)

        return reserva

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error al crear reserva: {error}")

    except Exception:
        LoggerSistema.registrar_excepcion(
            "Error inesperado al crear reserva."
        )
        print("No fue posible crear la reserva.")

    return None


def ejecutar_pruebas():
    """
    Ejecuta diez operaciones para demostrar
    el funcionamiento del sistema.
    """

    mostrar_titulo()

    print("\nOPERACION 1: Registro de cliente valido")

    cliente1 = registrar_cliente(
        "C001",
        "Carlos Rodriguez",
        "carlos@gmail.com",
        "3101234567"
    )

    print("\nOPERACION 2: Registro de cliente invalido")

    registrar_cliente(
        "C002",
        "Maria Lopez",
        "correo_incorrecto",
        "3109876543"
    )

    print("\nOPERACION 3: Creacion de servicio de sala")

    sala = None

    try:
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            50000,
            20
        )

        registrar_servicio(sala)

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error: {error}")

    print("\nOPERACION 4: Creacion de servicio de equipos")

    equipo = None

    try:
        equipo = AlquilerEquipo(
            "S002",
            "Computador portatil",
            80000,
            10
        )

        registrar_servicio(equipo)

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error: {error}")

    print("\nOPERACION 5: Creacion de asesoria especializada")

    asesoria = None

    try:
        asesoria = AsesoriaEspecializada(
            "S003",
            "Asesoria tecnologica",
            100000,
            "Ingenieria de sistemas"
        )

        registrar_servicio(asesoria)

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error: {error}")

    print("\nOPERACION 6: Creacion de servicio incorrecto")

    try:
        servicio_invalido = ReservaSala(
            "S004",
            "Sala incorrecta",
            -5000,
            0
        )

        registrar_servicio(servicio_invalido)

    except ErrorSistema as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Error controlado: {error}")

    print("\nOPERACION 7: Creacion de reserva valida")

    reserva1 = None

    if cliente1 is not None and sala is not None:
        reserva1 = crear_reserva(
            "R001",
            cliente1,
            sala,
            3
        )

    print("\nOPERACION 8: Creacion de reserva incorrecta")

    if cliente1 is not None and sala is not None:
        crear_reserva(
            "R002",
            cliente1,
            sala,
            -2
        )

    print("\nOPERACION 9: Confirmacion de reserva")

    if reserva1 is not None:
        try:
            resultado = reserva1.confirmar()
            LoggerSistema.registrar_evento(resultado)
            print(resultado)

        except ErrorSistema as error:
            LoggerSistema.registrar_error(str(error))
            print(f"Error: {error}")

    print("\nOPERACION 10: Cancelacion de reserva")

    if reserva1 is not None:
        try:
            resultado = reserva1.cancelar()
            LoggerSistema.registrar_evento(resultado)
            print(resultado)

        except ErrorSistema as error:
            LoggerSistema.registrar_error(str(error))
            print(f"Error: {error}")

    # Ejemplo de try, except, else y finally.
    print("\nPRUEBA DE MANEJO DE EXCEPCIONES")

    try:
        resultado = 100 / 5

    except ZeroDivisionError as error:
        LoggerSistema.registrar_error(str(error))
        print("No se puede dividir entre cero.")

    else:
        print(f"Calculo realizado correctamente: {resultado}")

    finally:
        print("Finalizo la prueba de excepciones.")

    # Ejemplo de encadenamiento de excepciones.
    print("\nPRUEBA DE ENCADENAMIENTO DE EXCEPCIONES")

    try:
        try:
            int("dato incorrecto")

        except ValueError as error:
            raise ErrorReserva(
                "No fue posible convertir el dato."
            ) from error

    except ErrorReserva as error:
        LoggerSistema.registrar_error(str(error))
        print(f"Excepcion controlada: {error}")

    # Resumen general del sistema.
    print("\n" + "=" * 65)
    print("RESUMEN GENERAL DEL SISTEMA")
    print("=" * 65)

    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    print("\nEventos y errores registrados en logs/sistema.log")

    LoggerSistema.registrar_evento(
        "Finalizacion de las pruebas del sistema Software FJ."
    )

    print("\nSISTEMA SOFTWARE FJ FINALIZADO")
    print("=" * 65)


if __name__ == "__main__":
    ejecutar_pruebas()
  
