from utils.config import Config
from db.database_functions import add_data,fetch_user
from utils.helper_functions import DataNotFoundError,hash_pwd,create_userid
from flask_jwt_extended import create_access_token,create_refresh_token

class Authentication:
    '''This class contains Authentication logic'''
    
    def register(self,username,password):
        hashed_pwd = hash_pwd(password)
        userid = create_userid()
        add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(userid,username,hashed_pwd,))

    
    def login(self,username,password):
            hashed_password = hash_pwd(password)
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            if user_data is None:
                raise DataNotFoundError('User not found')
            user_data[2] == hashed_password
            return user_data[0],user_data[3]

 
    def generate_access_token(self,user_id,role):
        token = create_access_token(identity=user_id,additional_claims={"role":role},fresh=True)
        return token
    

    def generate_refresh_token(self,user_id,role):
        token = create_refresh_token(identity=user_id,additional_claims={"role":role})
        return token
    

        
