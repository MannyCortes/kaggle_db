from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging 
import pandas as pd
import gc

Base = declarative_base()

#when designing a table seperate the nouns and verb/events.
class user(Base): 
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True, unique=True)
    device = Column(String)
    location = Column(String)

class seller(Base):
    __tablename__ = 'sellers'
    seller_id = Column(String, primary_key=True, unique=True)
    seller_rating = Column(Float)

class product(Base):
    __tablename__ = 'products'
    product_id = Column(String, primary_key=True, unique=True)
    category = Column(String)
    subcategory = Column(String)
    brand = Column(String)
    price = Column(Float)
    discount = Column(Float)
    final_price = Column(Float)
    rating = Column(Float)
    review_count = Column(Integer)
    stock = Column(Integer)
    purchase_date = Column(DateTime)
    shipping_time_days = Column(Integer)
    location = Column(String)
    payment_method = Column(String)
    is_returned = Column(Boolean)
    delivery_status = Column(String)



def load_data_to_db(engine, df):
    try:
        #users table, 2 brackets indicates keep the table as a 2D 
        #inner brackets indicates a python list of columns to select outter tells python to filter using that list
        df[['user_id', 'device', 'location']].to_sql(name='users', con=engine, if_exists='append', index=False)
    except SQLAlchemyError as e:
        logging.error(f"Error loading data to database: {e}")
       # trouble_shooting(table, df, engine)
    try:
        df[['seller_id', 'seller_rating']].to_sql(name='sellers', con=engine, if_exists='append', index=False)
    except SQLAlchemyError as e:
        logging.error(f"Error loading data to database: {e}")
       # trouble_shooting(table, df, engine)
    try:
        df[['product_id', 'category', 'subcategory', 'brand', 'price', 'discount', 'final_price', 
            'rating', 'review_count', 'stock', 'purchase_date', 'shipping_time_days', 
            'location', 'payment_method', 'is_returned', 'delivery_status']].to_sql(name='products', con=engine, if_exists='append', index=False)
    except SQLAlchemyError as e:
        logging.error(f"Error loading data to database: {e}")
       # trouble_shooting(table, df, engine)
    del df
    gc.collect()
    
    


#def trouble_shooting(table, df, engine):
    # try and except blocks, quarintine the bad data

   #if table == "users":
   ## if table == "sellers":
        
    #if table == "products":

def initialize_db():
    try:
        engine = create_engine('sqlite:///kaggle_amz_db.db')
        Base.metadata.create_all(engine)
        logging.info("Database initialized successfully.")
        return engine
    except SQLAlchemyError as e:
        logging.error(f"Error initializing database: {e}")