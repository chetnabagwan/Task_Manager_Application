import shortuuid
import logging
import sys
import os
from datetime import datetime
from tabulate import tabulate
from utils.input_validation import InputValidations
from db.database_functions import add_data,update_data,fetch_data,display_data
from utils.config import Config

logger = logging.getLogger('main.manager_controllers')

class Manager:
    def __init__(self,user_id):
        self.user_id = user_id
        

    def manager_menu(self):

        """This method displays choices to manager,operations he/she can perform."""

        user_input = input(Config.ENTER_YOUR_CHOICE)
        while True:
            while user_input != 'q':
                match user_input:
                    case '1':
                        self.view_all_users()
                        
                    case '2':
                        self.assign_tasks_to_user()
                    case '3':
                        self.view_status_of_assigned_tasks()
                    case '4':
                        self.update_status_of_assigned_task()
                    case '5':
                        os.system('cls') 
                        return
                    case '6':
                        sys.exit()
                    case _:
                        print(Config.WRONG_INPUT_ENTERED_MESSAGE)
                print(Config.NEXT)
                print(Config.MANAGER_PROMPT)
                user_input = input(Config.ENTER_YOUR_CHOICE)
                
            print(Config.THANKYOU)
  
    def view_all_users(self):

        """This method displays all users present in the database"""

        logger.info(f'Manager:{self.user_id} is viewing all users')
        users = display_data(Config.QUERY_TO_VIEW_ALL_USERS)
        HEADERS = ["USER ID","USERNAME"]
        print(tabulate(users,headers=HEADERS,tablefmt='rounded_outline'))


    def assign_tasks_to_user(self):

        """This method assigns tasks to a selected user."""

        logger.info(f'Manager:{self.user_id} is assigning tasks to users.')
        print(Config.USERS_AVAILABLE)
        self.view_all_users()
        task_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        user = InputValidations.userid_validator()
        task_name = InputValidations.task_name_validator()
        task_desc = InputValidations.task_desc_validator()
        today_date = datetime.strptime((datetime.strftime(datetime.now(),"%d-%m-%Y")),"%d-%m-%Y").strftime("%d-%m-%Y")
        due_date = InputValidations.date_validator(self.user_id,today_date)
        category = InputValidations.task_category_validator()
        add_data(Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,(task_id,user,task_name,task_desc,today_date,due_date,category,self.user_id))
        add_data(Config.INSERT_INTO_ASSIGNED_TASKS_TABLE,(self.user_id,user,task_id))
        print(Config.TASK_ASSIGNED_SUCCESSFULLY)


    def view_status_of_assigned_tasks(self):

        """This method shows status of tasks assigned by particular manager. """

        logger.info(f'Manager:{self.user_id} is trying to view status of assigned tasks')
        data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
        if len(data) == 0:
            print(Config.NO_DATA_FOUND)
        else:
            HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
            print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))


    def update_status_of_assigned_task(self):

        """Updates status of a selected task."""

        logger.info(f'Manager:{self.user_id} is updating status of assigned tasks')
        data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
        if len(data) == 0:
            print(Config.NO_DATA_FOUND)
        else:
            HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
            print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))
            print(Config.WHICH_TASK)
            task = InputValidations.user_or_task_id_validator()
            data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))
            while len(data) == 0:
                print(Config.TASKID_NOT_FOUND)
                task = InputValidations.taskid_validator()
                data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))
            status = InputValidations.task_status_validator() 
            update_data(Config.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS,(status,task))
            print(Config.TASK_STATUS_UPDATED)
