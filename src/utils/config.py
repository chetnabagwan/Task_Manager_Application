import yaml
import os

path_current_directory = os.path.dirname(__file__)
FPATH = os.path.join(path_current_directory, '../yml_files/prompts.yml')
FPATH_PRINT_STATEMENTS = os.path.join(path_current_directory, '../yml_files/print_statements.yml')
F_PATH_MANAGER_QUERIES = os.path.join(path_current_directory, '../db/queries/manager_queries.yml')
F_PATH_USER_QUERIES = os.path.join(path_current_directory, '../db/queries/user_queries.yml')

class Config:
    
    USER_PROMPT_WLCM  =None
    MANAGER_PROMPT_WLCM = None
    PASSWORD_REQUIREMENTS = None
    MANAGER = None
    ATTEMPTS = None
    WELCOME_MESSAGE = None
    WRONG_INPUT_ENTERED_MESSAGE = None
    ROW_NOT_EXISTS_MESSAGE =None
    PRINT_USERNAME = None
    PRINT_PASSWORD = None
    ENTER_STRONG_PASSWORD = None
    ENTER_ROLE = None
    WELCOME_MANAGER_MESSAGE = None
    WELCOME_USER_MESSAGE = None
    PRINT_LOGIN = None
    LOGIN_FAILED = None
    LOGIN_SIGNUP_MENU = None
    NO_DATA_FOUND = None
    YOUR_TASKS_ARE = None
    NO_TASKS_FOUND_TO_BE_DELETED = None
    TASK_ADDED_SUCCESSFULLY = None
    TASK_DELETED_SUCCESSFULLY = None
    TASK_DUE_DATE_UPDATED = None
    TASK_STATUS_UPDATED = None
    ENTER_YOUR_CHOICE = None
    ASK_FOR_LOGIN = None
    INVALID_CREDENTIALS = None
    LOGIN_SUCCESSFUL = None
    SIGNUP_SUCCESSFUL = None
    THANKYOU = None 
    TASK_ASSIGNED_SUCCESSFULLY = None
    INVALID_DUE_DATE = None
    NEXT = None
    ENTER_DATE_IN_FORMAT = None
    TASK_TITLE = None
    TASK_DESCRIPTION = None
    TASK_NAME_TO_UPDATE = None
    TASKS_THAT_CAN_BE_DELETED = None
    WHICH_TASK_TO_DELETE = None
    ENTER_USER_ID = None
    ENTER_TASK_ID = None
    USERS_AVAILABLE = None
    WHICH_TASK = None
    STATUS = None
    ONE = None
    TWO = None
    UPPER_Y =None
    LOWER_Y = None
    UPPER_N =None
    LOWER_N = None
    TODAY = None
    IMPORTANT = None
    FOR_LATER = None
    THREE = None
    STR_THREE = None
    INVALID_USERNAME = None
    INVALID_INPUT = None
    TASKID_NOT_FOUND = None
    ATTEMPTS_EXHAUSTED = None
    DB_CONNECTION_ERROR = None
    GEN_REGEX = None
    PWD_REGEX = None
    ID_REGEX = None
    PARAMS = None
    JWT_SECRET_KEY = None

    
    QUERY_FOR_CREATE_AUTH_TABLE = None
    QUERY_FOR_CREATE_TASKS_TABLE= None
    QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE = None
    QUERY_TO_ENABLE_FOREIGN_KEY = None
    QUERY_TO_ADD_IN_AUTH_TABLE = None
    QUERY_TO_VERIFY_LOGIN = None
    QUERY_TO_VIEW_ALL_USERS = None
    INSERT_INTO_TASKS_TABLE_BY_MANAGER = None
    INSERT_INTO_ASSIGNED_TASKS_TABLE = None
    VIEW_STATUS_OF_MY_ASSIGNED_TASKS  = None
    UPDATE_STATUS_OF_MY_ASSIGNED_TASKS = None
    QUERY_TO_FETCH_ALL_TASK_IDS = None

    INSERT_INTO_TASKS_TABLE = None
    TASKS_CATEGORY_PROMPT = None
    UPDATE_TASKS_OPTIONS = None
    UPDATE_DUE_DATE =None
    UPDATE_TASK_STATUS = None
    VIEW_TASKS = None
    DELETE_MY_TASKS =None
    VIEW_TASKS_TO_DELETE =None

    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.MANAGER_PROMPT_WLCM = data['MANAGER_PROMPT_WLCM']
            cls.USER_PROMPT_WLCM = data['USER_PROMPT_WLCM']
            cls.ATTEMPTS = data['ATTEMPTS']
            cls.PASSWORD_REQUIREMENTS = data['PASSWORD_REQUIREMENTS']
            cls.MANAGER = data['MANAGER']
            cls.GEN_REGEX = data['GEN_REGEX']
            cls.PWD_REGEX = data['PWD_REGEX']
            cls.ID_REGEX = data['ID_REGEX']
            cls.REASSIGNED = data['REASSIGNED']
            cls.COMPLETED = data['COMPLETED']
   
          
    @classmethod
    def load_print_statements(cls):
        with open(FPATH_PRINT_STATEMENTS,'r') as f:
            data = yaml.safe_load(f)           
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ROW_NOT_EXISTS_MESSAGE = data['ROW_NOT_EXISTS_MESSAGE']
            cls.WRONG_INPUT_ENTERED_MESSAGE = data['WRONG_INPUT_ENTERED_MESSAGE']
            cls.PRINT_USERNAME = data['PRINT_USERNAME']
            cls.PRINT_PASSWORD = data['PRINT_PASSWORD']
            cls.ENTER_STRONG_PASSWORD = data['ENTER_STRONG_PASSWORD']
            cls.ENTER_ROLE = data['ENTER_ROLE']
            cls.WELCOME_MANAGER_MESSAGE = data['WELCOME_MANAGER_MESSAGE']
            cls.WELCOME_USER_MESSAGE : ['Welcome User']
            cls.PRINT_LOGIN = data['PRINT_LOGIN']
            cls.LOGIN_FAILED = data['LOGIN_FAILED']
            cls.LOGIN_SIGNUP_MENU = data['LOGIN_SIGNUP_MENU']
            cls.NO_DATA_FOUND = data['NO_DATA_FOUND']
            cls.YOUR_TASKS_ARE = data['YOUR_TASKS_ARE']
            cls.NO_TASKS_FOUND_TO_BE_DELETED = data['NO_TASKS_FOUND_TO_BE_DELETED']
            cls.TASK_ADDED_SUCCESSFULLY = data['TASK_ADDED_SUCCESSFULLY']
            cls.TASK_DELETED_SUCCESSFULLY = data['TASK_DELETED_SUCCESSFULLY']
            cls.TASK_DUE_DATE_UPDATED = data['TASK_DUE_DATE_UPDATED']
            cls.TASK_STATUS_UPDATED = data['TASK_STATUS_UPDATED']
            cls.ENTER_YOUR_CHOICE = data['ENTER_YOUR_CHOICE']
            cls.ASK_FOR_LOGIN = data['ASK_FOR_LOGIN']
            cls.INVALID_CREDENTIALS = data['INVALID_CREDENTIALS']
            cls.LOGIN_SUCCESSFUL = data['LOGIN_SUCCESSFUL']
            cls.SIGNUP_SUCCESSFUL = data['SIGNUP_SUCCESSFUL']
            cls.THANKYOU = data['THANKYOU'] 
            cls.TASK_ASSIGNED_SUCCESSFULLY = data['TASK_ASSIGNED_SUCCESSFULLY']
            cls.INVALID_DUE_DATE = data['INVALID_DUE_DATE']
            cls.NEXT = data['NEXT']
            cls.ENTER_DATE_IN_FORMAT = data['ENTER_DATE_IN_FORMAT']
            cls.TASK_TITLE = data['TASK_TITLE']
            cls.TASK_DESCRIPTION = data['TASK_DESCRIPTION']
            cls.TASK_NAME_TO_UPDATE = data['TASK_NAME_TO_UPDATE']
            cls.TASKS_THAT_CAN_BE_DELETED = data['TASKS_THAT_CAN_BE_DELETED']
            cls.WHICH_TASK_TO_DELETE = data['WHICH_TASK_TO_DELETE']
            cls.ENTER_USER_ID = data['ENTER_USER_ID']
            cls.USERS_AVAILABLE = data['USERS_AVAILABLE']
            cls.WHICH_TASK = data['WHICH_TASK']
            cls.ENTER_TASK_ID = data['ENTER_TASK_ID']
            cls.STATUS = data['STATUS']
            cls.ONE = data['ONE']
            cls.TWO = data['TWO']
            cls.UPPER_Y =data['UPPER_Y']
            cls.LOWER_Y = data['LOWER_Y']
            cls.UPPER_N =data['UPPER_N']
            cls.LOWER_N = data['LOWER_N']
            cls.TODAY = data['TODAY']
            cls.IMPORTANT = data['IMPORTANT']
            cls.FOR_LATER = data['FOR_LATER']
            cls.THREE = data['THREE']
            cls.STR_THREE = data['STR_THREE']
            cls.STR_ZERO = data['STR_ZERO']
            cls.INVALID_USERNAME = data['INVALID_USERNAME']
            cls.INVALID_INPUT = data['INVALID_INPUT']
            cls.TASKID_NOT_FOUND = data['TASKID_NOT_FOUND']
            cls.ATTEMPTS_EXHAUSTED = data['ATTEMPTS_EXHAUSTED']
            cls.DB_CONNECTION_ERROR = data['DB_CONNECTION_ERROR']
            cls.ERROR_MESSAGE  = data['ERROR_MESSAGE']
            cls.PARAMS = data['PARAMS']
            cls.JWT_SECRET_KEY = data['JWT_SECRET_KEY']

    @classmethod
    def loadManagerQueries(cls):
        with open(F_PATH_MANAGER_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_FOR_CREATE_AUTH_TABLE = data['QUERY_FOR_CREATE_AUTH_TABLE']
            cls.QUERY_FOR_CREATE_TASKS_TABLE= data['QUERY_FOR_CREATE_TASKS_TABLE']
            cls.QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE = data['QUERY_FOR_CREATE_ASSIGNED_TASKS_TABLE']
            cls.QUERY_TO_ENABLE_FOREIGN_KEY = data['QUERY_TO_ENABLE_FOREIGN_KEY']
            cls.QUERY_TO_ADD_IN_AUTH_TABLE = data['QUERY_TO_ADD_IN_AUTH_TABLE']
            cls.QUERY_TO_VERIFY_LOGIN = data['QUERY_TO_VERIFY_LOGIN']
            cls.QUERY_TO_VIEW_ALL_USERS = data['QUERY_TO_VIEW_ALL_USERS']
            cls.INSERT_INTO_TASKS_TABLE_BY_MANAGER = data['INSERT_INTO_TASKS_TABLE_BY_MANAGER']
            cls.INSERT_INTO_ASSIGNED_TASKS_TABLE = data['INSERT_INTO_ASSIGNED_TASKS_TABLE']
            cls.VIEW_STATUS_OF_MY_ASSIGNED_TASKS  = data['VIEW_STATUS_OF_MY_ASSIGNED_TASKS']
            cls.UPDATE_STATUS_OF_MY_ASSIGNED_TASKS = data['UPDATE_STATUS_OF_MY_ASSIGNED_TASKS']
            cls.QUERY_TO_FETCH_ALL_TASK_IDS = data['QUERY_TO_FETCH_ALL_TASK_IDS']


    @classmethod
    def loadUserQueries(cls):
        with open(F_PATH_USER_QUERIES,'r') as f:
            data = yaml.safe_load(f)
            cls.INSERT_INTO_TASKS_TABLE = data['INSERT_INTO_TASKS_TABLE']
            cls.TASKS_CATEGORY_PROMPT = data['TASKS_CATEGORY_PROMPT']
            cls.UPDATE_TASKS_OPTIONS = data['UPDATE_TASKS_OPTIONS']
            cls.UPDATE_DUE_DATE = data['UPDATE_DUE_DATE']
            cls.UPDATE_TASK_STATUS = data['UPDATE_TASK_STATUS']
            cls.VIEW_TASKS = data['VIEW_TASKS']
            cls.DELETE_MY_TASKS = data['DELETE_MY_TASKS']
            cls.VIEW_TASKS_TO_DELETE = data['VIEW_TASKS_TO_DELETE']
            

  
Config.load()
Config.loadManagerQueries()
Config.loadUserQueries()
Config.load_print_statements()

    