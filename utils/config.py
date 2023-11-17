import yaml


FPATH = 'yml_files\\prompts.yml'
FPATH_PRINT_STATEMENTS = 'yml_files\\print_statements.yml'
FPATH_LOGGING_STATEMENTS = 'yml_files\\logging_statements.yml'
F_PATH_MANAGER_QUERIES = 'db\\queries\\manager_queries.yml'
F_PATH_USER_QUERIES = 'db\\queries\\user_queries.yml'

class Config:
    """
    Maintains all the config variables
    """
    @classmethod
    def load(cls):
        with open(FPATH, 'r') as f:
            data = yaml.safe_load(f)
            cls.MANAGER_PROMPT = data['MANAGER_PROMPT']
            cls.USER_PROMPT = data['USER_PROMPT']
            cls.MANAGER_PROMPT_WLCM = data['MANAGER_PROMPT_WLCM']
            cls.USER_PROMPT_WLCM = data['USER_PROMPT_WLCM']
            cls.ATTEMPTS = data['ATTEMPTS']
            cls.PASSWORD_REQUIREMENTS = data['PASSWORD_REQUIREMENTS']
            cls.MANAGER = data['MANAGER']
            
          
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
            cls.ENTER_DEFAULT_PASSWORD = data['ENTER_DEFAULT_PASSWORD']
            cls.ENTER_NEW_PASSWORD = data['ENTER_NEW_PASSWORD']
            cls.CONFIRM_PASSWORD = data['CONFIRM_PASSWORD'] 
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
            cls.STATUS = data['STATUS']
            cls.ONE = data['ONE']
            cls.TWO = data['TWO']
            cls.UPPER_Y =data['UPPER_Y']
            cls.LOWER_Y = data['LOWER_Y']
            cls.TODAY = data['TODAY']
            cls.IMPORTANT = data['IMPORTANT']
            cls.FOR_LATER = data['FOR_LATER']
            cls.THREE = data['THREE']
            cls.STR_THREE = data['STR_THREE']
            cls.INVALID_USERNAME = data['INVALID_USERNAME']
            cls.INVALID_INPUT = data['INVALID_INPUT']
            cls.TASKID_NOT_FOUND = data['TASKID_NOT_FOUND']




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
            
    @classmethod
    def loader(cls,func):
        def wrapper_func():
            Config.load()
            Config.loadManagerQueries()
            Config.loadUserQueries()
            Config.load_print_statements()
            func()      

        return wrapper_func
    