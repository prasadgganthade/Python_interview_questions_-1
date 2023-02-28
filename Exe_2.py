# Exercise 1: Accept numbers from a user
"""
number1 = int(input('Enter the number : '))
number2 = int(input('Enther the number : '))

result = number1 * number2
print('Multiplication is',result)

"""

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

print('My','name','is','james',sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

# Exercise 4: Display float number with 2 decimal places using print()

num = 490.856145
print('%.2f' % num)

# Exercise 5: Accept a list of 5 float numbers as an input from the user
"""

number = []

for i in range(0,5):
    print("Enter the number at location ",i,":")
    item = float(input())
    number.append(item)

print(number)
"""

# Exercise 7: Accept any three string from one input() call

"""
print('Enter the three strings')
name1 = input()
name2 = input()
name3 = input()
print(name1)
print(name2)
print(name3)
"""


# Exercise 8: Format variables using a string.format() method.
quantity = 5
money = 2000
price = 500
stament1 = "I have {1} rupees so I can buy {0} friuts for {2:.2f} rupees."
print(stament1.format(quantity,money,price))

# Exercise 9: Check file is empty or not
import os
size = os.stat("test.txt").st_size
if size == 0:
    print("file is empty")

# Exercise 10: Read line number 4 from the following file
