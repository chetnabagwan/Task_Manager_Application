from utils.helper_functions import DataNotFoundError,create_id
from db.database_functions import write_to_database,update_data,fetch_data
from utils.config import Config

class User:
    '''This class contains user operations logic'''
    def myprofile(self,user_id):
        """This methods displays user profile"""
        try:
            data = fetch_data(Config.VIEW_MY_PROFILE,(user_id,))
            return data[0] 
        except Exception as e:
            raise e

    def update_my_profile(self,user_id,name,email,phone_number):
        """This method updates user's profile info"""
        try:
            update_data(Config.UPDATE_MY_PROFILE,(name,email,phone_number,user_id))
        except Exception as e:
            raise e


   

    def view_my_tasks(self,user_id):
        """This method allows a user to view his/her tasks"""
      
        try:
            data=fetch_data(Config.VIEW_TASKS,(user_id,))
            return data
        except Exception as e:
            raise e

