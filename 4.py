def positive_sum(arr: list) -> int:
    return sum(x for x in arr if x > 0)


print(positive_sum([1, 2, 3, 4, 5]))
print(positive_sum([1, -2, 3, 4, 5]))
