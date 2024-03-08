import re


def regexcompile(password):
    
     if passRegex1.search(password) == None:
        return False
     if passRegex2.search(password) == None:
        return False
     if passRegex3.search(password) == None:
        return False
     if passRegex4.search(password) == None:
        return False
     else:
        return True

passRegex1 = re.compile(r'\w{8,}')
passRegex2 = re.compile(r'\d+')
passRegex3 = re.compile(r'[a-z]')
passRegex4 = re.compile(r'[A-Z]')    
    

    
