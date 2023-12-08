from datetime import datetime
import hashlib

def parse_date(date_str, fmt):
    return datetime.strptime(date_str, fmt)

def format_date(date_obj, fmt):
    return date_obj.strftime(fmt)

def hash_pwd(password):
    h_pwd =  hashlib.sha256(password.encode()).hexdigest()
    return h_pwd