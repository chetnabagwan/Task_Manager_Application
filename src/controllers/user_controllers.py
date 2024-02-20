import logging
from flask import abort
from business.user import User
from utils.helper_functions import DataNotFoundError,NotAuthorizedError,create_id,date_today
from utils.config import Config

logger = logging.getLogger('main.user_controllers')

ub_obj = User()
from utils.config import Config

class UserController:
    
    def myprofile(self,token):
        """This method shows the user profile"""
        logger.info('User is viewing his/her profile')
        try:
            r = token['role']
            if r != 'user':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            user_id = token['sub']
            profile_data = ub_obj.myprofile(user_id)
            return profile_data
        except Exception as e:
            raise e

    def update_my_profile(self,token,data):
        """This method Updates user's profile information"""
        logger.info('User is updating his/her profile')
        try:
            r = token['role']
            if r != 'user':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            user_id = token['sub'] 
            name = data['name']
            email = data['email']
            phone_number = data['phone_number']
            ub_obj.update_my_profile(user_id,name,email,phone_number)  
            return {'message' : 'Profile information updated successfully!'}
        except Exception as e:
            raise e
    

    def view_my_tasks(self,token):
        """This method allows a user to view his/her all tasks"""

        logger.info('User is viewing tasks.')
        try:    
            r = token['role']
            if r != 'user':
                logger.warning(f'Unauthorized user {token["sub"]} is assigning tasks to users.')
                raise NotAuthorizedError
            user_id = token['sub']
            tasks = ub_obj.view_my_tasks(user_id)
            print(tasks)
            if not tasks:
                return {"tasks": []}
            return tasks
        except Exception as e:
            raise e

    


   