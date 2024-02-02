from utils.helper_functions import DataNotFoundError,create_userid
from db.database_functions import add_data,update_data,fetch_data
from utils.config import Config



class Manager:
    '''This class contains Manager operations logic'''

    def get_all_users(self):
        """This method displays all users present in the database"""

        users = fetch_data(Config.QUERY_TO_VIEW_ALL_USERS)
        if users:
            return users
        raise DataNotFoundError("No users found!")
        

    def assign_tasks_to_user(self,task_id,user,task_name,task_desc,today_date,due_date,category,man_id):
        """This method assigns tasks to a selected user."""

        try:    
            add_data(Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,(task_id,user,task_name,task_desc,today_date,due_date,category,man_id),
                     Config.INSERT_INTO_ASSIGNED_TASKS_TABLE,(man_id,user,task_id))
        except Exception as e :
            raise e


    # def view_status_of_assigned_tasks(self):

    #     """This method shows status of tasks assigned by particular manager. """

    #     logger.info(f'Manager:{self.user_id} is trying to view status of assigned tasks')
    #     data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
    #     if len(data) == 0:
    #         print(Config.NO_DATA_FOUND)
    #     else:
    #         HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
    #         print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))


    # def update_status_of_assigned_task(self):

    #     """Updates status of a selected task."""

    #     logger.info(f'Manager:{self.user_id} is updating status of assigned tasks')
    #     data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
    #     if len(data) == 0:
    #         print(Config.NO_DATA_FOUND)
    #     else:
    #         HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
    #         print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))
    #         print(Config.WHICH_TASK)
    #         task = InputValidations.taskid_validator()
    #         data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))
    #         while len(data) == 0:
    #             print(Config.TASKID_NOT_FOUND)
    #             task = InputValidations.taskid_validator()
    #             data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))
    #         status = InputValidations.task_status_validator() 
    #         update_data(Config.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS,(status,task))
    #         print(Config.TASK_STATUS_UPDATED)