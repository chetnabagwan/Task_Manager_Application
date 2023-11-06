import sys
from authentication.authentication import Authentication
from utils.config import Config
from db.database_functions import create_table
from manager.manager_controllers import Manager
from users.user_controllers import User
from main_menu import MainMenu

#logging

if __name__== '__main__':
    Config.load()
    Config.loadManagerQueries()
    Config.loadUserQueries()
    Config.load_print_statements()
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_TASKS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE)
    MainMenu.start()
