immutable_var = ([0, 3], 10, 'december', True)
print(immutable_var)
# immutable_var[1] = 11
# Изменения в кортеже приводят к ошибке, так как это неизменяемый тип данных

mutable_list = [1, 2, 'a', 'b', 'Mod']
mutable_list[3] = 'bob'
print(mutable_list)