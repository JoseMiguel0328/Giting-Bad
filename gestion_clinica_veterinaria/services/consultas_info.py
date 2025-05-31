# ---- Información ----
# Este archivo maneja la persistencia (guardar, cargar y borrar) de las consultas en formato JSON.
# Usa la clase Consulta para reconstruir objetos desde el archivo.
# También utiliza logging para registrar eventos importantes o errores.

import json
from models.consulta import Consulta  # Se importa la clase Consulta para poder instanciar objetos
from config.logging_config import logger  # Se importa el sistema de logging

def guardar_consultas_json(consultas, archivo="data/consultas.json"):
    """
    1. Convierte cada objeto de la lista 'consultas' a diccionario con .to_dict().
    2. Escribe todos los datos en el archivo JSON especificado.
    3. Registra en el log que la operación fue exitosa.
    """
    data = [c.to_dict() for c in consultas]  #1
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  #2
    logger.info("Se han guardado las consultas correctamente.")  #3

def cargar_consultas_json(consultas, mascotas, archivo="data/consultas.json"):
    """
    1. Intenta abrir el archivo JSON con datos de consultas.
    2. Por cada item, busca la mascota correspondiente usando el diccionario 'mascotas'.
    3. Si encuentra la mascota, crea un objeto Consulta y lo agrega a la lista 'consultas'.
    4. Registra en el log que la carga fue exitosa.
    5. Si el archivo no existe, registra el error pero no detiene la ejecución.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)  #1
            for item in data:
                mascota = mascotas.get(item["mascota"])  #2
                if mascota:
                    consulta = Consulta(
                        item["fecha"], item["motivo"], item["diagnostico"], mascota
                    )  #3
                    consultas.append(consulta)
        logger.info("Información de consultas cargada satisfactoriamente.")  #4
    except FileNotFoundError:
        logger.error("El archivo consultas.json no existe. Imposible cargar la información.")  #5
        pass

    return consultas  # Retorna la lista de consultas actualizada

def borrar_consultas_json(archivo="data/consultas.json"):
    """
    1. Abre el archivo JSON en modo escritura y lo sobrescribe con una lista vacía.
    2. Deja registro en el log de que las consultas han sido borradas.
    3. También imprime un mensaje en consola.
    """
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)  #1
    logger.warning("Se han borrado las consultas.")  #2
    print("Se ha borrado la información del archivo de consultas.")  #3
