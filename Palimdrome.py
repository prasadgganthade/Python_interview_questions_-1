# Python programme to check if binary representationis a palimdrome
num = int(input('Enter the number : '))
bin_num = bin(num)
# remove ob from binary number
print(bin_num)
bin_num = bin_num[2:]
print('The binary number after removing first 2 characters :',bin_num)

if bin_num == bin_num[::-1]:
    print('Binary representation is palimdrome')
else:
    print('Binary number is not palimdrome')

"""
o/p
----------------------
0b1010
The binary number after removing first 2 characters : 1010
Binary number is not palimdrome
-------------------------------
0b101
The binary number after removing first 2 characters : 101
Binary representation is palimdrome
"""