for letter in "Python":
    print(letter)

my_list = [10, 12, 8, 7, 11]
iterator = iter(my_list)
print(iterator)
'''
print(next(iterator))
print(next(iterator))
'''

for elem in iterator:
    print(elem)

class Counter:
    def __init__(self, max_numbers):
        self.i =0
        self.max_numbers = max_numbers

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.max_numbers:
            raise StopIteration
        return self.i

count = Counter(5)
print("*"*50)
for elem in count:
    print(elem)
print("*" * 50)
def squeres(n):
    for i in range(n):
        yield i**2

for num in squeres(5):
    print(num)

print("*"*50)
def raise_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_degrees(2, 5)
for value in res:
    print(value)

print("*"*50)

class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, new_work):
        return f"I help with {self.work}, then with {new_work}"

helper = Helper("homework")
print(helper("classwork"))

print("*"*50)


def helper(work):
    work_in_memory = work

    def inner(new_work):
        return f"I help with {work_in_memory} then with {work}"
    return inner

h = helper("homework")
print(h("cleaning"))
print(h("driving"))