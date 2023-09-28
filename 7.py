def square_sum(numbers: list) -> int:
    return sum([i ** 2 for i in numbers])


print(square_sum([1, 2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
print(square_sum([-1, -2]))
print(square_sum([-1, 0, 1]))
