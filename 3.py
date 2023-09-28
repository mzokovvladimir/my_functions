def get_sum(a: int, b: int) -> int:
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum(0, 1))
print(get_sum(0, -1))
