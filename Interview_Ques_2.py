# 1 Print a number from -6 to 6
for i in range(-6,7):
    print(i)

# Given required 10 as key and 20 as value
k = [(10,20),(30,40),(50,60)]
# method 1
print(dict(k))
# method 2
def convert_dict(tup,di):
    for a, b in tup:
        di.setdefault(a,[]).append(b)
    return di
dict1 = {}
print(convert_dict(k,dict1))

# Using while loop print odd number less than 10 in reverse order
num = 10
while num > 0:
    if num % 2 != 0:
        print(num)
    num = num-1
# take your name and swap first and last character of your name
name = 'python'
first = name[0]
last = name[-1]
swap_string = last + name[1:-1] + first
print(swap_string)
# s = 'b2a4c3'
s = 'b2a4c3'
char = []
num = []
for i in s:
    if i.isalpha():
        char.append(i)
    else:
        x=int(i)
        num.append(x)
print(char)
print(num)
# given two list convert to dict
test_keys = ['uddhav','raj','aditya']
test_values = ['thackrey','thackrey','thackrey']
# method 1 using zip
result = dict(zip(test_keys,test_values))
print(result)
# method 2 using dict comprehenson
res = {test_keys[i] : test_values[i] for i in range(len(test_keys))}
print(res)
# iterate through char and give its index
s = 'karishma kapoor'
for index,ch in enumerate(s):
    print('Character is :',ch ,'index is :',index)
# convert to uppercase
print(test_keys)
print(list(x.upper() for x in test_keys))
# method 2
print(list(map(lambda y: y.upper(), test_keys)))
# print the table of 1 -10
for i in range(1,11):
    for j in range(1,11):
        print((i*j),end="\t")
    print()
# given
c = '1111100000'
b = ''
for i in c:
    if i == '1':
        b += '0'
    elif i == '0':
        b += '1'
print(b)
