# Python programme to convert a list of tuple into dictionary

list_tuple = [(12,45),(31,23),(67,55),(43,84),(98,32)]

def list_to_dict(list1):
    dict1 = {}
    for i,j in list1:
        dict1.update({i:j})
    return dict1
print('Dictionay :',list_to_dict(list_tuple))

"""
o/p-
Dictionay : {12: 45, 31: 23, 67: 55, 43: 84, 98: 32}
"""
