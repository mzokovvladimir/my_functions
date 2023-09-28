def open_or_senior(data: list[tuple[int, int]]) -> list[str]:
    new_list: list = []
    for a, b in data:
        if a > 55 and b > 7:
            new_list.append("Senior")
        else:
            new_list.append("Open")
    return new_list


# ['Open', 'Senior', 'Open', 'Senior']
l1 = [(45, 12), (55, 21), (19, -2), (104, 20)]
print(open_or_senior(l1))
l2 = [(16, 23), (73, 1), (56, 20), (1, -1)]
# ['Open', 'Open', 'Senior', 'Open']
print(open_or_senior(l2))
