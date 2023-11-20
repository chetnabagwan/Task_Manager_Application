import re

def password_validation(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    answer = re.search(pat,password)
    
    if answer is not None:
        return True
    else:
        return False
    
def username_validator(name):
    reg = "[A-Za-z]+"
    ans = re.match(reg,name)
    if ans is not None:
        return True
    else:
        return False

