from datetime import datetime
import hashlib
import shortuuid

class DataNotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

class UserAlreadyExistError(Exception):
    pass

# def parse_date(date_str, fmt):
#     return datetime.strptime(date_str, fmt)

# def format_date(date_obj, fmt):
#     return date_obj.strftime(fmt)

def date_today():
    return datetime.strptime((datetime.strftime(datetime.now(),"%d-%m-%Y")),"%d-%m-%Y").strftime("%d-%m-%Y")

def hash_pwd(password):
    h_pwd =  hashlib.sha256(password.encode()).hexdigest()
    return h_pwd

def create_id():
    id = int(shortuuid.ShortUUID('123456789').random(length=4))
    return id