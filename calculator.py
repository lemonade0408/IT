import re
from functools import wraps


def handle_errors(func):
    @wraps(func)
    def wrapper(expression):
        if not isinstance(expression, str):
            print("Ошибка: нужно ввести текстовый пример.")
            return None

        if len(expression) > 100 or not re.fullmatch(r"[0-9\s.+\-*/()%]+", expression):
            print("Ошибка: недопустимые символы или слишком длинный пример.")
            return None

        try:
            result = func(expression)
            print("Результат:", result)
            return result

        except ZeroDivisionError:
            print("Ошибка: делить на ноль нельзя!")

        except SyntaxError:
            print("Ошибка: неправильно записан пример!")

        except Exception as error:
            print("Произошла ошибка:", type(error).__name__)

        return None

    return wrapper


@handle_errors
def calculate(expression):
    return eval(expression, {"__builtins__": {}}, {})


while True:
    expression = input("Введите пример (или exit для выхода): ")

    if expression.lower() == "exit":
        break

    calculate(expression)