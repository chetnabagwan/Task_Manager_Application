import logging
from utils.config import Config
from db.database_functions import create_table
from main_menu import MainMenu

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt = "%d-%M-%Y %H:%M:%S", level=logging.DEBUG,
    filename="logs.log",
)

logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG, filename='utils/logs.log')
logger = logging.getLogger("main")


if __name__== '__main__':
    logger.info('Application started')
    Config.load()
    Config.loadManagerQueries()
    Config.loadUserQueries()
    Config.load_print_statements()
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_TASKS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE)
    MainMenu.start()
    logger.info('Application ended')
