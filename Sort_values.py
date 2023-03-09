# Python programme to sort dictionaries by values

dict1 = {'Three':9,'Six':36,'Two':4,'Eight':64,'Five':25}

def sor_by_values(dict1):
    return sorted(dict1.items(),key=lambda x:x[1])

print(sor_by_values(dict1))

"""
o/p
[('Two', 4), ('Three', 9), ('Five', 25), ('Six', 36), ('Eight', 64)]


"""