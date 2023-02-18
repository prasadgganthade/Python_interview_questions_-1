# Pythonprogramme to calculate grade
def grade_calculator(marks):
    if marks > 90:
        return 'Grade A'
    elif marks > 80:
        return 'Grade B'
    elif marks > 70:
        return 'Garde C'
    elif marks > 60:
        return 'Grade D'
    elif marks > 35:
        return 'Just pass'
    else:
        return 'Fail'

marks = int(input('Enter the marks : '))
print('Grade of student is :',grade_calculator(marks))
