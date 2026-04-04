import colorama
import inspect

def analyze_module(module):
    print(f"Аналізуємо модуль: {module.__name__}\n")

    for name in dir(module):
        if name.startswith("_"):
            continue

        obj = getattr(module, name)

        if inspect.isclass(obj):
            print(f"Клас: {name}")

        elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
            try:
                sig = inspect.signature(obj)
            except ValueError:
                sig = "(невідомо)"
            print(f"Функція: {name}{sig}")

        else:
            print(f"Інше: {name} (тип: {type(obj).__name__})")

analyze_module(colorama)