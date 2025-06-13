"""
---- Información ----
Este módulo configura el sistema de logging (registro de eventos) para toda la aplicación de la clínica veterinaria.

1. Crea una carpeta llamada 'logs' si no existe.
2. Define un archivo de log llamado 'clinica_veterinaria.log'.
3. Establece un logger principal llamado 'clinica_veterinaria'.
4. Define el formato de los mensajes de log.
5. Crea un handler que escribe los logs en el archivo.
"""

import logging
import os

# 1. 
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True) 

# 2. 
log_file = os.path.join(log_dir, 'clinica_veterinaria.log')

# 3. 
logger = logging.getLogger("clinica_veterinaria")
logger.setLevel(logging.DEBUG)  

# 4. 
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
"""
El formato incluye:
- asctime: fecha y hora del evento
- levelname: nivel del mensaje (INFO, DEBUG, ERROR, etc.)
- name: nombre del logger
- message: mensaje personalizado
"""

# 5. 
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)        
file_handler.setFormatter(formatter)        
logger.addHandler(file_handler)

logger.propagate = False


