num: int = 0


class Count:
    count: int = num

    def __init__(self):
        self.count += 1

    def _count(self):
        self.count += 1


result: Count = Count()
print(result.count)

one: int = 1
two: int = 2
print(one and two)
list1: list = list("Logika")
print(list1)


class Count:
    def _count_(self) -> None:
        print("1")

    def __init__(self):
        print("2")


result: Count = Count()
