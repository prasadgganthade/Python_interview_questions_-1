# Exercise 1: Create a function in Python

def details(name,age):
    print('My name is',name)
    print('My age is',age)

details('prasad',29)
# Exercise 2: Create a function with variable length of arguments
def length(l1,l2,l3):
    print('The length are')
    print(l1)
    print(l2)
    print(l3)

length(20,40,60)

# Exercise 3: Return multiple values from a function

def value(a,b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
print(value(40,10))

# Exercise 4: Create a function with a default argument

def employee(name,salary=100000):
    print('Name :',name,'Salary :',salary)

employee('Prasad')
employee('Ganesh',50000)

# Exercise 5: Create an inner function to calculate the addition in the following way
def outer_func(a,b):

    # inner function
    def inner_func(a,b):
        add = a+ b
        return add
    a = inner_func(a,b)
    return a +5
print(outer_func(10,5))

# Exercise 6: Create a recursive function

def addition(num):
    if num:
        return num + addition((num-1))
    else:
        return 0
print(addition(10))

# Exercise 7: Assign a different name to function and call it through the new name
def display_student(name,age):
    print(name,age)

display_student('John',25)

show_student = display_student
show_student('John',25)