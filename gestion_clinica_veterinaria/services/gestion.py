"""
---- Información ----

En este archivo se almacenan todas las funciones que permiten que el aplicativo funcione.
Para garantizar su funcionamiento, lo primero que hacemos es importar todos los objetos y el logger.
"""

from models.mascota import Mascota 
from models.dueno import Dueno     
from models.consulta import Consulta  
from config.logging_config import logger  
from exceptions.errores import ErrorBase
from services.db import SessionLocal  


def crear_mascota():
    """
    A. Registra una nueva mascota y su dueño si no existe.
    1. Crea el directorio data si no existe para guardar el archivo CSV.
    2. Obtiene la ruta del archivo CSV para añadir la nueva mascota.
    3. Solicita datos de la mascota y dueño.
    4. Valida si el dueño ya está registrado para evitar duplicados.
    5. Agrega la nueva mascota y guarda la información en el archivo CSV.
    6. Captura errores específicos de validación.
    """
    session = SessionLocal()  # Crear sesión local
    try:
        # 3
        nombre_mascota = input("Nombre de la mascota: ")
        especie_mascota = input("Especie: ")
        raza_mascota = input("Raza: ")
        edad_mascota = input("Edad: ")
        documento_dueno = input("\nDocumento del dueño: ").strip()
        
        # 4 - Verificar en la base de datos
        dueno_existente = session.query(Dueno).filter(Dueno.documento == documento_dueno).first()
        
        if dueno_existente:
            print("\nEl dueño ya se encuentra registrado en nuestra base de datos, se usará su información.")
            dueno = dueno_existente
            logger.info(f"La mascota {nombre_mascota} fue asignada a un dueño ya existente ({dueno.nombre}).")
        else:
            print("\nRegistrando un nuevo dueño en la base de datos...")
            nombre_dueno = input("Nombre del dueño: ")
            telefono_dueno = input("Teléfono: ")
            direccion_dueno = input("Dirección: ")
            dueno = Dueno(nombre_dueno, telefono_dueno, direccion_dueno, documento_dueno)
            session.add(dueno)
        
        nueva_mascota = Mascota(nombre_mascota, especie_mascota, raza_mascota, edad_mascota, dueno)
        session.add(nueva_mascota)
        session.commit()

        print(f"\nLa mascota {nombre_mascota} fue agregada correctamente ✓")

    except ErrorBase as e:
        session.rollback()
        logger.error(f"Ha ocurrido un error registrando una nueva mascota o dueño: {e}")
        print("Ha ocurrido un error llenando la información del formulario. Intente de nuevo.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inesperado: {e}")
        print("Ha ocurrido un error inesperado.")
    finally:
        session.close()

def actualizar(tipo):
    """
    Permite actualizar los datos de una mascota por su nombre.
    """
    session = SessionLocal()
    try:
        match tipo:
            case "mascota":
                nombre = input("Ingrese el nombre de la mascota que desea actualizar: ").strip().capitalize()
                mascota = session.query(Mascota).filter(Mascota.nombre == nombre).first()
                
                if not mascota:
                    print("No se encontró una mascota con ese nombre.")
                    return
                
                print(f"\nMascota actual: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
                print("Deja en blanco si no deseas cambiar algún dato.")
                
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nueva_especie = input("Nueva especie: ").strip()
                nueva_raza = input("Nueva raza: ").strip()
                nueva_edad = input("Nueva edad: ").strip()
                
                if nuevo_nombre:
                    mascota.nombre = nuevo_nombre
                if nueva_especie:
                    mascota.especie = nueva_especie
                if nueva_raza:
                    mascota.raza = nueva_raza
                if nueva_edad:
                    mascota.edad = int(nueva_edad)
                
                session.commit()
                print("Información de la mascota actualizada correctamente ✓")
                logger.info(f"Mascota {nombre} actualizada.")
            
            case "dueno":
                documento = input("Ingrese el documento del dueño que desea actualizar: ").strip()
                dueno = session.query(Dueno).filter(Dueno.documento == documento).first()
                
                if not dueno:
                    print("No se encontró un dueño con ese documento.")
                    return
                
                print(f"\nDueño actual: {dueno.nombre}, Tel: {dueno.telefono}, Dir: {dueno.direccion}")
                print("Deja en blanco si no deseas cambiar algún dato.")
                
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nuevo_telefono = input("Nuevo teléfono: ").strip()
                nueva_direccion = input("Nueva dirección: ").strip()
                
                if nuevo_nombre:
                    dueno.nombre = nuevo_nombre
                if nuevo_telefono:
                    dueno.telefono = int(nuevo_telefono)
                if nueva_direccion:
                    dueno.direccion = nueva_direccion
                
                session.commit()
                print("Información del dueño actualizada correctamente ✓")
                logger.info(f"Dueño {documento} actualizado.")
        
    except Exception as e:
        session.rollback()
        logger.error(f"Error actualizando {tipo}: {e}")
        print(f"Ocurrió un error actualizando la información de {tipo}.")
    finally:
        session.close()

def crear_consulta():
    """
    B. Registra una nueva consulta veterinaria para una mascota existente.
    1. Solicita nombre de la mascota para la consulta.
    2. Verifica si la mascota está registrada.
    3. Solicita datos de la consulta.
    4. Crea y agrega la consulta a la lista.
    5. Informa éxito o captura errores.
    """
    session = SessionLocal()
    try:
        # 1
        nombre_mascota = input("Nombre de la mascota: ").strip().capitalize()
        
        # 2 - Buscar en la base de datos
        mascota = session.query(Mascota).filter(Mascota.nombre == nombre_mascota).first()
        
        if not mascota:
            print(f"\nNo se encontró una mascota registrada con el nombre {nombre_mascota}.")
            logger.warning(f"Cuidado, intento de buscar mascota {nombre_mascota} sin nombre registrado.")
            return
        
        # 3
        fecha = input("Fecha (dd/mm/aaaa): ")
        motivo = input("Motivo de la visita: ")
        diagnostico = input("¿Qué síntomas tiene?: ")

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        session.add(consulta)
        session.commit()

        # 4
        print(f"Consulta registrada correctamente para {nombre_mascota} ✓")
        
    except ErrorBase as e:
        session.rollback()
        logger.error(f"Error al registrar consulta: {e}")
        print("Ha ocurrido un error registrando una nueva consulta, porfavor verifique la información.")
    finally:
        session.close()


    """
    G. Permite actualizar la última consulta registrada de una mascota, usando solo su nombre.
    """
    session = SessionLocal()
    try:
        nombre_mascota = input("Ingrese el nombre de la mascota: ").strip().capitalize()

        # Buscar la mascota
        mascota = session.query(Mascota).filter(Mascota.nombre == nombre_mascota).first()
        if not mascota:
            print("Mascota no encontrada.")
            return

        # Buscar la última consulta registrada
        consulta = (
            session.query(Consulta)
            .filter(Consulta.mascota_id == mascota.id)
            .order_by(Consulta.id.desc())
            .first()
        )

        if not consulta:
            print("No hay consultas registradas para esta mascota.")
            return

        print(f"\nConsulta actual:")
        print(f"- Fecha: {consulta.fecha}")
        print(f"- Motivo: {consulta.motivo}")
        print(f"- Diagnóstico: {consulta.diagnostico}")

        print("\nDeja en blanco si no deseas modificar ese campo.")

        nueva_fecha = input("Nueva fecha: ").strip()
        nuevo_motivo = input("Nuevo motivo: ").strip()
        nuevo_diagnostico = input("Nuevo diagnóstico: ").strip()

        if nueva_fecha:
            consulta.fecha = nueva_fecha
        if nuevo_motivo:
            consulta.motivo = nuevo_motivo
        if nuevo_diagnostico:
            consulta.diagnostico = nuevo_diagnostico

        session.commit()
        print("Consulta actualizada correctamente ✓")
        logger.info(f"Consulta actualizada para la mascota {nombre_mascota}.")

    except Exception as e:
        session.rollback()
        logger.error(f"Error al actualizar consulta: {e}")
        print("Ocurrió un error al actualizar la consulta.")
    finally:
        session.close()

def listar_mascotas():
    """
    C. Lista todas las mascotas registradas.
    1. Verifica que haya mascotas registradas.
    2. Muestra la información de cada mascota.
    3. Captura errores inesperados.
    """
    session = SessionLocal()
    try:
        # Cargar mascotas desde la base de datos
        mascotas_db = session.query(Mascota).all()
        
        # 1
        if not mascotas_db:
            print("No hay mascotas registradas.")
            logger.info("Intento de listar mascotas sin haber registrado ninguna.")
            return
        
        # 2
        for mascota in mascotas_db:
            print(f"\n- {mascota}")
        logger.info("Mascotas listadas con éxito.")
        
    except Exception as e:
        # 3
        logger.error(f"Error al listar las mascotas: {e}")
        print("Error al cargar las mascotas.")
    finally:
        session.close()

def listar_duenos():
    session = SessionLocal()

    try:
        # Cargar mascotas desde la base de datos
        duenos_db = session.query(Dueno).all()
        
        # 1
        if not duenos_db:
            print("No hay dueños registrados.")
            logger.info("Intento de listar dueño no registrado.")
            return
        
        # 2
        for dueno in duenos_db:
            print(f"\n- {dueno}")
        logger.info("Dueños listados con éxito.")
        
    except Exception as e:
        # 3
        logger.error(f"Error al listar dueno: {e}")
        print("Error al cargar los dueños.")
    finally:
        session.close()

def mostrar_historial():
    """
    D. Muestra el historial de consultas de una mascota.
    1. Verifica que existan mascotas.
    2. Solicita el nombre de la mascota.
    3. Busca consultas asociadas.
    4. Informa si no hay historial.
    5. Muestra el historial encontrado.
    6. Maneja errores durante el proceso.
    """
    session = SessionLocal()
    try:
        # 2
        nombre_mascota = input("Ingrese el nombre de la mascota: ").strip().capitalize()
        
        # Buscar mascota en la base de datos
        mascota = session.query(Mascota).filter(Mascota.nombre == nombre_mascota).first()
        
        if not mascota:
            print("Mascota no encontrada.")
            logger.warning("Cuidado, nombre de mascota no encontrado.")
            return

        # 3 - Buscar consultas en la base de datos
        historial = session.query(Consulta).filter(Consulta.mascota_id == mascota.id).all()

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
    except Exception as e:
        logger.error(f"Error inesperado en historial: {e}")
        print("Error inesperado al mostrar el historial.")
    finally:
        session.close()

def borrar(tipo):
    """
    Función para borrar datos según el tipo especificado.
    Parámetros:
    - tipo: "mascota", "dueno" o "todo"
    """
    session = SessionLocal()
    try:
        match tipo:
            case "mascota":
                # 1
                nombre_mascota = input("Ingrese el nombre de la mascota a eliminar: ").strip().capitalize()
                
                # 2 - Buscar mascota en la base de datos
                mascota = session.query(Mascota).filter(Mascota.nombre == nombre_mascota).first()
                
                # 3
                if not mascota:
                    print(f"No se encontró una mascota con el nombre '{nombre_mascota}'.")
                    logger.warning(f"Intento de eliminar mascota inexistente: {nombre_mascota}")
                    return
                
                # Mostrar información de la mascota antes de eliminar
                print(f"\nMascota a eliminar:")
                print(f"- Nombre: {mascota.nombre}")
                print(f"- Especie: {mascota.especie}")
                print(f"- Raza: {mascota.raza}")
                print(f"- Edad: {mascota.edad}")
                
                # Confirmación antes de eliminar
                confirmacion = input(f"¿Está seguro de que desea eliminar a {nombre_mascota}? Esto eliminará las consultas asociadas también. (s/n): ").strip().lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                    return
                
                # 4 - Eliminar consultas asociadas primero (por integridad referencial)
                consultas_eliminadas = session.query(Consulta).filter(Consulta.mascota_id == mascota.id).delete()
                
                # 5 - Eliminar la mascota
                session.delete(mascota)
                session.commit()
                
                print(f"✓ Mascota '{nombre_mascota}' eliminada correctamente.")
                if consultas_eliminadas > 0:
                    print(f"✓ También se eliminaron {consultas_eliminadas} consulta(s) asociada(s).")
                
                logger.info(f"Mascota {nombre_mascota} eliminada exitosamente junto con {consultas_eliminadas} consultas.")

            case "dueno":
                # 1
                documento_dueno = input("Ingrese el documento del dueño a eliminar: ").strip()
                
                # 2 - Buscar dueño en la base de datos
                dueno = session.query(Dueno).filter(Dueno.documento == documento_dueno).first()
                
                # 3
                if not dueno:
                    print(f"No se encontró un dueño con el documento '{documento_dueno}'.")
                    logger.warning(f"Intento de eliminar dueño inexistente: {documento_dueno}")
                    return
                
                # 4 - Verificar si tiene mascotas asociadas
                mascotas_asociadas = session.query(Mascota).filter(Mascota.dueno_documento == documento_dueno).count()
                
                if mascotas_asociadas > 0:
                    print(f"No se puede eliminar al dueño '{dueno.nombre}' porque tiene {mascotas_asociadas} mascota(s) asociada(s).")
                    print("Primero debe eliminar las mascotas antes de eliminar al dueño.")
                    logger.warning(f"Intento de eliminar dueño {dueno.nombre} con {mascotas_asociadas} mascotas asociadas.")
                    return
                
                # Mostrar información del dueño antes de eliminar
                print(f"\nDueño a eliminar:")
                print(f"- Nombre: {dueno.nombre}")
                print(f"- Documento: {dueno.documento}")
                print(f"- Teléfono: {dueno.telefono}")
                print(f"- Dirección: {dueno.direccion}")
                
                # Confirmación antes de eliminar
                confirmacion = input(f"\n¿Está seguro de que desea eliminar al dueño '{dueno.nombre}'? (s/n): ").strip().lower()
                if confirmacion != 's':
                    print("Operación cancelada.")
                    return
                
                # 5 - Eliminar el dueño
                session.delete(dueno)
                session.commit()
                
                print(f"✓ Dueño '{dueno.nombre}' eliminado correctamente.")
                logger.info(f"Dueño {dueno.nombre} (documento: {documento_dueno}) eliminado exitosamente.")

            case "todo":
                # 1 - Confirmación múltiple
                print("⚠️  ADVERTENCIA: Esta operación eliminará TODOS los datos de mascotas, dueños y consultas.")
                print("Esta acción NO se puede deshacer.")
                
                confirmacion1 = input("¿Está seguro de que desea continuar? (escriba 'SI' en mayúsculas): ").strip()
                if confirmacion1 != 'SI':
                    print("Operación cancelada.")
                    return
                
                confirmacion2 = input("Confirme nuevamente escribiendo 'ELIMINAR TODO': ").strip()
                if confirmacion2 != 'ELIMINAR TODO':
                    print("Operación cancelada.")
                    return
                
                # Contar registros antes de eliminar
                total_consultas = session.query(Consulta).count()
                total_mascotas = session.query(Mascota).count()
                total_duenos = session.query(Dueno).count()
                
                if total_consultas == 0 and total_mascotas == 0 and total_duenos == 0:
                    print("No hay datos para eliminar.")
                    return
                
                # 2 - Eliminar todas las consultas primero
                session.query(Consulta).delete()
                
                # 3 - Eliminar todas las mascotas
                session.query(Mascota).delete()
                
                # 4 - Eliminar todos los dueños
                session.query(Dueno).delete()
                
                session.commit()
                
                # 5 - Mostrar resumen
                print("✓ Todos los datos han sido eliminados exitosamente:")
                print(f"  - {total_consultas} consulta(s) eliminada(s)")
                print(f"  - {total_mascotas} mascota(s) eliminada(s)")
                print(f"  - {total_duenos} dueño(s) eliminado(s)")
                
                logger.info(f"Eliminación masiva completada: {total_consultas} consultas, {total_mascotas} mascotas, {total_duenos} dueños.")
            
            case _:
                print(f"Tipo de eliminación no válido: '{tipo}'. Use 'mascota', 'dueno' o 'todo'.")
                logger.warning(f"Llamada a función borrar() con tipo inválido: {tipo}")
                
    except ErrorBase as e:
        session.rollback()
        # Crear variable para el identificador según el tipo
        identificador = ""
        if tipo == "mascota" and 'nombre_mascota' in locals():
            identificador = nombre_mascota
        elif tipo == "dueno" and 'documento_dueno' in locals():
            identificador = documento_dueno
        elif tipo == "todo":
            identificador = "todos los datos"
        
        logger.error(f"Error al eliminar {tipo} {identificador}: {e}")
        print(f"Ha ocurrido un error al eliminar {tipo}. Intente de nuevo.")
    except Exception as e:
        session.rollback()
        logger.error(f"Error inesperado al eliminar {tipo}: {e}")
        print("Ha ocurrido un error inesperado.")
    finally:
        session.close()

def menu(tipo):
    match tipo:
        case "principal":
            """
            E. Muestra el menú principal de opciones para el usuario.
            1. Imprime las opciones disponibles.
            """
            print("\n========================")
            print("---- Menú principal ----")
            print("========================")
            print("1. Mascotas")
            print("2. Consultas")
            print("3. Dueños")
            print("4. Borrar datos")
            print("5. Salir")

        case "mascotas":
            print("\n=======================")
            print("---- Menú Mascotas ----")
            print("=======================")
            print("1. Registrar nueva mascota")
            print("2. Actualizar mascota ya existente")
            print("3. Listar mascotas")
            print("4. Borrar datos mascotas")
            print("5. Volver al menú principal")

        case "consultas":
            """
            E. Muestra el menú principal de opciones para el usuario.
            1. Imprime las opciones disponibles.
            """
            print("\n========================")
            print("---- Menú Consultas ----")
            print("========================")
            print("1. Registrar nueva consulta")
            print("2. Mostrar historial de consultas")
            print("3. Salir")

        case "duenos":
            """
            E. Muestra el menú principal de opciones para el usuario.
            1. Imprime las opciones disponibles.
            """
            print("\n=======================")
            print("----- Menú Dueños -----")
            print("=======================")
            print("1. Listar dueños")
            print("2. Actualizar dueños")
            print("3. Borrar Datos Dueños")
            print("4. Volver al menú principal")
        
