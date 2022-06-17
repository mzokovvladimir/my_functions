def remove_every_other(my_list):
    return my_list[::2]


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([[1, 2]]))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
