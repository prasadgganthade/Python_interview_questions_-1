# Python program to find the perimeter of a cylinder
# perimeter of cylinder = 4 * pi * radius + 2 * height

from math import pi
def cylinder_perimeter(radius,height):
    perimeter = 4 * pi * radius + 2 * height
    return perimeter

radius,height = map(int,input('Enter the radius and height of cylinder seperated by space : ').split())
print('Perimeter of cylinder is :',cylinder_perimeter(radius,height))

"""
o/p
Enter the radius and height of cylinder seperated by space : 5 10
Perimeter of cylinder is : 82.83185307179586
"""