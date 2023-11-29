from datetime import datetime

def parse_date(date_str, fmt):
    return datetime.strptime(date_str, fmt)

def format_date(date_obj, fmt):
    return date_obj.strftime(fmt)
