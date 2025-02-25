
from sqlalchemy import create_engine
from sqlalchemy.orm import session
from sqlalchemy.ext.declarative import declarative_base
from database import *
from sqlalchemy.orm import sessionmaker, declarative_base

# --------------- ⬇ sqlite connection ⬇ --------------

SQLALCHEMY_DB_URL = "sqlite:///./sql_app.db"

#----------------⬇  Create engine ⬇ -------------
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#----------⬇  Create base class ⬇ ------------
Base = declarative_base()
 

