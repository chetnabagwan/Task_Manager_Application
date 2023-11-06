import hashlib
from pwinput import pwinput
from utils.input_validation import password_validation
from utils.config import Config
import shortuuid
from db.database_functions import add_data,fetch_user


class Authentication:
    def __init__():  
        pass

    @classmethod
    def login(self):
        print(Config.PRINT_LOGIN)
        print("\n")
        attempts = Config.ATTEMPTS

        while attempts:
            username = input(Config.PRINT_USERNAME)
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            user_data = fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
            #print(user_data)
            if user_data == None:
                print(f"{Config.LOGIN_FAILED} {attempts}/3")
                attempts=attempts-1               
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
        name = input(Config.PRINT_USERNAME)
        while True:
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            if not password_validation(password):
                print(Config.ENTER_STRONG_PASSWORD)
                print(Config.PASSWORD_REQUIREMENTS)
            else:
                break
        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
        userid = int(shortuuid.ShortUUID('123456789').random(length=4))
        add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(userid,name,hashed_pwd,))
        print(Config.SIGNUP_SUCCESSFUL)
            
       
        
   

   