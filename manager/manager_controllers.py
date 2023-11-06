import sys
import shortuuid
from datetime import datetime
from pprint import pprint
from db.database_functions import add_data,update_data,fetch_data,display_data
from utils.config import Config
from tabulate import tabulate


class Manager:
    def __init__(self,user_id):
        self.user_id = user_id
        

    def manager_menu(self):
        user_input = input(Config.ENTER_YOUR_CHOICE)
        while user_input != '5':
            match user_input:
                case '1':
                    Manager.view_all_users()
                case '2':
                    self.assign_tasks_to_user()
                case '3':
                    self.view_status_of_assigned_tasks()
                case '4':
                   self.update_status_of_assigned_task()
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            user_input = input(Config.ENTER_YOUR_CHOICE)
        print(Config.THANKYOU)

    @staticmethod
    def view_all_users():
        display_data(Config.QUERY_TO_VIEW_ALL_USERS)

    def assign_tasks_to_user(self):
        print(Config.USERS_AVAILABLE)
        display_data(Config.QUERY_TO_VIEW_ALL_USERS)
        task_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        user=input(Config.ENTER_USER_ID)
        task_name = input(Config.TASK_TITLE)
        task_desc = input(Config.TASK_DESCRIPTION)
        date_created = datetime.now()
        due_date = input(Config.ENTER_DATE_IN_FORMAT)
        print(Config.TASKS_CATEGORY_PROMPT)
        cat_choice=input(Config.ENTER_YOUR_CHOICE)
        if cat_choice=='1' :
            category='Today'
        elif cat_choice=='2' :
            category='Important'
        else :
            category='For_later'
        
        add_data(Config.INSERT_INTO_TASKS_TABLE_BY_MANAGER,(task_id,user,task_name,task_desc,date_created,due_date,category,self.user_id))
        add_data(Config.INSERT_INTO_ASSIGNED_TASKS_TABLE,(self.user_id,user,task_id))
        print(Config.TASK_ASSIGNED_SUCCESSFULLY)

    def view_status_of_assigned_tasks(self):
        data = fetch_data(Config.VIEW_STATUS_OF_MY_ASSIGNED_TASKS,(self.user_id,))
        if len(data) == 0:
            print(Config.NO_DATA_FOUND)
        else:
            HEADERS = ['USER ID',"TASK ID","STATUS" ,"TASK NAME","TASK DESCRIPTION","DATE OF CREATION" ,"DUE DATE"]
            print(tabulate(data,headers=HEADERS , tablefmt = 'rounded_outline'))

        
        pprint(data)

    def update_status_of_assigned_task(self):
        display_data(Config.QUERY_TO_VIEW_ALL_USERS)
        task = input(Config.WHICH_TASK)
        status = input(Config.STATUS)
        update_data(Config.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS,(status,task))
        print(Config.TASK_STATUS_UPDATED)
