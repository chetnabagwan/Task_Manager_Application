import logging
from flask import abort
from business.manager import Manager
from utils.helper_functions import DataNotFoundError,NotAuthorizedError,create_userid,date_today
from utils.config import Config

logger = logging.getLogger('main.manager_controllers')

mb_obj = Manager()

class ManagerController:

    def get_all_users(self,token):
        '''This method displays all users present in the database'''
        
        logger.info(f'Manager is viewing all users')
        try:
            r = token['role']
            if r != 'admin':
                raise NotAuthorizedError
            data = mb_obj.get_all_users()
            return data
        except DataNotFoundError:
            abort(404,message = "Data not found")


    def assign_tasks_to_user(self,token,data):
        '''This method assigns tasks to a user.'''

        logger.info(f'Manager is assigning tasks to users.')
        try:    
            r = token['role']
            if r != 'admin':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            man_id = token['sub']
            task_id = create_userid()
            user = data['user']
            task_name = data['task_name']
            task_desc = data['task_desc']
            today_date = date_today()
            due_date = data['due_date']
            category = data['category']
            mb_obj.assign_tasks_to_user(task_id,user,task_name,task_desc,today_date,due_date,category,man_id),
        except Exception as e:
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
