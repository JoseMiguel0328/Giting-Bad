"""
---- Información ----

1. Este es el archivo principal del código, aquel que va a ser ejecutado por el usuario.

2. Para garantizar su funcionamiento lo primero que hacemos es importar todos las funciones y el logger.

3. Seguido a esto declaramos los diccionarios 'mascotas', 'duenos' y la lista 'consultas'.
Estas variables son fundamentales para la ejecución de las funciones.

4. Finalmente validamos que si el archivo 'main.py' es el que esta siendo ejecutado funcione el programa.
Esta validación es importante para poder hacer pruebas en otros archivos de forma aislada.
"""

from config.logging_config import logger
from exceptions.errores import ErrorBase 
from services.consultas_info import (
    guardar_consultas_json, 
    cargar_consultas_json, 
    borrar_consultas_json
)

from services.gestion import (             
    mostrar_mascotas_csv,
    crear_mascota,
    crear_consulta,
    listar_mascotas,
    mostrar_historial,
    borrar_datos_csv,
    menu
)

# (3) 
mascotas = {}
duenos = {}
consultas = []

mostrar_mascotas_csv(mascotas, duenos)
cargar_consultas_json(consultas, mascotas)

def main():
    try:
        while True:
            menu()  # (4) 
            accion = int(input("Por favor ingrese una opción (1-6): "))
            
            match accion:
                case 1:  
                    crear_mascota(mascotas, duenos)
                case 2:  
                    crear_consulta(mascotas, consultas)
                    guardar_consultas_json(consultas)
                case 3:  
                    listar_mascotas(mascotas)
                case 4:  
                    mostrar_historial(mascotas, consultas)
                case 5:  
                    confirmacion = input("¿Está seguro que desea borrar toda la información? (s/n): ").lower()
                    if confirmacion == 's':
                        borrar_datos_csv()
                        mascotas.clear()
                        duenos.clear()
                        consultas.clear()
                        borrar_consultas_json()
                    else:
                        print("Operación cancelada.")
                case 6:  
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