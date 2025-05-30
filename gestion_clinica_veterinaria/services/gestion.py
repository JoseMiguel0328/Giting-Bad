"""
---- Información ----

En este archivo se almacenan todas las funciones que permiten que el aplicativo funcione.
Para garantizar su funcionamiento, lo primero que hacemos es importar todos los objetos y el logger.
"""

import csv  
import os   
from models.mascota import Mascota 
from models.dueno import Dueno     
from models.consulta import Consulta  
from config.logging_config import logger  
from exceptions.errores import ErrorBase  


"""
A. La función crear_mascota registra nuevas mascotas y las relaciona con sus dueños.
B. La función crear_consulta registra una nueva consulta veterinaria asociada a una mascota específica.
C. La función listar_mascotas muestra toda la información de las mascotas y sus respectivos dueños.
D. La función mostrar_historial muestra todas las consultas que se han realizado a una mascota específica.
E. La función menu imprime el menú con el que va a interactuar el usuario.
- Todas estas funciones serán llamadas desde el archivo main.py.
"""


RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), '..', 'data', 'mascotas_duenos.csv')

def mostrar_mascotas_csv(mascotas, duenos):
    """
    1. Lee el archivo CSV y carga las mascotas y dueños en los diccionarios correspondientes.
    2. Si el archivo no existe, informa al usuario.
    3. Se crea la mascota y se añade al diccionario.
    4. Se muestra un resumen de mascotas y dueños cargados.
    5. En caso de error, captura la excepción e informa.
    
    """
    try:
        with open(RUTA_ARCHIVO, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                print("fila csv:", fila)  # 1

                nombre_mascota = fila[0]
                especie = fila[1]
                raza = fila[2]
                edad = fila[3]

                nombre_dueno = fila[4]
                telefono = fila[5]
                direccion = fila[6]
                documento = fila[7]

                # 2
                if documento not in duenos:
                    dueno = Dueno(nombre_dueno, telefono, direccion, documento)
                    duenos[documento] = dueno
                else:
                    dueno = duenos[documento]

                # 3. 
                mascota = Mascota(nombre_mascota, especie, raza, edad, dueno)
                mascotas[nombre_mascota] = mascota

        print("Datos cargados correctamente desde el archivo CSV.")
        logger.info("Se cargo la información orrectamente")

        print("\nListado de mascotas cargadas:")
        # 4
        for nombre, mascota in mascotas.items():
            print(f"- Mascota: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
            dueno = mascota.dueno
            print(f"  Dueño: {dueno.nombre}, Tel: {dueno.telefono}, Dirección: {dueno.direccion}, Documento: {dueno.documento}")

    except FileNotFoundError:
        # 5
        print(f"Archivo {RUTA_ARCHIVO} no encontrado.")
        logger.warning(f"No se encontro información en {RUTA_ARCHIVO}")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")
        logger.error(f"Ha habido un problema cargando la información{e}")


def crear_mascota(mascotas, duenos):
    """
    A. Registra una nueva mascota y su dueño si no existe.
    1. Crea el directorio data si no existe para guardar el archivo CSV.
    2. Obtiene la ruta del archivo CSV para añadir la nueva mascota.
    3. Solicita datos de la mascota y dueño.
    4. Valida si el dueño ya está registrado para evitar duplicados.
    5. Agrega la nueva mascota y guarda la información en el archivo CSV.
    6. Captura errores específicos de validación.
    """
    # 1
    csv_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(csv_dir, exist_ok=True) 

    # 2
    csv_mascota_file = os.path.join(csv_dir, 'mascotas_duenos.csv')

    try:
        # 3
        nombre_mascota = input("Nombre de la mascota: ")
        especie_mascota = input("Especie: ")
        raza_mascota = input("Raza: ")
        edad_mascota = input("Edad: ")
        documento_dueno = input("\nDocumento del dueño: ").strip()
        
        # 4
        if documento_dueno in duenos:
            print("\nEl dueño ya se encuentra registrado en nuestra base de datos, se usará su información.")
            dueno = duenos[documento_dueno]
            logger.info(f"La mascota {nombre_mascota} fue asignada a un dueño ya existente ({dueno.nombre}).")
        else:
            print("\nRegistrando un nuevo dueño en la base de datos...")
            nombre_dueno = input("Nombre del dueño: ")
            telefono_dueno = input("Teléfono: ")
            direccion_dueno = input("Dirección: ")
            dueno = Dueno(nombre_dueno, telefono_dueno, direccion_dueno, documento_dueno)
            duenos[documento_dueno] = dueno
        
        nueva_mascota = Mascota(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, dueno)
        mascotas[nombre_mascota] = nueva_mascota
        print(f"\nLa mascota {nombre_mascota} fue agregada correctamente ✓")

        # 5
        existe = os.path.isfile(csv_mascota_file)
        with open(csv_mascota_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if not existe:
                writer.writerow(['nombre', 'especie', 'raza', 'edad', 'dueno_nombre', 'dueno_telefono', 'dueno_direccion', 'dueno_documento'])
            writer.writerow([
                nueva_mascota.nombre,
                nueva_mascota.especie,
                nueva_mascota.raza,
                nueva_mascota.edad,
                dueno.nombre,
                dueno.telefono,
                dueno.direccion,
                dueno.documento
            ])

    except ErrorBase as e:
        # 6
        logger.error(f"Ha ocurrido un error registrando una nueva mascota o dueño: {e}")
        print("Ha ocurrido un error llenando la información del formulario. Intente de nuevo.")


# B
def crear_consulta(mascotas, consultas):
    """
    B. Registra una nueva consulta veterinaria para una mascota existente.
    1. Solicita nombre de la mascota para la consulta.
    2. Verifica si la mascota está registrada.
    3. Solicita datos de la consulta.
    4. Crea y agrega la consulta a la lista.
    5. Informa éxito o captura errores.
    """
    try:
        # 1
        nombre_mascota = input("Nombre de la mascota: ").strip()
        # 2
        if nombre_mascota not in mascotas:
            print(f"\nNo se encontró una mascota registrada con el nombre {nombre_mascota}.")
            logger.warning(f"Cuidado, intento de buscar mascota {nombre_mascota} sin nombre registrado.")
            return
        else:
            # 3
            fecha = input("Fecha (dd/mm/aaaa): ")
            motivo = input("Motivo de la visita: ")
            diagnostico = input("¿Qué síntomas tiene?: ")

            consulta = Consulta(fecha, motivo, diagnostico, mascotas[nombre_mascota])
            consultas.append(consulta)

        # 4
        print(f"Consulta registrada correctamente para {nombre_mascota} ✓")
    except ErrorBase as e:
        # 5
        logger.error(f"Error al registrar consulta: {e}")
        print("Ha ocurrido un error registrando una nueva consulta, porfavor verifique la información.")


# C
def listar_mascotas(mascotas):
    """
    C. Lista todas las mascotas registradas.
    1. Verifica que haya mascotas registradas.
    2. Muestra la información de cada mascota.
    3. Captura errores inesperados.
    """
    try:
        # 1
        if not mascotas:
            print("No hay mascotas registradas.")
            logger.info("Intento de listar mascotas sin haber registrado ninguna.")
            return
        # 2
        for mascota in mascotas.values():
            print(f"\n- {mascota}")
        logger.info("Mascotas listadas con éxito.")
    except Exception as e:
        # 3
        logger.error(f"Error al listar las mascotas: {e}")


# D
def mostrar_historial(mascotas, consultas):
    """
    D. Muestra el historial de consultas de una mascota.
    1. Verifica que existan mascotas.
    2. Solicita el nombre de la mascota.
    3. Busca consultas asociadas.
    4. Informa si no hay historial.
    5. Muestra el historial encontrado.
    6. Maneja errores durante el proceso.
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
    except ErrorBase as e:
        # 6
        logger.error(f"Error al mostrar historial: {e}")
        print(f"Estamos teniendo problemas al listar el historial de {nombre_mascota}, sentimos los inconvenientes.")


def borrar_datos_csv():
    """
    1. Borra todo el contenido del archivo CSV de mascotas y dueños.
    2. Captura errores al limpiar el archivo.
    """
    csv_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    csv_mascota_file = os.path.join(csv_dir, 'mascotas_duenos.csv')
    try:
        with open(csv_mascota_file, 'w', encoding='utf-8') as file:
            file.write('')  # 1
        print("Archivo CSV limpiado correctamente.")
        logger.info("Se borro la información correctamente")
    except Exception as e:
        # 2
        print(f"Error limpiando el archivo CSV: {e}")
        logger.error(f"Error limpiando el archivo CSV: {e}")


def menu():
    """
    E. Muestra el menú principal de opciones para el usuario.
    1. Imprime las opciones disponibles.
    """
    print("========================")
    print("---- Menú principal ----")
    print("========================")
    print("1. Registrar nueva mascota")
    print("2. Registrar nueva consulta")
    print("3. Listar mascotas")
    print("4. Mostrar historial de consultas")
    print("5. Borrar datos")
    print("6. Salir")