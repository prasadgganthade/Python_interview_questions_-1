# 1. Take a list and random number
"""
suaring of each number in the list
Find 2nd largest number from list
middle number of list
"""
list1 = [1,5,8,3,10]
square_list = []
for i in list1:
    a = i*i
    square_list.append(a)
print(square_list)
list1.sort()
print(list1)
second_last = list1[-2]
print('Second max number is:',second_last)
# middle number
middle_index = int((len(list1) - 1)/2)
print('Middle number is :',list1[middle_index])
# 2
"""
Take 2 tuple and take random number in it do the element by element addition with new tuple
"""
tup1 = (1,5,10)
tup2 = (10,20,30)
result = tuple(map(lambda x,y:x + y,tup1,tup2))
print('Addition of tuple is :',result)
# 3 Take one string and count vowels in the string
def vowel_count(str):
    count = 0
    vowels = set('aeiouAEIOU')
    for i in str:
        if i in vowels:
            count = count + 1
    print('The number of vowels is :',count)

string1 = 'Geeksfor geeks'
vowel_count(string1)
# method 2
string2 = 'Hello world WELCOME'
count1 = 0
for i in range(len(string2)):
    if (string2[i] == 'a') or (string2[i] == 'e') or (string2[i] == 'i') or (string2[i] == 'o') or (string2[i] == 'u') or (string2[i] == 'A') or (string2[i] == 'E') or (string2[i] == 'I') or (string2[i] == 'O') or (string2[i] == 'U'):
        count1 = count1 + 1
print('No of vowels are :',count1)
# 4
"""
Take your name 
- characters present at even index
- character present at odd index
"""
name = 'PrasadGanthade'
even_char = name[1::2]
odd_char = name[::2]
print('Character of even index : ',even_char)
print('Character of odd index : ',odd_char)
# 5 Break your name 5 times using while loop
c = 0
while c < 5:
    print(name)
    c = c+1
# 6 Take one empty dict, add four key value pair using for loop, and addition of all values
dicts = {}

keys = ['A','B','C','D']
values = [10,12,14,16]
for i in range(len(keys)):
    dicts[keys[i]] = values[i]
print(dicts)
def sum_values(dict):
    return sum(dict.values())
print(sum_values(dicts))
# print left traingle pattern
n = 5
for i in range(n + 1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
# 8. filter value by asscending
tup = [('suresh',87),('ramesh',45),('dinesh',70)]
def sort_tuple(tup):
    tup.sort(key= lambda x: x[1])
    return tup
print(sort_tuple(tup))
# 9 Print pattern for alphabet
n = 6

for i in range(n+1):
    for j in range(n - i - 1):
        print(chr(65 + j),end=" ")
    print()
#10  calculate addition of marks in string
s = 'deepali got 78 88 90 91 marks in four subject'
a = s.split()
print(a)
sum = 0
for i in a:
    if i.isdigit() == True:
        z = int(i)
        sum = sum +z
print(sum)
# 11 reversing of words in python
s = 'python java'
a = s.split()

print(a)
b = " ".join(reversed(a))[::-1]
print(b)

