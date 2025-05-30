import json
from models.consulta import Consulta
from config.logging_config import logger


def guardar_consultas_json(consultas, archivo="data/consultas.json"):
    data = [c.to_dict() for c in consultas]
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logger.info("Se han guardado las consultas correctamente.")

def cargar_consultas_json(consultas, mascotas, archivo="data/consultas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                mascota = mascotas.get(item["mascota"])
                if mascota:
                    consulta = Consulta(
                        item["fecha"], item["motivo"], item["diagnostico"], mascota
                    )
                    consultas.append(consulta)
        logger.info("Información de consultas cargada satisfactoriamente.")
    except FileNotFoundError:
        logger.error("El archivo consultas.json no existe. Imposible cargar la información.")
        pass  # Si el archivo no existe, se retorna lista vacía

    return consultas

def borrar_consultas_json(archivo="data/consultas.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)
    logger.warning("Se han borrado las consultas.")
    print("Se ha borrado la información del archivo de consultas.")



