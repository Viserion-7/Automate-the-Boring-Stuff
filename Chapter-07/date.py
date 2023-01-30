import re
inpt_date = input("Enter date: ")
dateRegex = re.compile(r'((0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-[12]\d{3})')
date = dateRegex.search(inpt_date)

day = date.group(2)
month = date.group(3)
temp = date.group(0)
year=int(temp[6:10])

if month in ['04','06','09','11']:
    if not int(day) or int(day) > 30:
        print("Invalid day")
elif month == '02':
    if (year%4==0):
        if (year % 100):
            if (year%400):
                pass
            else: 
                print("Invalid day")
    else:
        print("Invalid day")
elif month in ['01','03','05','07','08','10','12']:
    if not int(day) or int(day) > 31:
        print("Invalid day")
else:
    print("Invalid month")