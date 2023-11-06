import yaml
import logging
import sqlite3
from utils.config import Config

logger = logging.getLogger('database_context_manager')

class DatabaseContextManager:

    def __init__(self,host) -> None:
        try:
            self.connection = None
            self.host = host
        except Exception as e:
            print("DB Connect error")
            #logging.critical(Config.ERROR_MESSAGE)

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.host)
            return self.connection
        except Exception as e:
            print("DB Connect error")
            #logging.critical(Config.ERROR_MESSAGE)

    def __exit__(self,exc_type,exc_value,exc_tb) -> None: 
        if exc_tb or exc_type or exc_value:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()