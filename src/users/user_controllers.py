import sys
import os
import shortuuid
import logging
from datetime import datetime
from tabulate import tabulate
from utils.input_validation import InputValidations
from db.database_functions import add_data,update_data,fetch_data
from utils.config import Config

logger = logging.getLogger('main.user_controllers')

class User:
    
    def __init__(self,user_id) -> None:
        self.user_id=user_id
    
    def user_menu(self):

        """Displays user prompt and user can make choice accordingly"""

        user_input = input(Config.ENTER_YOUR_CHOICE)
        while user_input != 'q':
            match user_input:
                case '1':
                    self.create_new_tasks()
                case '2':
                    self.update_my_tasks()
                case '3':
                    self.view_my_tasks()
                case '4':
                    self.delete_my_tasks()
                case '5':
                    os.system('cls') 
                    return
                case '6':
                    sys.exit()
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            print(Config.NEXT)
            print(Config.USER_PROMPT)
            user_input = input(Config.ENTER_YOUR_CHOICE)
        print(Config.THANKYOU)
           

    def create_new_tasks(self): 

        """This method creates new task for user"""

        logger.info(f'User:{self.user_id} is creating new tasks.')

        task_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        task_name = InputValidations.task_name_validator()
        task_desc = InputValidations.task_desc_validator()
        fdate = datetime.strptime((datetime.strftime(datetime.now(),"%d-%m-%Y")),"%d-%m-%Y")
        today_date = fdate.strftime("%d-%m-%Y")
        due_date = InputValidations.date_validator(self.user_id,today_date)
        category = InputValidations.task_category_validator()     
        add_data(Config.INSERT_INTO_TASKS_TABLE,(task_id,self.user_id,task_name,task_desc,today_date,due_date,category))
        print(Config.TASK_ADDED_SUCCESSFULLY)


    def view_my_tasks(self):

        """This method allows a user to view his/her tasks"""

        logger.info(f'User:{self.user_id} is viewing tasks.')
        data=fetch_data(Config.VIEW_TASKS,(self.user_id,))
        if len(data) == 0 :
            print(Config.NO_DATA_FOUND)
        else:
            print(Config.YOUR_TASKS_ARE)   
            HEADERS = ["TASK ID","USER ID","TASK NAME" ,"TASK DESCRIPTION","DATE OF CREATION","DUE DATE","IS COMPLETED","CATEGORY","ASSIGNED BY"]
            print(tabulate(data,headers=HEADERS,tablefmt='rounded_outline'))


    def update_my_tasks(self):

        """This method helps user to update his/her tasks. User can update both status and duedate of a task"""
        
        logger.info(f'User:{self.user_id} is updating tasks.')
        self.view_my_tasks()
        task_name = InputValidations.task_name_validator()
        print(Config.UPDATE_TASKS_OPTIONS)
        ch=input(Config.ENTER_YOUR_CHOICE)
        if ch== Config.ONE :
            date = datetime.strptime((datetime.strftime(datetime.now(),"%d-%m-%Y")),"%d-%m-%Y")
            today_date = date.strftime("%d-%m-%Y")
            updated_date = InputValidations.date_validator(self.user_id,today_date)
            update_data(Config.UPDATE_DUE_DATE,(updated_date,task_name))
            print(Config.TASK_DUE_DATE_UPDATED)
        else :
            update_data(Config.UPDATE_TASK_STATUS,(task_name,))
            print(Config.TASK_STATUS_UPDATED)


    def delete_my_tasks(self):

        """This method deletes a selected task."""

        logger.info(f'User:{self.user_id} is trying to delete tasks.')
        data=fetch_data(Config.VIEW_TASKS_TO_DELETE,(self.user_id,))
        if len(data) == 0 :
            print(Config.NO_TASKS_FOUND_TO_BE_DELETED)
        else:
            print(Config.TASKS_THAT_CAN_BE_DELETED)
            HEADERS = ["TASK ID","USER ID","TASK NAME" ,"TASK DESCRIPTION","DATE OF CREATION","DUE DATE","IS COMPLETED","CATEGORY","ASSIGNED BY"]
            print(tabulate(data,headers=HEADERS,tablefmt='rounded_outline'))
            task_id = InputValidations.taskid_validator()
            update_data(Config.DELETE_MY_TASKS,(self.user_id,task_id))
            print(Config.TASK_DELETED_SUCCESSFULLY)
