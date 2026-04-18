class MyIterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i * 2


obj = MyIterable(5)

for num in obj:
    print(num)