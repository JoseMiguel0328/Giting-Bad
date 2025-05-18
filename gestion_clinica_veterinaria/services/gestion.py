from models.mascota import Mascota
from models.dueno import Dueno
from models.consulta import Consulta

def crear_mascota(mascotas, duenos):
    #Pedimos la información de la mascota
    nombre_mascota = input("Nombre de la mascota: ")
    especie_mascota = input("Especie: ")
    raza_mascota = input("Raza: ")
    edad_mascota = input("Edad: ")
    documento_dueno = input("\nDocumento del dueño: ").strip()
    

    #Se verifica si el dueño ya está en la base de datos
    if (documento_dueno in duenos):
        print("\nEl dueño ya se encuentra registrado en nuesta base de datos, se usará su información.")
        dueno = duenos[documento_dueno] #Si, si se encuentra registrado, creamos un objeto con su información.
    else:
        print("\nRegistrando un nuevo dueño a la base de datos...")
        
        nombre_dueno = input("Nombre del dueño: ")
        telefono_dueno = input("Teléfono: ")
        direccion_dueno = input("Dirección: ")
    
        #Se crean ambos objetos con la información suministrada
        dueno = Dueno(nombre_dueno, telefono_dueno, direccion_dueno, documento_dueno) 
        duenos[documento_dueno] = dueno #Se agrega información al diccionario del dueño
    
    nueva_mascota = Mascota(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, dueno)
    mascotas[nombre_mascota] = nueva_mascota # #Se agrega información al diccionario de la mascota

    print(f"\nLa mascota {nombre_mascota} fue agregada correctamente ✓")

def crear_consulta(mascotas, consultas):
    # Se pide información para las cconsulta
    nombre_mascota = input("Nombre de la mascota: ").lower().strip()
    
    # Se verifica si hay o no una mascota registrada
    if (nombre_mascota not in mascotas):
        print(f"\nNo se encontro una mascota registrada con el nombre {nombre_mascota}.")
        return
    
    fecha = input("Fecha (dd/mm/aaaa): ")
    motivo = input("Motivo de la visita: ")
    diagnostico = input("Que sintomas tiene: ")
    # Se crean los objetos de la consulta
    consulta = Consulta(fecha, motivo, diagnostico, mascotas[nombre_mascota])

    # Se agrega la información de la consulta a la lista
    consultas.append(consulta)
    print(f"Consulta registrada correctamente para {nombre_mascota} ✓")
        
        
def listar_mascotas(mascotas):
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for mascota in mascotas.values():
        print(f"\n- {mascota}")
    return

def mostrar_historial(mascotas, consultas):
    if not mascotas:
        print("No hay mascotas registradas.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ").strip()
    if (nombre_mascota not in mascotas):
        print("Mascota no encontrada.")
        return
    
    historial = []

    for consulta in consultas:
        if (consulta.mascota.nombre == nombre_mascota):
            historial.append(consulta)
    
    if not historial:
        print("No hay un historial para esta mascota registrada.")
        return
    
    print(f"El historial de {nombre_mascota} es el siguiente:\n")

    for consulta in historial:
        print(f"- {consulta}")
    return

def menu():
    print(  "\n ============================================\n " \
            "------------------- MENU -------------------\n " \
            "============================================\n")
    print("Bienvenido al sistema gestor de la clínica veterinaria Amigos Peludos ¿Qué desea hacer?")
    print("1. Registrar mascota")
    print("2. Registrar consulta")
    print("3. Listar mascotas")
    print("4. Ver historial de consultas de una mascota")
    print("5. Salir de la aplicación")
