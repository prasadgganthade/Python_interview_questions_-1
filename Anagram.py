# 1. Python Program to Check if Two Strings are Anagram
# Sorted method
def check_anagran(s1,s2):

    if sorted(s1) == sorted(s2):
        print('Strings are anagram')
    else:
        print('Strings are not anagram')

s1 = 'listen'
s2 = 'silent'
check_anagran(s1,s2)

# o/p - Strings are anagram

# 2. Print anagrams together in Python using List and Dictionary
list1 = ['bat','bag','tab','gab']

def anagrams(list1):
    dct = {}
    for i in list1:
        item = ''.join(sorted(i))
        if item in dct:
            dct[item].append(i)
        else:
            dct[item] = [i]
    return list(dct.values())
print('The list of anagrams :',anagrams(list1))

# o/p - The list of anagrams : [['bat', 'tab'], ['bag', 'gab']]



