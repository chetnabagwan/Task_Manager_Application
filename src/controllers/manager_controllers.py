import logging
from flask_smorest import abort
from business.manager import Manager
from utils.helper_functions import DataNotFoundError,NotAuthorizedError,create_id,date_today
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
