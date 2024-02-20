"""Task manager allows users to create and manage their day to day tasks and alerts 
   them about their pending tasks.The manager can also assign and check the status of tasks."""

import logging
from utils.config import Config
from db.database_functions import create_table,write_to_database
import hashlib
import shortuuid  

# logging.basicConfig(
#     format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
#     datefmt = "%d-%M-%Y %H:%M:%S", level=logging.DEBUG,
#     filename="logs.log",
# )

# logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
#                     datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG, filename='utils/logs.log')
# logger = logging.getLogger(__name__)

def create_admin():
    q1= 'INSERT INTO authentication (user_id,username,password,role) VALUES (%s,%s,%s,%s)'
    q2 = 'INSERT INTO users(user_id,name,email,phone_number,gender) VALUES (%s,%s,%s,%s,%s)'
    password = 'Chetna@6'
    id = int(shortuuid.ShortUUID('123456789').random(length=4))
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    d1 = (id,'chetna6',hashed_password,'manager')
    d2 = (id,'Chetna Bagwan','bagwanchetna6@gmail.com',7389430182,'female')
    write_to_database([q1,q2],[d1,d2])


def app():
    """Function to start the application"""
    # logger.info('Application started')
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_USERS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_TASKS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE)
    print(Config.WELCOME_MESSAGE)
    create_admin()
    # MainMenu.start()
    # logger.info('Application ended')    

if __name__ == '__main__':
    app()