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

        welcomemsg_role(role, user_id)
      

#decorator
def user_has_permission(func):     
    #wrapper function
    @functools.wraps(func)
    def check_role(*args):
        role, user_id = args
        if role == Config.MANAGER :                                            
            func(role, user_id)
            print(Config.MANAGER_PROMPT)
            a = Manager(user_id)
            a.manager_menu()
            MainMenu.start()
        else :
            func(role,user_id)
            print(Config.USER_PROMPT)
            a = User(user_id)
            a.user_menu()
            MainMenu.start()
    return check_role


@user_has_permission
    print(f'-----------Welcome {role.upper()}------------\n')
    
