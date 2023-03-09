# Python programme to ssort the dictonaries by keys

def sort_dict_by_keys(dict):
    return sorted(dict.items())
dict1 = {'Three':9,'Six':36,'Two':4,'Eight':64,'Five':25}
print(sort_dict_by_keys(dict1))

"""
o/p
[('Eight', 64), ('Five', 25), ('Six', 36), ('Three', 9), ('Two', 4)]

"""