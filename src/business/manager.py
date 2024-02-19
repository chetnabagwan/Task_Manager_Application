from utils.helper_functions import DataNotFoundError,create_userid
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
        

    def assign_tasks_to_user_logic(self,task_id,user,task_name,task_desc,today_date,due_date,category,man_id):
        """This method assigns tasks to a selected user."""

        try:    
            write_to_database([Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,Config.INSERT_INTO_ASSIGNED_TASKS_TABLE],[(task_id,user,task_name,task_desc,today_date,due_date,category,man_id),
           (man_id,user,task_id)])
        except Exception as e :
            raise e


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

