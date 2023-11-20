import shortuuid
import logging
import sys
import os
from datetime import datetime
from utils.input_validation import username_validator
from db.database_functions import add_data,update_data,fetch_data,display_data
from utils.config import Config
from tabulate import tabulate

logger = logging.getLogger('main.manager_controllers')

class Manager:
    def __init__(self,user_id):
        self.user_id = user_id
        

    def manager_menu(self):
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
        logger.info(f'Manager:{self.user_id} is viewing all users')
        users = display_data(Config.QUERY_TO_VIEW_ALL_USERS)
        HEADERS = ["USER ID","USERNAME"]
        print(tabulate(users,headers=HEADERS,tablefmt='rounded_outline'))

    def assign_tasks_to_user(self):
        logger.info(f'Manager:{self.user_id} is assigning tasks to users.')
        print(Config.USERS_AVAILABLE)
        self.view_all_users()
        task_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        while True:
            user = input(Config.ENTER_USER_ID).strip() 
            if len(user) < 4 and len(user) >4 :
                print(Config.INVALID_INPUT)
            else:
                break
        while True:
            task_name = input(Config.TASK_TITLE).lower().strip() 
            if username_validator(task_name) is False  :
                print(Config.INVALID_INPUT)
            elif len(task_name) == 0:
                print(Config.INVALID_INPUT)
            else:
                break
        while True:
            task_desc = input(Config.TASK_DESCRIPTION).lower().strip() 
            if username_validator(task_desc) is False :
                print(Config.INVALID_INPUT)
            elif len(task_desc) == 0:
                print(Config.INVALID_INPUT)
            else:
                break

        d = datetime.now()
        today_date = datetime.strptime((datetime.strftime(d,"%d-%m-%Y")),"%d-%m-%Y")
        while True:
            d1= input(Config.ENTER_DATE_IN_FORMAT)
            due_date = datetime.strptime(str(d1),"%d-%m-%Y")
            if due_date < today_date:
                print(Config.INVALID_DUE_DATE)
                logger.info(f'Manager:{self.user_id} has given invalid duedate')
            else :
                break

        print(Config.TASKS_CATEGORY_PROMPT)
        cat_choice=input(Config.ENTER_YOUR_CHOICE)
        if cat_choice == Config.ONE:
            category = Config.TODAY
        elif cat_choice == Config.TWO :
            category = Config.IMPORTANT
        else :
            category = Config.FOR_LATER
        
        add_data(Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,(task_id,user,task_name,task_desc,date_created,due_date,category,self.user_id))
        add_data(Config.INSERT_INTO_ASSIGNED_TASKS_TABLE,(self.user_id,user,task_id))
        print(Config.TASK_ASSIGNED_SUCCESSFULLY)

    def view_status_of_assigned_tasks(self):
        logger.info(f'Manager:{self.user_id} is trying to view status of assigned tasks')
        data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
        if len(data) == 0:
            print(Config.NO_DATA_FOUND)
        else:
            HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
            print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))

    def update_status_of_assigned_task(self):
        logger.info(f'Manager:{self.user_id} is updating status of assigned tasks')
        data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
        if len(data) == 0:
            print(Config.NO_DATA_FOUND)
        else:
            HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
            print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))
            
            task = input(Config.WHICH_TASK).strip()
            while len(task) == 0 or len(task) > 4:
                print(Config.INVALID_INPUT)
                task = input(Config.WHICH_TASK).strip()
            
            data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))
            while len(data) == 0:
                print(Config.TASKID_NOT_FOUND)
                task = input(Config.WHICH_TASK).strip()
                data = fetch_data(Config.QUERY_TO_FETCH_ALL_TASK_IDS,(task,))

            status =""
            while True:
                s = input(Config.STATUS)
                if s == '0':
                    status = "pending"
                    break
                elif s=='1':
                    status = "completed"
                    break
                else:
                    print(Config.INVALID_INPUT)
                    
                
            update_data(Config.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS,(status,task))
            print(Config.TASK_STATUS_UPDATED)
