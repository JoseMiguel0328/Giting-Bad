from config.logging_config import logger
from services.db import engine, Base
from models.dueno import Dueno
from models.mascota import Mascota
from models.consulta import Consulta

def init_database():
    logger.info("Iniciando creación de base de datos...")
    
    # Verificar qué tablas SQLAlchemy conoce
    for table_name, table in Base.metadata.tables.items():
        logger.info(f"Tabla encontrada: {table_name}")
    
    # Crear las tablas
    Base.metadata.create_all(bind=engine)
    
    # Verificar que se crearon
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables_created = inspector.get_table_names()
    logger.info(f"Tablas creadas: {tables_created}")
    
    logger.info("Tablas creadas correctamente.")

if __name__ == "__main__":
    init_database()