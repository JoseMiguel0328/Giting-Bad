# Bucle principal del código

from models.mascota import Mascota
from models.dueno import Dueno
from models.consulta import Consulta
from services.gestion import (
    crear_mascota,
    crear_consulta,
    listar_mascotas,
    mostrar_historial,
    menu
)

mascotas = {}
duenos = {}
consultas = []

def main():
    while True:
        menu()
        accion = int(input("Porfavor ingrese una opción (1-5): "))
        
        match accion:
            case 1:
                crear_mascota(mascotas, duenos)
            case 2:
                crear_consulta(mascotas, consultas)
            case 3:
                listar_mascotas(mascotas)
            case 4:
                mostrar_historial(mascotas, consultas)
            case 5:
                print("Gracias por usar nuestros sevicios!")
                break
            case _:
                print("Ingrese una opción valida.")

if __name__ == "__main__":
    main()