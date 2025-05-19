"""
---- Información ----

En este archivo se almacenan todas las funciones que permiten que el aplicativo funcione.
Para garantizar su funcionamiento, lo primero que hacemos es importar todos los objetos y el logger.
"""

from models.mascota import Mascota
from models.dueno import Dueno
from models.consulta import Consulta
from config.logging_config import logger

"""
A. La función crear_mascota registra nuevas mascotas y las relaciona con sus dueños.
B. La función crear_consulta registra una nueva consulta veterinaria asociada a una mascota específica.
C. La función listar_mascotas muestra toda la información de las mascotas y sus respectivos dueños.
D. La función mostrar_historial muestra todas las consultas que se han realizado a una mascota específica.
E. La función menu imprime el menú con el que va a interactuar el usuario.

- Todas estas funciones serán llamadas desde el archivo main.py.
"""

# A
def crear_mascota(mascotas, duenos):
    """
    0. Se usa un bloque try para capturar errores.
    1. Se solicita al usuario la información básica de la mascota.
    2. Se verifica si el dueño ya está registrado mediante su documento.
    3. Si ya está registrado, se recupera su información.
    4. Se registra un log indicando que se usará un dueño ya existente.
    5. Si el dueño no está registrado, se pide su información.
    6. Se crea el objeto Dueno con los datos ingresados.
    7. Se guarda el objeto Dueno en el diccionario de dueños.
    8. Se crea el objeto Mascota y se almacena en el diccionario de mascotas.
    9. Si ocurre un error, se registra y se notifica al usuario.
    """
    try:
        # 1
        nombre_mascota = input("Nombre de la mascota: ")
        especie_mascota = input("Especie: ")
        raza_mascota = input("Raza: ")
        edad_mascota = input("Edad: ")
        documento_dueno = input("\nDocumento del dueño: ").strip()
        
        # 2
        if documento_dueno in duenos:
            # 3
            print("\nEl dueño ya se encuentra registrado en nuestra base de datos, se usará su información.")
            dueno = duenos[documento_dueno]
            # 4
            logger.info(f"La mascota {nombre_mascota} fue asignada a un dueño ya existente ({dueno.nombre}).")
        else:
            # 5
            print("\nRegistrando un nuevo dueño en la base de datos...")
            nombre_dueno = input("Nombre del dueño: ")
            telefono_dueno = input("Teléfono: ")
            direccion_dueno = input("Dirección: ")
            # 6
            dueno = Dueno(nombre_dueno, telefono_dueno, direccion_dueno, documento_dueno)
            # 7
            duenos[documento_dueno] = dueno
        
        # 8
        nueva_mascota = Mascota(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, dueno)
        mascotas[nombre_mascota] = nueva_mascota
        print(f"\nLa mascota {nombre_mascota} fue agregada correctamente ✓")
    except Exception as e:
        # 9
        logger.error(f"Ha ocurrido un error registrando una nueva mascota o dueño: {e}")
        print("Ha ocurrido un error llenando la información del formulario. Intente de nuevo.")

# B
def crear_consulta(mascotas, consultas):
    """
    1. Se solicita el nombre de la mascota para registrar la consulta.
    2. Se verifica si la mascota está registrada.
    3. Si está registrada, se solicita la información de la consulta.
    4. Se crea un objeto Consulta y se agrega a la lista de consultas.
    5. Se informa al usuario del registro exitoso.
    6. Si ocurre un error, se captura y se registra.
    """
    try:
        # 1
        nombre_mascota = input("Nombre de la mascota: ")
        # 2
        if nombre_mascota not in mascotas:
            print(f"\nNo se encontró una mascota registrada con el nombre {nombre_mascota}.")
            logger.warning(f"Cuidado, intento de buscar mascota {nombre_mascota} sin nombre registrado.")
            return
        
        # 3
        fecha = input("Fecha (dd/mm/aaaa): ")
        motivo = input("Motivo de la visita: ")
        diagnostico = input("¿Qué síntomas tiene?: ")
        consulta = Consulta(fecha, motivo, diagnostico, mascotas[nombre_mascota])
        # 4
        consultas.append(consulta)
        print(f"Consulta registrada correctamente para {nombre_mascota} ✓")
    except Exception as e:
        # 6
        logger.error(f"Error al registrar consulta: {e}")

# C
def listar_mascotas(mascotas):
    """
    1. Verifica si hay mascotas registradas.
    2. Si hay, las imprime con su información.
    3. Si no hay, informa al usuario y registra el intento.
    4. Captura cualquier error en el proceso.
    """
    try:
        if not mascotas:
            print("No hay mascotas registradas.")
            logger.info("Intento de listar mascotas sin haber registrado ninguna.")
            return
        for mascota in mascotas.values():
            print(f"\n- {mascota}")
        logger.info("Mascotas listadas con éxito.")
    except Exception as e:
        logger.error(f"Error al listar las mascotas: {e}")

# D
def mostrar_historial(mascotas, consultas):
    """
    1. Verifica si hay mascotas registradas.
    2. Pide al usuario el nombre de una mascota.
    3. Busca en las consultas las que correspondan a esa mascota.
    4. Si no hay historial, informa al usuario.
    5. Si hay, imprime el historial.
    6. Captura errores en el proceso.
    """
    try:
        # 1
        if not mascotas:
            print("No hay mascotas registradas.")
            logger.warning("No hay mascota registrada.")
            return

        # 2
        nombre_mascota = input("Ingrese el nombre de la mascota: ").strip().capitalize()
        if nombre_mascota not in mascotas:
            print("Mascota no encontrada.")
            logger.warning("Cuidado, nombre de mascota no encontrado.")
            return

        # 3
        historial = []
        for consulta in consultas:
            if consulta.mascota.nombre == nombre_mascota:
                historial.append(consulta)

        # 4
        if not historial:
            print("No hay un historial para esta mascota registrado.")
            logger.warning(f"Mascota {nombre_mascota} sin historial registrado.")
            return

        # 5
        print(f"El historial de {nombre_mascota} es el siguiente:\n")
        for consulta in historial:
            print(f"- {consulta}")
    except Exception as e:
        # 6
        logger.error(f"Error al mostrar historial: {e}")

# E
def menu():
    """
    Imprime el menú principal de opciones del sistema para que el usuario pueda seleccionar una acción.
    """
    print(  "\n ============================================\n " \
            "------------------- MENU -------------------\n " \
            "============================================\n")
    print("Bienvenido al sistema gestor de la clínica veterinaria Amigos Peludos. ¿Qué desea hacer?")
    print("1. Registrar mascota")
    print("2. Registrar consulta")
    print("3. Listar mascotas")
    print("4. Ver historial de consultas de una mascota")
    print("5. Salir de la aplicación")
