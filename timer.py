import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            print("Время выполнения:", round(end - start, 4), "сек.")

    return wrapper


@measure_time
def calculate():
    return sum(range(1000000))


if __name__ == "__main__":
    print("Результат:", calculate())