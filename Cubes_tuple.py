# Python program - Create a list of tuples from the given list  having a number and its cube in each tuple

list1 = [1,3,5,7,9]

def cube_tuple(list1):
    return [(i, i ** 3) for i in list1]

print('List of tuples :',cube_tuple(list1))

"""
o/p
List of tuples : [(1, 1), (3, 27), (5, 125), (7, 343), (9, 729)]
"""