from flask_smorest import abort
import logging
from business.authentication import Authentication
from utils.config import Config
from utils.helper_functions import DataNotFoundError
from blocklist import BLOCKLIST

logger = logging.getLogger(__name__)

authb_obj = Authentication()

class AuthController:
    '''Authenticatioon controller class which have signup, signin andlogout methods'''

    def RegisterController(self,register_data):
        '''Method for registering a new user'''

        username = register_data['username']
        logger.info(f'User with username : {username} is registering into the application')
        password = register_data['password']
        authb_obj.register(username,password)
        return {'status_code':201,
                'message': Config.SIGNUP_SUCCESSFUL}, 201
    
    
    def LoginController(self,login_data: dict):
            '''Method for user login'''

            username = login_data['username']
            logger.info(f'User with username : {username} tries to login into the application')
            password = login_data['password']
            try:    
                user_data = authb_obj.login(username,password)
                user_id,role = user_data

                access_token = authb_obj.generate_access_token(user_id,role)
                refresh_token = authb_obj.generate_refresh_token(user_id,role)
                
                return {"message":Config.LOGIN_SUCCESSFUL,
                        "access_token" : access_token,
                        "refresh_token":refresh_token}

            except DataNotFoundError:
                logger.warning(f'User with username : {username} failed,Invalid credentials')
                abort(401,message=Config.INVALID_CREDENTIALS)
           

    def LogoutController(self,token_id):
        '''Method for user logout'''

        BLOCKLIST.add(token_id)
        logger.info(f'User logged out of the application')
        return {'status_code':204,'message':Config.LOGOUT_SUCCESSFUL},200
