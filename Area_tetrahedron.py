# 1. Python Program to calculate the area of a Tetrahedron
# area of tetrahedron = sqrt(3) *(side * side)

import math
def area_tetrahedron(side):
    area = math.sqrt(3) * side**2
    print('Area of tetrahedron is :',area)

side = int(input('Enter the side of tetrahedron : '))
area_tetrahedron(side)

# o/p -Enter the side of tetrahedron : 20
# Area of tetrahedron is : 692.8203230275509