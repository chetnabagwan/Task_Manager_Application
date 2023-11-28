"""This file contains the input validations functions."""

import re

def password_validation(password):

    """Validates the password entered whether it meets the password requirements or not."""

    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*#?&])[A-Za-z\\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    answer = re.search(pat,password)
    
    if answer is not None:
        return True
    else:
        return False
  
    
def username_validator(name):
    
    """Validates the input entered."""

    reg = "^[a-zA-Z]+(?:\\s[a-zA-Z]+)*$"
    ans = re.fullmatch(reg,name)
    if ans is not None:
        return True
    else:
        return False

