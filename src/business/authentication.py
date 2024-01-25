import shortuuid
from utils.config import Config
from db.database_functions import add_data,fetch_user
from utils.helper_functions import hash_pwd


class Authentication:

    @staticmethod
    def login(username,password):
            hashed_password = hash_pwd(password)
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            if user_data is None:
                raise 
            elif user_data[2] == hashed_password:
                return user_data[0],user_data[3]
            else:
                raise "Invalid Login"


    @staticmethod
    def sign_up(username,password):
        hashed_pwd = hash_pwd(password)
        userid = int(shortuuid.ShortUUID('123456789').random(length=4))
        add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(userid,username,hashed_pwd,))
        
