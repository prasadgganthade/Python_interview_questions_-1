import datetime
today_date = datetime.date.today()
print('Todays date is :',today_date) #Todays date is : 2023-02-16

print('Formatted date is :',today_date.strftime("%d-%m-%y"))

"""
o/p
Todays date is : 2023-02-16
Formatted date is : 16-02-23
"""