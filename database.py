from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carrega o .env de outra pasta
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", ".env")
load_dotenv(dotenv_path)

# Pega a URL do banco do .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")

# Cria o engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# Sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
