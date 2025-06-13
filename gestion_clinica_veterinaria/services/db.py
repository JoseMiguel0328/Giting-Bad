from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

db_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(db_dir, exist_ok=True) 
db_file = os.path.join(db_dir, 'clinica_veterinaria.db')
db_url = f'sqlite:///{db_file}'

engine = create_engine(
    db_url,
    pool_size=5,
    max_overflow=10
    )

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()