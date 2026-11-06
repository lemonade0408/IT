result = []

def razdelitel(a, b):
    if a < b:
        raise ValueError("Первое число меньше второго")

    if b > 100:
        raise IndexError("Второе число больше 100")

    return a / b


data = [
    (10, 2),
    (2, 5),
    ("123", 4),
    (18, 0),
    ([], 15),
    (8, 4),
    (150, 101)
]

for a, b in data:
    try:
        res = razdelitel(a, b)
        result.append(res)

    except (ValueError, IndexError, TypeError, ZeroDivisionError) as error:
        print(type(error).__name__, ":", error)

print("Результаты:", result)