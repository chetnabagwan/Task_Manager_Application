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
            print(data)
            return data
        except Exception as e:
            raise e
            # abort(404,detail= "No data found")


    def view_status_of_assigned_tasks(self,token):
        """This method shows status of tasks assigned by particular manager. """

        logger.info('Manager is trying to view status of assigned tasks')
        try:    
            r = token['role']
            if r != 'manager':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                abort(403,detail= "Not authorized")
            man_id = token['sub']
            return mb_obj.view_status_of_assigned_tasks_logic(man_id)
        except Exception as e:
            raise e


  
