"""Context Manager for the database"""
import pymysql


class DatabaseContextManager:
    """ A class for sqlite3 database connection
        Automatically opens, commits and closes the connections
        
        Implements Singleton Design Pattern"""
    def __new__(cls,*args,**kwargs)->'DatabaseContextManager':
        if not hasattr(cls,'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.connection = None

    def __enter__(self):
        self.connection = pymysql.connect(user='chetna', password='123456',
                              host='127.0.0.1',
                              database='task_manager'
                              )
        return self.connection
        

    def __exit__(self,exc_type,exc_value,exc_tb) -> None:
        if exc_tb or exc_type or exc_value:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()