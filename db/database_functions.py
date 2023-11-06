import hashlib
import logging
import sys
from utils.config import Config
from utils import config
from .database_connection import DatabaseContextManager
from pprint import pprint

DATABASE_NAME = 'data.db'
def create_table(query) -> None:
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def add_data(query,*args) -> None:
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)

def fetch_user(query,username: str,password: str) -> str:
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query,(username,password,))
        record = cursor.fetchone()
        return record      
    

def update_data(query,*args) -> None:
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

def fetch_data(query,*args) :
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()  
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)
        records = cursor.fetchall()
        return records
    
def display_data(query):
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()  
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        data = cursor.execute(query).fetchall()
        pprint(data)
    