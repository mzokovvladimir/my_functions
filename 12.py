num = 0


class Count:
    count = num

    def __init__(self):
        self.count += 1

    def _count(self):
        self.count += 1


result = Count()
print(result.count)

one = 1
two = 2
print(one and two)
list1 = list("Logika")
print(list1)


class Count:
    def _count_(self):
        print("1")

    def __init__(self):
        print("2")


result = Count()
