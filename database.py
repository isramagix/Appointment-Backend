from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el .env
load_dotenv()

# Obtiene la URL de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crea el manejador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para declarar modelos
Base = declarative_base()
