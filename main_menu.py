import sys
from authentication.authentication import Authentication
from utils.config import Config
from manager.manager_controllers import Manager
from users.user_controllers import User

class MainMenu:
    @classmethod   
    def start(cls):
        print(Config.WELCOME_MESSAGE)
        print("\n")
        print(Config.LOGIN_SIGNUP_MENU)
        ch=input(Config.ENTER_YOUR_CHOICE)
        print('\n')
        if ch == "1":
            user_id,role=Authentication.login()
        elif ch == "2":
            Authentication.signUp()
            a = input(Config.ASK_FOR_LOGIN)   
            print('\n') 
            if a=='Y' or 'y':
                user_id,role=Authentication.login()
            else:
                sys.exit(2)
        else:
            print(Config.WRONG_INPUT_ENTERED_MESSAGE)
        ch=input(Config.ENTER_YOUR_CHOICE)
            
                
        
    
        if role == Config.MANAGER :
            print(Config.MANAGER_PROMPT)
            a=Manager(user_id)
            a.manager_menu()
        else :
            print(Config.USER_PROMPT)
            a=User(user_id)
            a.user_menu()