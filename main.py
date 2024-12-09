def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

print_params(1, 'String', c = True)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = (9,7), True, {'Vasya': 89009666666}
values_dict = {'a': 1608, 'b': 1919, 'c': 2255}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = 1000, True
print_params(values_list_2, 42)
