import logging
import pymysql
from utils.config import Config
from .database_connection import DatabaseContextManager


logger = logging.getLogger('database helper functions')

def create_table(query) -> None:
    """Function to creat table in database."""

    logger.info('Creating Database schema')
    with DatabaseContextManager() as connection:
        cursor = connection.cursor()
        cursor.execute(query)



def write_to_database(query:str|list,data:tuple|list):
    with DatabaseContextManager() as connection:
        cursor = connection.cursor() 
        if isinstance(query,str):
            cursor.execute(query,data)
        else:
            for i in range(len(query)):
                cursor.execute(query[i],data[i])
        connection.commit()


def fetch_user(query,username: str,password: str) -> str:
    """ Function to fetch user data from database"""
    
    logger.info('Fetching user data from the database.')
    with DatabaseContextManager() as connection:
        cursor = connection.cursor()
        cursor.execute(query,(username,password,))
        record = cursor.fetchone()
        return record     
  

def update_data(query,*args) -> None:
    """Function to update data in database"""

    logger.info('Updating data in the database.')
    with DatabaseContextManager() as connection:
        cursor = connection.cursor()   
        cursor.execute(query,*args)  


def fetch_data(query,*args ) :
    """Function to fetch data from database"""

    logger.info('Fetching data from the database')
    with DatabaseContextManager() as connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)  
        cursor.execute(query,*args)
        records = cursor.fetchall()
        return records


