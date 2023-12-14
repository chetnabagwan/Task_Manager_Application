import time
import sys
import logging
import functools
from authentication.authentication import Authentication
from utils.config import Config
from manager.manager_controllers import Manager
from users.user_controllers import User

logger = logging.getLogger('app.main_menu')

class MainMenu:
    """Main menu class"""
    
    @classmethod
    def check_role(cls,role, user_id):
        
        if role == Config.MANAGER :
            print(Config.MANAGER_PROMPT_WLCM)                                            
            a = Manager(user_id)
            a.manager_menu()
            cls.start()
        else :
            print(Config.USER_PROMPT_WLCM)
            a = User(user_id)
            a.user_menu()
            cls.start()
        
    @classmethod
    def start(cls):
        print("\n")
        print(Config.LOGIN_SIGNUP_MENU)
        ch = input(Config.ENTER_YOUR_CHOICE)
        print('\n')
        while ch != 'q':
            if ch == Config.ONE:
                x=Authentication.login()
                if x is not None:
                    user_id,role = x
                    break
                else:
                    print(Config.ATTEMPTS_EXHAUSTED)
                    time.sleep(10)
            elif ch == Config.TWO:
                Authentication.sign_up()
                a = input(Config.ASK_FOR_LOGIN)
                print('\n')
                if a in (Config.UPPER_Y, Config.LOWER_Y):
                    user_id,role=Authentication.login()
                    break
                elif a in (Config.UPPER_N, Config.LOWER_N):
                    sys.exit()
            elif ch==Config.STR_THREE:
                sys.exit()
            else:
                print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            print(Config.LOGIN_SIGNUP_MENU)
            ch = input(Config.ENTER_YOUR_CHOICE)

        cls.check_role(role, user_id)
      


    


