my_dict = {'mau': 16, 'gav': 26, 'kva': 43}
print(my_dict)
print(my_dict['gav'])
print(my_dict.get('chick', 'no'))
my_dict.update({'ku': 3, 'zhu': 31})
print(my_dict.pop('mau'))
print(my_dict.keys())

my_set = {13, 15, 15, 13, 43, '43', 43.0}
print(my_set)
my_set.update([1, '3'])
my_set.discard(43)
print(my_set)