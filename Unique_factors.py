# Python programme for product of unique prime factors of number

from functools import reduce

num = int(input('Enter the number : '))
factor_lst = []
while num > 0:
    for divisor in range(2,(num//2)+1):
        if num % divisor == 0:
            factor_lst.append(divisor)
            num = num//divisor
            break
        else:
            continue
    else:
        factor_lst.append(num)
        num = num//num
        break

unique_factors = set(factor_lst)
product = 1
print('Product of uniquefactors is :',reduce(lambda x,y:x*y,unique_factors))

"""
o/p
Enter the number : 50
Product of uniquefactors is : 10
"""