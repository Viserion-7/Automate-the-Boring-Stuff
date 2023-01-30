import re
def check(pwd):
    if len(pwd) < 8:
        return False
    upper= re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    num = re.compile(r'[0-9]')
    
    c1 = upper.search(pwd)
    c2 = lower.search(pwd)
    c3 = num.search(pwd)
    print(pwd,c1,c2,c3)
    
    if c1 and c2 and c3:
        return True
    else:
        return False
        
c=input("Enter a password : ")
print(check(c))