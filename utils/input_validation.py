import re

def password_validation(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg)
    answer = re.search(reg,password)
    
    if answer is not None:
        return True
    else:
        return False
    
print(password_validation("Chetna@12"))
