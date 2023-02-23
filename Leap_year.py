 # 12) Write a Python program to check leap year.
def leapyear(year):
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print('The given year is leap year')
    else:
        print('The given year is not leap year')
year = int(input('Enter the year to check whether it is leap year : '))
leapyear(year)