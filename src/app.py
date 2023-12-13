"""Task manager allows users to create and manage their day to day tasks and alerts 
   them about their pending tasks.The manager can also assign and check the status of tasks."""

import logging
from utils.config import Config
from main_menu import MainMenu
from db.database_functions import create_table

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt = "%d-%M-%Y %H:%M:%S", level=logging.DEBUG,
    filename="logs.log",
)

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG, filename='utils/logs.log')
logger = logging.getLogger(__name__)

@Config.config_loader
def app():
    """Function to start the application"""

    logger.info('Application started')
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_TASKS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE)
    print(Config.WELCOME_MESSAGE)
    MainMenu.start()
    logger.info('Application ended')    

if __name__ == '__main__':
    app()
