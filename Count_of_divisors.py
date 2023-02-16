# Python program to check if a count of divisor is even or odd
def count_divisor(num):
    divisors = 0
    for i in range(1,(num//2)+1):
        if num % i == 0:
            divisors += 1
    print(divisors)
    if divisors % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = int(input('Enter number : '))
print('Count of divisor :',count_divisor(num))

"""
o/p
Enter number : 25
2
Count of divisor : Even
----------
Enter number : 30
7
Count of divisor : Odd
"""