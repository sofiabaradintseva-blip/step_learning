import math
import inspect
import sys

print(inspect.ismodule(math))
print(inspect.isclass(math))

for name in dir(math):
    print(name)

print("*" * 50)
for name in dir(math):
    obj = getattr(math, name)

    if inspect.isfunction(obj):
        print(name)

print(math.sqrt(16))
print(inspect.signature(math.sqrt))

print(inspect.getmodule(math.sqrt))

def analyze_module(module):
    import inspect

    print(f"Аналізуємо модуль: {module.__name__}\n")
    for name in dir(module):
        obj = getattr(module, name)

        if inspect.isclass(obj):
            print(f"Клас: {name}")
        elif callable(obj):
            try:
                sig = inspect.signature(obj)
            except:
                sig = "невідомо"
            print(f"Функція: {name} {sig}")

analyze_module(math)

print("Python: ", sys.version)
print("OS: ", sys.platform)
print("Path to python: ", sys.executable)
print(len(sys.modules))
def multiply(a, b=10):
    return a*b

print("Name: ", multiply.__name__)
print("Arguments: ", inspect.signature(multiply))
print("Code: ", )
print(inspect.getsource(multiply))