import sqlite3
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt
import logging
from utils.config import Config
from db.database_functions import write_to_database,fetch_user
from utils.helper_functions import DataNotFoundError,hash_pwd,create_id

logger = logging.getLogger(__name__)
class Authentication:
    '''This class contains Authentication logic'''
    
    def register(self,username,password,name,email,phone_number,gender):
        '''Method to signup'''
        hashed_pwd = hash_pwd(password)
        userid = create_id()
        try:
            write_to_database([Config.QUERY_TO_ADD_IN_AUTH_TABLE,Config.QUERY_TO_ADD_IN_USERS_TABLE],[(userid,username,hashed_pwd,),(userid,name,email,phone_number,gender,)])
            logger.info(f'Adding userdata of {username} into database')
        except sqlite3.Error as e:
            raise e

    
    def login(self,username,password):
            '''Method to signin'''
        
            hashed_password = hash_pwd(password)
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            # print(user_data)
            if user_data is None:
                logger.info(f'No user found with username : {username}')
                raise DataNotFoundError('User not found')
            user_data['password'] == hashed_password
            return user_data['user_id'],user_data['role']

 
    def generate_access_token(self,user_id,role):
        '''Method for generating access token'''

        token = create_access_token(identity=user_id,additional_claims={"role":role},fresh=True)
        return token
    

    def generate_refresh_token(self,user_id,role):
        '''Method for generating refresh token'''

        token = create_refresh_token(identity=user_id,additional_claims={"role":role})
        return token
    
 
        
