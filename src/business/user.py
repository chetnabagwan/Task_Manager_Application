from utils.helper_functions import DataNotFoundError,create_userid
from db.database_functions import write_to_database,update_data,fetch_data
from utils.config import Config

class User:
    '''This class contains user operations logic'''
    def myprofile(self,user_id):
        """This methods displays user profile"""
        try:
            data = fetch_data(Config.VIEW_MY_PROFILE,(user_id,))
            return data[0] 
        except Exception as e:
            raise e

    def update_my_profile(self,user_id,name,email,phone_number):
        """This method updates user's profile info"""
        try:
            update_data(Config.UPDATE_MY_PROFILE,(name,email,phone_number,user_id))
        except Exception as e:
            raise e


    def create_new_tasks(self,task_id,user_id,task_name,task_desc,today_date,due_date,category):
        """This method creates new task for user"""
     
        try:
            write_to_database(Config.INSERT_INTO_TASKS_TABLE,(task_id,user_id,task_name,task_desc,today_date,due_date,category))
        except Exception as e:
            raise e


    def view_my_tasks(self,user_id):
        """This method allows a user to view his/her tasks"""
      
        try:
            data=fetch_data(Config.VIEW_TASKS,(user_id,))
            return data
        except Exception as e:
            raise e


    def update_my_tasks(self,task_id,status,due_date):
        """This method helps user to update his/her tasks. User can update both status and duedate of a task"""
        
        try:
            update_data(Config.UPDATE_DUE_DATE,(due_date,task_id))
            update_data(Config.UPDATE_TASK_STATUS,(task_id,))
            print(Config.TASK_STATUS_UPDATED)
        except Exception as e:
            raise e

    def delete_my_tasks(self,task_id):
        """This method deletes a selected task."""

        try:
            update_data(Config.DELETE_MY_TASKS,(task_id))
        except Exception as e:
            raise e
