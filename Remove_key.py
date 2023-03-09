# Python programme to remove a key from a dictionary

def remove_key(dic,key):
    if key in dic:
        dic.pop(key)
        return 'List after deleting key :',dic
    else:
        return 'No such key is present'

dic = {'Three':9,'Six':36,'Four':16,'Five':25}
print('Dictionary is :',dic)
print(remove_key(dic,input('Enter the key want to remove : ').capitalize()))

"""
o/p
-------------------------------
Dictionary is : {'Three': 9, 'Six': 36, 'Four': 16, 'Five': 25}
Enter the key want to remove : one
No such key is present
--------------------------------
Dictionary is : {'Three': 9, 'Six': 36, 'Four': 16, 'Five': 25}
Enter the key want to remove : six
('List after deleting key :', {'Three': 9, 'Four': 16, 'Five': 25})
"""



