from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging 
import pandas as pd

Base = declarative_base()

def initialize_db():
    try:
        engine = create_engine('sqlite:///kaggle_amz_db.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except SQLAlchemyError as e:
        logger.error(f"Error initializing database: {e}")