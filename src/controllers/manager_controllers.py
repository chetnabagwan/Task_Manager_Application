import logging
from flask_smorest import abort
from business.manager import Manager
from utils.helper_functions import DataNotFoundError,NotAuthorizedError,create_userid,date_today
from utils.config import Config
from pymysql import DatabaseError

logger = logging.getLogger('main.manager_controllers')

mb_obj = Manager()

class ManagerController:

    def get_all_users(self,token):
        '''This method displays all users present in the database'''
        
        logger.info(f'Manager is viewing all users')
        try:
            r = token['role']
            if r != 'manager':
                abort(403,detail= "Not authorized")
            data = mb_obj.get_all_users_logic()
            return data
        except DatabaseError:
            abort(404,detail= "No data found")


    def assign_tasks_to_user(self,token,data):
        '''This method assigns tasks to a user.'''

        logger.info(f'Manager is assigning tasks to users.')
        try:    
            r = token['role']
            if r != 'manager':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            man_id = token['sub']
            task_id = create_userid()
            user_id = data['user_id']
            task_name = data['task_name']
            task_desc = data['task_desc']
            today_date = date_today()
            due_date = data['due_date']
            category = data['category']
            mb_obj.assign_tasks_to_user_logic(task_id,user_id,task_name,task_desc,today_date,due_date,category,man_id)
        except Exception as e:
            raise e

    def view_status_of_assigned_tasks(self,token):
        """This method shows status of tasks assigned by particular manager. """

        logger.info(f'Manager:{man_id} is trying to view status of assigned tasks')
        try:    
            r = token['role']
            if r != 'manager':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            man_id = token['sub']
            mb_obj.view_status_of_assigned_tasks_logic(man_id)
        except Exception as e:
            raise e


    def update_taskstatus(self,token,data):
        logger.info(f'Manager:{man_id} is trying to view status of assigned tasks')
        try:    
            r = token['role']
            if r != 'manager':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            man_id = token['sub']
            task_id = data['task_id']
            status = data['status']
            mb_obj.update_status_of_assigned_task(task_id,status)
        except Exception as e:
            raise e
