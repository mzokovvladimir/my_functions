def find_digit(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return arr[i]


my_list = [2, 2, 1, 2, 2, 2, 2]
print(find_digit(my_list))
