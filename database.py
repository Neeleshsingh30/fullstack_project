from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL connection URL
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/StudentsDB"

# Engine create
engine = create_engine(DATABASE_URL, echo=True)

# Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()
