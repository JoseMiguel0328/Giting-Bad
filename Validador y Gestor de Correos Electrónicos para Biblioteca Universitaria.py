#Importar biblioteca regex
import re 

# Variables globales
correosEstudiantes = []
correosDocentes = []

# Función para imprimir el menú
def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Ingresar correos")
    print("2. Ver correos guardados")
    print("3. Búsqueda de correos")
    print("4. Salir")

# Función para ingresar correos
def ingresar_correos():
    celdas = int(input("\nCantidad de correos que desea ingresar: "))
    for i in range(celdas):
        while True:
            correo = input(f"Ingrese el correo #{i + 1}: ").lower().strip() # Normalizar los datos del input
            if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo): # Verificar patrón de correos
                if correo.endswith("@estudiante.utv.edu.co"): # Verificar el dominio del correo y clasificarlo
                    correosEstudiantes.append(correo) # Función para agregar datos a las variables
                    print("Correo de estudiante")
                    break
                elif correo.endswith("@utv.edu.co"):
                    correosDocentes.append(correo)
                    print("Correo de docente")
                    break
                else:
                    print("Dominio no válido")
            else:
                print("Correo inválido")

# Función para mostrar correos
def mostrar_correos(): 
    print("\nCorreos de estudiantes:")
    for correo in correosEstudiantes: # Bucle para capturar dominios de estudiante
        print(correo)

    print("\nCorreos de docentes:")
    for correo in correosDocentes: 
        print(correo)
    
# Función para buscar correos
def buscar_correos(busqueda):
    resultadosBusqueda = [] 
    totalidadCorreos = correosEstudiantes + correosDocentes # Mezclar ambas listas de correos para búscar de forma global
    correosEncontrados = 0

    for i in totalidadCorreos:
        if re.search(busqueda, i, re.IGNORECASE): # Función para buscar entre todos los correos (Ignora mayúsculas)
            resultadosBusqueda.append(i)
            correosEncontrados += 1

    print(f"\nSe han encontrado una totalidad de {correosEncontrados} correos que cumplen con su critério de búsqueda.\n")
    for correo in resultadosBusqueda:
        print(correo)

# Ejecutar el menú
while True:
    menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        ingresar_correos()
    elif opcion == "2":
        mostrar_correos()
    elif opcion == "3":
        busqueda = input("\n¿Qué correos está buscando?: ")
        buscar_correos(busqueda)
    elif opcion == "4":
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción no válida. Intente de nuevo.")