import sys
import shortuuid
from datetime import datetime,timedelta
from db.database_functions import add_data,update_data,fetch_data
from utils.config import Config
from tabulate import tabulate

class User:
    
    def __init__(self,user_id) -> None:
        self.user_id=user_id
    
    
    def user_menu(self):
        user_input = input(Config.ENTER_YOUR_CHOICE)
        while user_input != '6':
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
                    sys.exit()
                #case '6': back return
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            print(Config.NEXT)
            print(Config.USER_PROMPT)
            user_input = input(Config.ENTER_YOUR_CHOICE)
        print(Config.THANKYOU)

    
    def create_new_tasks(self): 
        task_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        task_name = input(Config.TASK_TITLE)
        task_desc= input(Config.TASK_DESCRIPTION)
        date_created = datetime.now()
        yesterday = date_created - timedelta(days=1)
        due_date = input(Config.ENTER_DATE_IN_FORMAT)
        if yesterday < due_date:
            pass
        else:
            print(Config.INVALID_DUE_DATE)
        print(Config.TASKS_CATEGORY_PROMPT)
        cat_choice=input(Config.ENTER_YOUR_CHOICE)
        if cat_choice=='1' :
            category='Today'
        elif cat_choice=='2' :
            category='Important'
        else :
            category='For_later'
        
        add_data(Config.INSERT_INTO_TASKS_TABLE,(task_id,self.user_id,task_name,task_desc,date_created,due_date,category))
        print(Config.TASK_ADDED_SUCCESSFULLY)

    def update_my_tasks(self):
        task_name = input(Config.TASK_NAME_TO_UPDATE)
        print(Config.UPDATE_TASKS_OPTIONS)
        ch=input(Config.ENTER_YOUR_CHOICE)
        if ch== '1' :
            updated_date=input(Config.ENTER_DATE_IN_FORMAT)
            update_data(Config.UPDATE_DUE_DATE,(updated_date,task_name))
            print(Config.TASK_DUE_DATE_UPDATED)
        else :
            update_data(Config.UPDATE_TASK_STATUS,(task_name,))
            print(Config.TASK_STATUS_UPDATED)

    def view_my_tasks(self):
        data=fetch_data(Config.VIEW_TASKS,(self.user_id,))
        if len(data) == 0 :
            print(Config.NO_DATA_FOUND)
        else:
            print(Config.YOUR_TASKS_ARE)
            print("\n")
            HEADERS = ["TASK ID","USER ID","TASK NAME" ,"TASK DESCRIPTION","DATE OF CREATION","DUE DATE","IS COMPLETED","CATEGORY","ASSIGNED BY"]
            print(tabulate(data,headers=HEADERS,tablefmt='rounded_outline'))

    def delete_my_tasks(self):
        data=fetch_data(Config.VIEW_TASKS_TO_DELETE,(self.user_id,))
        if len(data) == 0 :
            print(Config.NO_TASKS_FOUND_TO_BE_DELETED)
        else:
            print(Config.TASKS_THAT_CAN_BE_DELETED)
            HEADERS = ["TASK ID","USER ID","TASK NAME" ,"TASK DESCRIPTION","DATE OF CREATION","DUE DATE","IS COMPLETED","CATEGORY","ASSIGNED BY"]
            print(tabulate(data,headers=HEADERS,tablefmt='rounded_outline'))
        
            print("\n")
            task_id = input(Config.WHICH_TASK_TO_DELETE)
            update_data(Config.DELETE_MY_TASKS,(self.user_id,task_id))
            print(Config.TASK_DELETED_SUCCESSFULLY)
