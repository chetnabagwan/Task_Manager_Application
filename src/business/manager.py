from utils.helper_functions import DataNotFoundError,create_id
from db.database_functions import write_to_database,update_data,fetch_data
from utils.config import Config
from pymysql import DatabaseError


class Manager:
    '''This class contains Manager operations logic'''

    def get_all_users_logic(self):
        """This method displays all users present in the database"""

        users = fetch_data(Config.QUERY_TO_VIEW_ALL_USERS)
        if users:
            return users
        raise DatabaseError
        

    def view_status_of_assigned_tasks_logic(self,man_id):
        """This method shows status of tasks assigned by particular manager. """

        try:
            data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(man_id,))
            return data
        except Exception as e:
            raise e 


    def update_status_of_assigned_task(self,task_id,status,due_date):
        """Updates status of a selected task."""

        try:
            update_data(Config.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS,(status,task_id,due_date))
        except Exception as e:
            raise e

