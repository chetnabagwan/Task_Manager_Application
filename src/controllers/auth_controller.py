from flask_smorest import abort
from business.authentication import Authentication
from utils.helper_functions import DataNotFoundError
from blocklist import BLOCKLIST

authb_obj = Authentication()

class AuthController:
    '''Authenticatioon controller class which have signup, signin andlogout methods'''

    def RegisterController(self,register_data):
        '''Method for registering a new user'''

        username = register_data['username']
        password = register_data['password']
        authb_obj.register(username,password)
        return {'status_code':201,
                'message': 'Succesfully registered'}, 201
    
    
    def LoginController(self,login_data: dict):
            '''Method for user login'''

            username = login_data['username']
            password = login_data['password']
            try:    
                user_data = authb_obj.login(username,password)
                user_id,role = user_data

                access_token = authb_obj.generate_access_token(user_id,role)
                refresh_token = authb_obj.generate_refresh_token(user_id,role)
                
                return {"message":'successfully logged in',
                        "access_token" : access_token,
                        "refresh_token":refresh_token}

            except DataNotFoundError:
                abort(401,message="Invalid Credentials")
           

    def LogoutController(self,token_id):
        '''Method for user logout'''

        BLOCKLIST.add(token_id)

        return {'status_code':204,'message': 'Successfully logged out'},200
