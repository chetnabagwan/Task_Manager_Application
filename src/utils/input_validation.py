"""This file contains the input validations functions."""

import re
import logging
from datetime import datetime
from .config import Config


logger = logging.getLogger('Validations')

class InputValidations:

    @staticmethod
    def password_validator(password):

        """Validates the password entered whether it meets the password requirements or not."""

        pat = re.compile(Config.PWD_REGEX)
        answer = re.search(pat,password)
        
        if answer is not None:
            return True
        else:
            return False

    @staticmethod
    def gen_validator(input):
        
        """Validates the input entered."""
        pat = re.compile(Config.GEN_REGEX)
        ans = re.match(pat,input)
        if ans is not None:
            return True
        else:
            return False

    @staticmethod  
    def task_name_validator():
        while True:
            tname = input(Config.TASK_TITLE)
            if InputValidations.gen_validator(tname) is False:
                print(Config.INVALID_INPUT)
            return tname

    @staticmethod
    def task_desc_validator():
        while True:
            tdesc = input(Config.TASK_DESCRIPTION)
            if InputValidations.gen_validator(tdesc) is False:
                print(Config.INVALID_INPUT)
            return tdesc
   
    @staticmethod
    def date_validator(user_id,today_date):
        while True:
            d1= input(Config.ENTER_DATE_IN_FORMAT)
            d_date = datetime.strptime(str(d1),"%d-%m-%Y")
            due_date = d_date.strftime("%d-%m-%Y")
            if due_date < today_date:
                print(Config.INVALID_DUE_DATE)
                logger.info(f'Manager:{user_id} has given invalid duedate')
            return due_date
        
    @staticmethod
    def task_category_validator():
        while True:
            print(Config.TASKS_CATEGORY_PROMPT)
            cat_choice=input(Config.ENTER_YOUR_CHOICE)
            if cat_choice == Config.ONE :
                return Config.TODAY
            elif cat_choice == Config.TWO :
                return Config.IMPORTANT
            elif cat_choice == Config.STR_THREE:
                return Config.FOR_LATER
            else :
                print(Config.WRONG_INPUT_ENTERED_MESSAGE)

    @staticmethod
    def userid_validator():
        while True:
            id = input(Config.ENTER_USER_ID)
            if re.match(Config.ID_REGEX,id):
                return id
            print(Config.INVALID_INPUT)

    @staticmethod
    def taskid_validator():
        while True:
            id = input(Config.ENTER_TASK_ID).strip() 
            if re.match(Config.ID_REGEX,id):
                return id
            print(Config.INVALID_INPUT)


    @staticmethod
    def task_status_validator():
        while True:
            s = input(Config.STATUS)
            if s == Config.STR_ZERO:
                return Config.REASSIGNED
            elif s == Config.ONE:
                return Config.COMPLETED
            else:
                print(Config.INVALID_INPUT)   

    
    

    