import logging
from src.utils.config import Config
from src.db.database_connection import DatabaseContextManager


logger = logging.getLogger('database helper functions')#puri krna h logging
DATABASE_NAME = 'data.db'

def create_table(query) -> None:
    """Function to creat table in database."""

    logger.info('Creating Database schema')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)


def add_data(query,*args) -> None:
    """Function to add data in specific table of database"""

    logger.info('Adding data in database')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)


def fetch_user(query,username: str,password: str) -> str:
    """ Function to fetch user data from database"""
    
    logger.info('Fetching user data from the database.')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query,(username,password,))
        record = cursor.fetchone()
        return record     
  

def update_data(query,*args) -> None:
    """Function to update data in database"""

    logger.info('Updating data in the database.')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  


def fetch_data(query,*args ) :
    """Function to fetch data from database"""

    logger.info('Fetching data from the database')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()  
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)
        records = cursor.fetchall()
        return records


def display_data(query):
    """Function to display data from database"""

    logger.info('Displaying data from the database')
    with DatabaseContextManager(DATABASE_NAME) as connection:
        cursor = connection.cursor()  
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        data = cursor.execute(query).fetchall()
        return data
    