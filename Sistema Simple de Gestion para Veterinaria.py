"""
- Registrar nuevas mascotas y asignarlas a un dueño.
- Registrar consultas veterinarias para una mascota específica.
- Mostrar todas las mascotas registradas junto con su dueño.
- Mostrar el historial de consultas de una mascota en particular.

"""

class mascota():
    def __init__(self, nombre='', especie='', raza='', edad=0, dueno=''): # Se crea el constructor
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno
    
    def __str__(self): # Se utiliza el metodo magico str 
        return

class dueno():
    def __init__(self, nombre='', telefono=0, direccion='', documento=''): # Se crea el constructor
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.documento = documento

    def __str__(self): #Se utiliza el metodo magico str 
        return

class consulta():
    def __init__(self, fecha='', motivo='', diagnostico='', mascota=''): # Se crea el constructor
        self.motivo = motivo
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.mascota = mascota
        
    def __str__(self): #Se utiliza el metodo magico str 
        return

mascotas = {}
duenos = {}

def crearMascota():

    #Pedimos la información de la mascota
    nombreMascota = input("\nNombre de la mascota: ")
    especieMascota = input("\nEspecie: ")
    razaMascota = input("\nRaza: ")
    edadMascota = input("\nEdad: ")
    documentoDueno = input("\nDocumento del dueño: ")
    

    #Se verifica si el dueño ya está en la base de datos
    if (documentoDueno in duenos):
        print("\nEl dueño ya se encuentra registrado en nuesta base de datos, se usará su información.")
        d = duenos[documentoDueno] #Si, si se encuentra registrado, creamos un objeto con su información.
    else:
        print("\nRegistrando un nuevo dueño a la base de datos...")
        
        nombreDueno = input("\nNombre del dueño: ")
        telefonoDueno = input("\nTeléfono: ")
        direccionDueno = input("\nDirección: ")
    
        #Se crean ambos objetos con la información suministrada
        d = dueno(nombreDueno, telefonoDueno, direccionDueno, documentoDueno) 
    
    m = mascota(nombreMascota, especieMascota, razaMascota, edadMascota, d)

    duenos[documentoDueno] = {'dueno': d} #Se agrega información al diccionario del dueño
    mascotas[nombreMascota] = {'mascota': m, 'consultas': []} # #Se agrega información al diccionario de la mascota

    print(f"\nLa mascota {nombreMascota} fue agregada correctamente ✓")

def crearConsulta():
    # Se pide información para las cconsulta
    Fecha = input("Fecha: ")
    Motivo = input("\nMotivo de la visita: ")
    Diagnostico = input("\nQue sintomas tiene: ")
    nombreMascota = input("\nNombre de la mascota: ")
    
    # Se verifica si hay o no una mascota registrada
    if nombreMascota not in mascotas:
        print(f"\nNo se encontro una mascota registrada con el nombre {nombreMascota}.")
        return
    
    # Se crean los objetos de la consulta
    m = mascotas[nombreMascota]['mascota']
    c = consulta(Fecha, Motivo, Diagnostico, m)

    # Se agrega la información de la consulta a la lista
    mascotas[nombreMascota]['consultas'].append(c)
    print(f"Consulta registrada correctamente para {nombreMascota} ✓")
        
        
def listarMascotas():
    return

def mostrarHistorial():
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


# Bucle principal del código
while True:
    menu()
    accion = int(input("Porfavor ingrese una opción (1-5): "))
    
    match accion:
        case 1:
            crearMascota()
        case 2:
            crearConsulta()
        case 3:
            continue
        case 4:
            continue
        case 5:
            print("Gracias por usar nuestros sevicios!")
            break
        case _:
            print("Ingrese una opción valida.")
