# Exercise 1: Calculate the multiplication and sum of two numbers
number1 = 20
number2 = 30
mul = number1 * number2
add = number1 + number2
print('The multiplication of two number is',mul)
print('The addition of two given number is',add)

# Exercise 2: Print the sum of the current number and the previous number
previous_num = 0

for i in range(1,11):
    x_sum = previous_num + i
    print("Current number is",i,"previous number",previous_num,'Sum is',x_sum)
    previous_num = i
# Exercise 3: Print characters from a string that are present at an even index number
str1 = "pynative"
a = len(str1)

for i in range(0,a -1,2):
    print(str1[i])

# Exercise 4: Remove first n characters from a string
str1 = "pynative"
print(str1[4:])

# Exercise 5: Check if the first and last number of a list is the same
number1 = [10,20,30,40,10]
number2 = [75,65,35,75,30]

def first_last_num(numberlist):
    first_number = numberlist[0]
    last_number = numberlist[-1]

    if first_number == last_number:
        return True
    else:
        return False

print(first_last_num(number1))
print(first_last_num(number2))

# Exercise 6: Display numbers divisible by 5 from a list
list1 = [10,20,33,46,55]
a = []
for i in list1:
    if i % 5 == 0:
        a.append(i)
print(a)

# Exercise 7: Return the count of a given substring from a string

str1 = "Emma is good developer. Emma is writer. Emma is a good teacher"

b= str1.count('Emma')
print('The count of Emma is',b)

# Exercise 8: Print the following pattern
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

# Exercise 9: Check Palindrome Number

def palimdrome(number):
    original_number = number
    reverse_number = 0
    while number > 0:
        reminder = number % 10
        reverse_number = (reverse_number * 10) + reminder
        number = number // 10

    if original_number == reverse_number:
        print('Given number is palindrome')
    else:
        print('Given number is not palimdrome')

palimdrome(121)
palimdrome(521)

# Exercise 10: Create a new list from a two list using the following condition
# Odd number from first list and even number from second list
list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]

odd_num = []
for i in list1:
    if i % 2 != 0:
        odd_num.append(i)

even_num = []
for num in list2:
    if num % 2 == 0:
        even_num.append(num)

new_list = odd_num + even_num
print(new_list)

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 1550
print("Given number",number)

while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")

# Exercise 12: Calculate income tax for the given income by adhering to the below rules
income = 25000
tax = 0
print('Given income :',income)

if income < 10000:
    tax = 0
elif income <= 20000:
    x = income - 10000
    tax = (x * 10)/100
elif income > 20000:
    tax  = ((10000*10)/100) + (((income - 20000)*20)/100)
print('Total tax to pay is',tax)

# Exercise 13: Print multiplication table form 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print((i*j),end="\t")
    print()
# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
"""
* * * * *  
* * * *  
* * *  
* *  
*
"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base,exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base,"raises to the power of",exp,"is :",result)

exponent(5,4)
exponent(1,0)
