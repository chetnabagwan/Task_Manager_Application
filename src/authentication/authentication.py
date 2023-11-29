import hashlib
import shortuuid
from pwinput import pwinput
from utils.input_validation import InputValidations
from utils.config import Config
from db.database_functions import add_data,fetch_user


class Authentication:
    def __init__():  
        pass

    @classmethod
    def login(self):
        print(Config.PRINT_LOGIN)
        attempts = Config.ATTEMPTS

        while attempts:
            while True:
                username = input(Config.PRINT_USERNAME).strip() 
                if InputValidations.gen_validator(username) is False:
                    print(Config.INVALID_USERNAME)
                else:
                    break
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            #print(user_data)
            if user_data == None:
                attempts=attempts-1 
                print(f"{Config.LOGIN_FAILED} {attempts}/{Config.THREE }")
                            
            elif user_data[2] == hashed_password:
                print(Config.LOGIN_SUCCESSFUL)
                break 
            else:
                print(Config.INVALID_CREDENTIALS)
                  
            
        if attempts <= 0:
            return None
        else:
            return user_data[0],user_data[3] 
    
    @classmethod
    def signUp(self):
        while True:
                username = input(Config.PRINT_USERNAME).strip() 
                if InputValidations.gen_validator(username) is False:
                    print(Config.INVALID_USERNAME)
                else:
                    break
        while True:
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            if not InputValidations.password_validation(password):
                print(Config.ENTER_STRONG_PASSWORD)
                print(Config.PASSWORD_REQUIREMENTS)
            else:
                break
        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
        userid = int(shortuuid.ShortUUID('123456789').random(length=4))
        add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(userid,username,hashed_pwd,))
        print(Config.SIGNUP_SUCCESSFUL)
            
       
        
   

   