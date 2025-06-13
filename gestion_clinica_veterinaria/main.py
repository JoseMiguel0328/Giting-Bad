"""
---- Información ----

1. Este es el archivo principal del código, aquel que va a ser ejecutado por el usuario.

2. Para garantizar su funcionamiento lo primero que hacemos es importar todos las funciones y el logger.

3. Finalmente validamos que si el archivo 'main.py' es el que esta siendo ejecutado funcione el programa.
Esta validación es importante para poder hacer pruebas en otros archivos de forma aislada.
"""

from config.logging_config import logger
from exceptions.errores import ErrorBase 

from services.gestion import (             
    crear_mascota,
    actualizar,
    crear_consulta,
    listar_mascotas,
    listar_duenos,
    mostrar_historial,
    borrar,
    menu
)

def main():
    try:
        while True:
            menu("principal")  # (3) 
            accion = int(input("Por favor ingrese una opción (1-6): "))

            match accion:
                case 1:  
                    menu("mascotas")
                    accion_mascota = int(input("Por favor ingrese una opción (1-6): "))
                    match accion_mascota:
                        case 1:
                            crear_mascota()
                        case 2:
                            actualizar("mascota")
                        case 3:
                            listar_mascotas()
                        case 4:
                            borrar("mascota")
                        case 5:
                            pass
                case 2:  
                    menu("consultas")
                    accion_consulta = int(input("Por favor ingrese una opción (1-6): "))
                    match accion_consulta:
                        case 1:
                            crear_consulta()
                        case 2:
                            mostrar_historial()
                        case 3:
                            pass
                case 3:  
                    menu("duenos")
                    accion_dueno = int(input("Por favor ingrese una opción (1-6): "))
                    match accion_dueno:
                        case 1:
                            listar_duenos()
                        case 2:
                            actualizar("dueno")
                        case 3:
                            borrar("dueno")
                        case 4:
                            pass
                case 4:  
                    borrar("todo")
                case 5:  
                    print("Gracias por usar nuestros servicios!")
                    break
                case _:  
                    print("Ingrese una opción válida.")    

    except ErrorBase as e:  # Manejo de errores de validación personalizados
        print("Error de validación de datos.")
        logger.warning(f"Error de validación en main: {e}")

    except Exception as e:  # Manejo de errores inesperados
        print("Ha ocurrido un error fatal. Visite el log para más información.")
        logger.critical(f"Error inesperado en main: {e}", exc_info=True)

# (4) Punto de entrada del programa: ejecuta main solo si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()