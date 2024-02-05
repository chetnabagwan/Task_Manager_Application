from flask_jwt_extended import create_access_token,create_refresh_token
import logging
from utils.config import Config
from db.database_functions import add_data,fetch_user
from utils.helper_functions import DataNotFoundError,hash_pwd,create_userid

logger = logging.getLogger(__name__)
class Authentication:
    '''This class contains Authentication logic'''
    
    def register(self,username,password):
        '''Method to signup'''
        hashed_pwd = hash_pwd(password)
        userid = create_userid()
        add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(userid,username,hashed_pwd,))
        logger.info(f'Adding userdata of {username} into database')

    
    def login(self,username,password):
            '''Method to signin'''
        
            hashed_password = hash_pwd(password)
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            if user_data is None:
                logger.info(f'No user found with username : {username}')
                raise DataNotFoundError('User not found')
            user_data[2] == hashed_password
            return user_data[0],user_data[3]

 
    def generate_access_token(self,user_id,role):
        '''Method for generating access token'''

        token = create_access_token(identity=user_id,additional_claims={"role":role},fresh=True)
        return token
    

    def generate_refresh_token(self,user_id,role):
        '''Method for generating refresh token'''

        token = create_refresh_token(identity=user_id,additional_claims={"role":role})
        return token
    

        
