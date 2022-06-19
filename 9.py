d = {"a": 3, "b": 0, "c": 4, "d": -3}
for key, value in d.items():
    if value == max(d.values()):
        print(key, value)

print({key: value for key, value in d.items() if value == max(d.values())})
