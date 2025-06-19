# config/logging_config.py
"""
Configuración centralizada de logging para el proyecto.
"""

import os
import logging
from pathlib import Path

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Crear directorio de logs si no existe
LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

# Configuración de logging
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    
    # Formatters - cómo se ven los mensajes de log
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} - {message}',
            'style': '{',
        },
    },
    
    # Handlers - dónde van los logs
    'handlers': {
        # Log general de Django
        'django_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGS_DIR / 'django.log',
            'maxBytes': 1024*1024*5,  # 5MB
            'backupCount': 5,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        
        # Log de errores
        'errores_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGS_DIR / 'errores.log',
            'maxBytes': 1024*1024*2,  # 2MB
            'backupCount': 3,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
        
        # Consola (para desarrollo)
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    
    # Loggers - qué se loggea y dónde
    'loggers': {
        # Logger para Django general
        'django': {
            'handlers': ['django_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        
        # Logger para errores de la aplicación
        'veterinaria.errores': {
            'handlers': ['errores_file', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        
        # Logger general de la aplicación
        'veterinaria': {
            'handlers': ['django_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    
    # Logger raíz
    'root': {
        'level': 'INFO',
        'handlers': ['console'],
    },
}

# Función para obtener un logger específico
def get_logger(name='veterinaria'):
    """
    Obtiene un logger configurado.
    
    Args:
        name (str): Nombre del logger. Opciones:
                    - 'veterinaria' (general)
                    - 'veterinaria.errores' (específico para errores)
    
    Returns:
        logging.Logger: Logger configurado
    """
    return logging.getLogger(name)

# Configurar logging al importar el módulo
import logging.config
logging.config.dictConfig(LOGGING_CONFIG)