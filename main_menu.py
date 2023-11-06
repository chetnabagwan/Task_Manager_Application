import sys
import logging
from authentication.authentication import Authentication
from utils.config import Config
from manager.manager_controllers import Manager
from users.user_controllers import User

logger = logging.getLogger('main.main_menu')

class MainMenu:
    @classmethod   
    def start(cls):
        print(Config.WELCOME_MESSAGE)
        print("\n")
        print(Config.LOGIN_SIGNUP_MENU)
        ch = input(Config.ENTER_YOUR_CHOICE)
        print('\n')
        while ch != 'q':
            if ch == Config.ONE:
                user_id,role=Authentication.login()
                break
            elif ch == Config.TWO:
                Authentication.signUp()
                a = input(Config.ASK_FOR_LOGIN)   
                print('\n') 
                if a==Config.UPPER_Y or Config.LOWER_Y:
                    user_id,role=Authentication.login()
                    break
                else:
                    sys.exit()
            elif ch==Config.STR_THREE:
                sys.exit()
            else:
                print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            ch = input(Config.ENTER_YOUR_CHOICE)
            
                
        if role == Config.MANAGER :
            print(Config.MANAGER_PROMPT)
            a=Manager(user_id)
            a.manager_menu()
            MainMenu.start()
        else :
            print(Config.USER_PROMPT)
            a=User(user_id)
            a.user_menu()
            MainMenu.start()