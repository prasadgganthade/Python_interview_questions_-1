# Python programs for common divisors of two numbers

def common_divisors(num1,num2):
    min_num = min(num1,num2)
    common_division = []

    for i in range(1,min_num+1):
        if num1 % i == 0 and num2 % i == 0:
            common_division.append(i)
    return common_division

num1,num2 = map(int,input('Enter two number seperated by coma : ').split(','))
print('Common divisors of two number is :',common_divisors(num1,num2))


"""
o/p
Enter two number seperated by coma : 20,10
Common divisors of two number is : [1, 2, 5, 10]
"""