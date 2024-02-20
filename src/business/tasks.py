from utils.helper_functions import DataNotFoundError,create_id
from db.database_functions import write_to_database,update_data,fetch_data
from utils.config import Config

class Task:
    '''This class contains tasks related logic,all the operations on tasks'''
    def create_new_tasks(self,task_id,user_id,task_name,task_desc,today_date,due_date,category):
        """This method creates new task for user"""
     
        try:
            write_to_database([Config.INSERT_INTO_TASKS_TABLE],[(task_id,user_id,task_name,task_desc,today_date,due_date,category)])
        except Exception as e:
            raise e


    def assign_tasks_to_user_logic(self,task_id,user,task_name,task_desc,today_date,due_date,category,man_id):
        """This method assigns tasks to a selected user."""

        try:    
            write_to_database([Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,Config.INSERT_INTO_ASSIGNED_TASKS_TABLE],[(task_id,user,task_name,task_desc,today_date,due_date,category,man_id),
            (man_id,user,task_id)])
        except Exception as e :
            raise e

    
    def update_my_tasks(self,user_id,task_id,task_name,task_desc,due_date,is_completed):
        """This method helps user to update his/her tasks. User can update both status and duedate of a task"""
        
        try:
            tasks = fetch_data(Config.VIEW_TASKS_TO_DELETE_BY_USERS,(user_id,))
            for task in tasks:
                if task['task_id']==task_id:
                    print(task['task_id'])
                    update_data(Config.UPDATE_TASK,(task_name,task_desc,due_date,is_completed,task_id))
                    return
                
            raise DataNotFoundError
        except Exception as e:
            raise e


    def update_assigned_tasks(self,man_id,task_id,task_name,task_desc,due_date,is_completed):
        """This method helps user to update his/her tasks. User can update both status and duedate of a task"""
        
        try:
            tasks = fetch_data(Config.GET_TASKS_TO_DELETE_BY_MANAGER,(man_id,))
            for task in tasks:
                if task['task_id']==task_id:
                    print(task['task_id'])
                    update_data(Config.UPDATE_TASK,(task_name,task_desc,due_date,is_completed,task_id))
                    return  
            raise DataNotFoundError
        except Exception as e:
            raise e
        

    def delete_my_tasks(self,task_id,user_id):
        """This method deletes a selected task"""

        try:
            tasks = fetch_data(Config.VIEW_TASKS_TO_DELETE_BY_USERS,(user_id,))
            for task in tasks:
                if task['task_id']==task_id:
                    update_data(Config.DELETE_TASKS,(task_id,))
                    print("got it user")
                    return     
            raise DataNotFoundError
        except Exception as e:
            raise e

    def delete_assigned_tasks(Self,task_id,man_id):
        """This method deletes the assigned tasks by manager"""

        try:
            print(task_id)
            tasks = fetch_data(Config.GET_TASKS_TO_DELETE_BY_MANAGER,(man_id,))
            print(tasks)
            for task in tasks:
                if task['task_id']==int(task_id):
                    print("hello")
                    update_data(Config.DELETE_TASKS,(task_id,))
                    print("got it manager")

                    return  
            raise DataNotFoundError
        except Exception as e:
            raise e